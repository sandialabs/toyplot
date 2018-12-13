
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _labels-and-legends:

Labels and Legends
==================

Of course, most figures must be properly labelled before they can be of
value, so Toyplot provides several mechanisms to help:

Coordinate System Labels
------------------------

First, :ref:`cartesian-coordinates`, :ref:`numberline-coordinates`,
and :ref:`table-coordinates` provide labels that can be specified when
they are created. In all cases the ``label`` parameter provides a
top-level label for the coordinate system:

.. code:: python

    import numpy
    import toyplot
    
    canvas = toyplot.Canvas(width=600, height=600)
    canvas.cartesian(grid=(2,2,0), label="Cartesian Coordinates").plot(numpy.linspace(0, 1)**2)
    canvas.numberline(grid=(2,2,1), label="Numberline Coordinates").scatterplot(numpy.random.normal(size=100))
    canvas.table(grid=(2,2,2), label="Table Coordinates", data = numpy.random.random((4, 3)));



.. raw:: html

    <div class="toyplot" id="tc3be864166ad4040ad309815fe1c8b97" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600.0px" id="t0a7cdf1c26fb47ad8e0b00f34dcd7de2" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 600.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tc1e8861c2443414083bd5094cf8124f0"><clipPath id="t154a0892b1bf46e2822f4a9a4f53a132"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t154a0892b1bf46e2822f4a9a4f53a132)"><g class="toyplot-mark-Plot" id="t1fa2d970316045f09f94f8a20e62b649" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 54.0 249.9167013744273 L 58.0 249.66680549770928 L 62.0 249.2503123698459 L 66.0 248.66722199083716 L 70.0 247.91753436068305 L 74.0 247.0012494793836 L 78.0 245.91836734693877 L 82.0 244.6688879633486 L 86.0 243.25281132861306 L 90.0 241.6701374427322 L 94.0 239.92086630570594 L 98.0 238.00499791753435 L 102.0 235.92253227821743 L 106.0 233.67346938775512 L 110.0 231.25780924614745 L 114.0 228.67555185339444 L 118.0 225.92669720949604 L 122.0 223.0112453144523 L 126.0 219.92919616826322 L 130.0 216.6805497709288 L 134.0 213.26530612244898 L 138.0 209.68346522282383 L 142.0 205.93502707205332 L 146.0 202.01999167013744 L 150.0 197.9383590170762 L 154.0 193.69012911286964 L 158.0 189.2753019575177 L 162.0 184.69387755102045 L 166.0 179.94585589337777 L 170.0 175.03123698458978 L 174.0 169.9500208246564 L 178.0 164.7022074135777 L 182.0 159.2877967513536 L 186.0 153.70678883798416 L 190.0 147.9591836734694 L 194.0 142.04498125780927 L 198.0 135.96418159100375 L 202.0 129.7167846730529 L 206.0 123.30279050395671 L 210.0 116.72219908371514 L 214.0 109.97501041232822 L 218.0 103.06122448979593 L 222.0 95.9808413161183 L 226.0 88.73386089129534 L 230.0 81.32028321532698 L 234.0 73.74010828821326 L 238.0 65.99333610995419 L 242.0 58.079966680549774 L 246.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="te32a692435db4f5383796c79ce7dbbfd" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="196.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(40.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(80.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g><g transform="translate(120.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">30</text></g><g transform="translate(160.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">40</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t33bdc6835ad14323b8ffc2c574c5a6e5" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g><g transform="translate(150.0,42.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-74.683" y="-4.823">Cartesian Coordinates</text></g></g><g class="toyplot-coordinates-Numberline" id="t60288bc18e3f4f3992c856e699aeb89f"><clipPath id="t91ae23ebc73e4477a10022201b304d40"><rect height="40.0" width="200.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t91ae23ebc73e4477a10022201b304d40)" transform="translate(350.0,150.0)"><g class="toyplot-mark-Point" id="tdd838ec62804476cb9c6b95c28888984"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(122.66017388963544, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(29.573204075346148, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(43.22198100131734, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(110.8564053193853, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(0.0, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(62.01319029922261, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(62.63336193293901, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(66.32388155593888, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(91.4437625023873, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(89.4021296226603, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(103.66067012889233, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(138.66895269216877, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(12.933016089105045, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(111.95694200298973, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(96.1179288549211, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(97.99399777906015, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(121.19682272776897, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(88.09647684092808, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(77.02544883195324, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(117.82211023817123, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(81.26098900781716, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(101.47162514957986, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(174.80609090628658, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(195.71590634976016, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(67.11722603668026, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(90.2026970246305, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(83.31886601435667, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(78.13305137993838, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(115.99942278223226, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(133.71012768705563, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(93.5762684048264, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(44.08352571072155, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(99.08304519237805, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(90.81113083263335, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(173.00421115242034, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(144.6689431699854, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(75.42780023196698, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(43.68196331533516, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(46.392549379517895, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(107.06289441824283, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(115.11935492273322, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(132.24243561056352, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(84.37701754171272, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(40.29121765097386, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(83.41276205878842, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(120.01565685632202, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(69.9710056555927, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(159.92696460239168, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(168.9227744082306, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(73.9263977351104, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(43.16072117332666, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(146.87795273269813, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(200.0, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(105.24097872500762, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(96.35896315977548, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(95.76320267208479, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(115.96110884863245, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(96.94625542444591, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(70.12483976085215, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(87.02352262566424, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(57.35001783199889, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(138.47975406924738, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(51.2895199227998, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(66.91840678660496, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(85.81410140981927, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(142.66051890428767, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(107.12397881904107, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(129.95527897310194, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(77.44298111674468, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(65.57951324135396, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(92.29506046217274, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(138.69039551752584, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(73.4815060211574, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(14.868119038600081, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(123.87218320613908, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(109.7416779623894, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(77.96181212575569, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(81.27630959487374, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(89.63822987917935, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(138.53372650414494, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(89.03659138584096, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(13.876585703091294, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(174.99510660630548, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(102.83720412930346, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(42.44068086526988, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(58.93889217903959, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(67.63385273704972, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(172.8139629593245, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(130.70296459973133, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(34.80855654075546, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(80.2462146874708, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(127.21903635388496, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(99.63390293422587, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(76.12526059256562, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(112.93027807035101, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(117.91020091414379, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(95.45491296920692, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(53.59520866976774, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(76.57842973191762, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(145.24245614663278, 0)"><circle r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t638cec8392794d7995cd6297ccc09008" transform="translate(350.0,150.0)translate(0,20.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(10.943157776003407,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.445" y="8.555">-2</text></g><g transform="translate(94.18615273071521,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(177.42914768542698,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">2</text></g></g><g transform="translate(100.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-69.678" y="10.265999999999998">Numberline Coordinates</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Table" id="t35e23d5b92dc4f00b9b7ce0aae0dc534"><g transform="translate(150.0,350.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-61.068000000000005" y="-10.423">Table Coordinates</text></g><g transform="translate(83.33333333333334,370.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">0</text></g><g transform="translate(150.0,370.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">1</text></g><g transform="translate(216.66666666666669,370.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.3360000000000003" y="3.066">2</text></g><g transform="translate(81.33333333333334,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(83.33333333333334,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(85.33333333333334,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0959942</text></g><g transform="translate(148.0,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(150.0,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(152.0,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">342215</text></g><g transform="translate(214.66666666666669,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(216.66666666666669,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(218.66666666666669,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">643352</text></g><g transform="translate(81.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(83.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(85.33333333333334,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">78201</text></g><g transform="translate(148.0,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(150.0,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(152.0,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">922674</text></g><g transform="translate(214.66666666666669,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(216.66666666666669,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(218.66666666666669,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">164269</text></g><g transform="translate(81.33333333333334,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(83.33333333333334,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(85.33333333333334,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">771373</text></g><g transform="translate(148.0,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(150.0,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(152.0,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">927859</text></g><g transform="translate(214.66666666666669,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(216.66666666666669,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(218.66666666666669,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">502476</text></g><g transform="translate(81.33333333333334,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(83.33333333333334,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(85.33333333333334,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">649282</text></g><g transform="translate(148.0,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(150.0,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(152.0,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">921088</text></g><g transform="translate(214.66666666666669,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672000000000001" y="3.066">0</text></g><g transform="translate(216.66666666666669,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.6680000000000001" y="3.066">.</text></g><g transform="translate(218.66666666666669,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">219075</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.0" y1="390.0" y2="390.0"></line></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tc3be864166ad4040ad309815fe1c8b97";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t0a7cdf1c26fb47ad8e0b00f34dcd7de2";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t1fa2d970316045f09f94f8a20e62b649","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"te32a692435db4f5383796c79ce7dbbfd",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t33bdc6835ad14323b8ffc2c574c5a6e5",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tdd838ec62804476cb9c6b95c28888984","data","point data",["x0"],[[0.6841181332894496, -1.5523936564397187, -1.2244675184290241, 0.40052025032831956, -2.2629208086988464, -0.772989065302041, -0.7580887932958787, -0.6694202002206849, -0.06588879292053065, -0.11494115776727255, 0.2276351878817361, 1.0687457842105357, -1.9521915732564832, 0.42696179497007986, 0.04641294141944036, 0.09148745910491568, 0.6489595914166443, -0.14631083115402557, -0.4123038559123972, 0.5678785949572128, -0.3105405741331135, 0.17504109319536884, 1.9369783179817721, 2.439358499157365, -0.650359269479954, -0.09570668879109633, -0.2610979271534105, -0.38569254649019974, 0.5240866228656119, 0.9496048280781677, -0.014653108678288593, -1.203768005878498, 0.11765296201384857, -0.08108843032180746, 1.8936862726908363, 1.2129018295589984, -0.45068903416926964, -1.213415962336693, -1.148291297716987, 0.30937718409899123, 0.5029420722646198, 0.9143419911922385, -0.2356747302121729, -1.29488217258552, -0.2588419764999572, 0.6205808462239812, -0.5817942299720643, 1.5794917496047005, 1.7956254870016568, -0.48676179915504203, -1.2259393498551763, 1.2659755942382855, 2.5422883289303235, 0.26560375441337203, 0.052204042640281924, 0.03789027394383331, 0.5231660905464506, 0.06631435342354842, -0.5780982047307058, -0.17208967815124335, -0.8850266600512621, 1.064200089452092, -1.0306364597105917, -0.6551361098659462, -0.20114728753934707, 1.1646473363901635, 0.3108448007034027, 0.8593906613246401, -0.40227220616172277, -0.6873044273557101, -0.04543546924450029, 1.069260970512248, -0.4974507878007541, -1.9056987013806497, 0.7132379245022245, 0.37373775991930985, -0.3898067486347971, -0.31017248100852346, -0.10926860221716295, 1.065496833638841, -0.12372359614585841, -1.9295213266009035, 1.9415196178262026, 0.20785055615297976, -1.2432390711938548, -0.8468522923965391, -0.6379467727731616, 1.8891153609114282, 0.8773545903504077, -1.4266088389122475, -0.3349215883169125, 0.7936495711414813, 0.1308878952871534, -0.43393181967985595, 0.4503472117944223, 0.5699950655628291, 0.030483291457304777, -0.9752398765332959, -0.42304395723332694, 1.2266810785386726]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t638cec8392794d7995cd6297ccc09008",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 2.5422883289303235, "min": -2.2629208086988464}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t35e23d5b92dc4f00b9b7ce0aae0dc534","data","table data",["0", "1", "2"],[[0.09599421007290054, 0.7820097830483989, 0.7713732019547355, 0.6492822990613943], [0.34221531379558756, 0.9226742236252384, 0.9278585854677817, 0.9210878053590125], [0.6433517650660396, 0.16426912405229266, 0.5024755502941332, 0.21907542721076567]],"toyplot");
    })();</script></div></div>


Naturally, some coordinate systems - such as Cartesian - allow you to
specify additional, axis-specific labels:

.. code:: python

    canvas = toyplot.Canvas(width=300, height=300)
    axes = canvas.cartesian(label="Cartesian Coordinates", xlabel="Days", ylabel="Users")
    axes.plot(numpy.linspace(0, 1)**2);



.. raw:: html

    <div class="toyplot" id="t3881a53e4fd7496f846c2c1a080d3f88" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t4caa09420c864933baf1e5d53b6dbc96" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t279c35ecda9440d5a7c9617b41ebac86"><clipPath id="ta9d3d8a463484f4387df9c8140140a4f"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#ta9d3d8a463484f4387df9c8140140a4f)"><g class="toyplot-mark-Plot" id="tfd204e084eab4352a8d2d49e32d07a83" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 54.0 249.9167013744273 L 58.0 249.66680549770928 L 62.0 249.2503123698459 L 66.0 248.66722199083716 L 70.0 247.91753436068305 L 74.0 247.0012494793836 L 78.0 245.91836734693877 L 82.0 244.6688879633486 L 86.0 243.25281132861306 L 90.0 241.6701374427322 L 94.0 239.92086630570594 L 98.0 238.00499791753435 L 102.0 235.92253227821743 L 106.0 233.67346938775512 L 110.0 231.25780924614745 L 114.0 228.67555185339444 L 118.0 225.92669720949604 L 122.0 223.0112453144523 L 126.0 219.92919616826322 L 130.0 216.6805497709288 L 134.0 213.26530612244898 L 138.0 209.68346522282383 L 142.0 205.93502707205332 L 146.0 202.01999167013744 L 150.0 197.9383590170762 L 154.0 193.69012911286964 L 158.0 189.2753019575177 L 162.0 184.69387755102045 L 166.0 179.94585589337777 L 170.0 175.03123698458978 L 174.0 169.9500208246564 L 178.0 164.7022074135777 L 182.0 159.2877967513536 L 186.0 153.70678883798416 L 190.0 147.9591836734694 L 194.0 142.04498125780927 L 198.0 135.96418159100375 L 202.0 129.7167846730529 L 206.0 123.30279050395671 L 210.0 116.72219908371514 L 214.0 109.97501041232822 L 218.0 103.06122448979593 L 222.0 95.9808413161183 L 226.0 88.73386089129534 L 230.0 81.32028321532698 L 234.0 73.74010828821326 L 238.0 65.99333610995419 L 242.0 58.079966680549774 L 246.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="t08e1de4410f149b3a6ad0c60e79351a4" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="196.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(40.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(80.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g><g transform="translate(120.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">30</text></g><g transform="translate(160.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">40</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g></g><g transform="translate(100.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-14.340000000000002" y="10.265999999999998">Days</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tea4ab178e52b4ea8830b817c5c14e829" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">1.0</text></g></g><g transform="translate(100.0,-22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-16.674" y="0.0">Users</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g><g transform="translate(150.0,42.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-74.683" y="-4.823">Cartesian Coordinates</text></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t3881a53e4fd7496f846c2c1a080d3f88";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t4caa09420c864933baf1e5d53b6dbc96";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tfd204e084eab4352a8d2d49e32d07a83","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t08e1de4410f149b3a6ad0c60e79351a4",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tea4ab178e52b4ea8830b817c5c14e829",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Coordinate System Text
----------------------

Another option for labelling a figure is to insert text using the same
domain as the data. For example, we can label individual series in a
plot:

.. code:: python

    def series(x):
        return numpy.cumsum(numpy.random.normal(loc=0.05, size=len(x)))
    
    numpy.random.seed(1234)
    x = numpy.arange(100)
    y = numpy.column_stack([series(x) for i in range(5)])

.. code:: python

    label_style = {"text-anchor":"start", "-toyplot-anchor-shift":"5px"}
    canvas, axes, mark = toyplot.plot(x, y)
    for i in range(y.shape[1]):
        axes.text(x[-1], y[-1,i], "Series %s" % i, style=label_style)



.. raw:: html

    <div class="toyplot" id="t89d610a233bc4923a99aa49f99edeb1e" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="t1c0a0ea4401447d0ac9f7918763dec18" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t4fd54345db444449927b73f9fb2aa77f"><clipPath id="t087f2f6158424112b6bb1516429927db"><rect height="520.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t087f2f6158424112b6bb1516429927db)"><g class="toyplot-mark-Plot" id="tdb513cd0765349e98d8bdb254cf3f029" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 343.3300205953749 L 54.59959732549238 358.7920369979883 L 59.19919465098476 338.69902399829283 L 63.79879197647714 342.2583705684162 L 68.39838930196953 351.3459033202555 L 72.99798662746191 338.645870513082 L 77.5975839529543 326.3195159397324 L 82.19718127844668 334.2678325321839 L 86.79677860393906 333.37754329294927 L 91.39637592943143 363.0918754077105 L 95.99597325492383 346.8295026460248 L 100.5955705804162 332.70949416307025 L 105.19516790590859 319.1128731325027 L 109.79476523140096 345.82647843101597 L 114.39436255689336 349.6761738365487 L 118.99395988238572 348.96988796792573 L 123.59355720787812 342.7977774199124 L 128.1931545333705 338.2025479353999 L 132.79275185886289 319.6211964170079 L 137.39234918435525 339.90662258741213 L 141.99194650984765 341.975220530528 L 146.59154383534002 350.18705885629316 L 151.1911411608324 346.88831609324103 L 155.79073848632478 338.71076911964946 L 160.39033581181715 320.1701622775058 L 164.98993313730955 325.8524088143114 L 169.58953046280195 316.0200090382306 L 174.18912778829431 339.9660090171619 L 178.7887251137867 341.76983923118337 L 183.38832243927908 326.74156137410824 L 187.98791976477148 331.4553439190562 L 192.58751709026387 326.2049539388292 L 197.18711441575624 311.33103683791296 L 201.7867117412486 296.4793486175726 L 206.38630906674095 284.0970412494765 L 210.98590639223335 285.07399555091905 L 215.58550371772574 282.70636005311985 L 220.1851010432181 286.4031590107421 L 224.7846983687105 274.3195632758751 L 229.38429569420288 241.2407065541016 L 233.98389301969527 239.53050351805496 L 238.58349034518764 246.52915869095634 L 243.18308767068004 245.36179987328694 L 247.78268499617243 272.8034333998005 L 252.3822823216648 268.76788040910606 L 256.9818796471572 280.2481881469161 L 261.58147697264957 281.4243947407773 L 266.18107429814194 280.4989687201691 L 270.7806716236343 269.5843416474706 L 275.38026894912673 265.98953487895074 L 279.9798662746191 253.91496338192485 L 284.57946360011147 272.83038673960164 L 289.1790609256039 291.15175252455737 L 293.77865825109626 291.8417742721321 L 298.37825557658863 298.59374362393095 L 302.97785290208105 299.875986880472 L 307.5774502275734 294.40087550655176 L 312.1770475530658 294.2045541985582 L 316.7766448785582 285.86033106372054 L 321.3762422040506 264.23664291281534 L 325.97583952954295 276.7614998566594 L 330.5754368550353 277.0372049614677 L 335.17503418052775 272.18616357938197 L 339.7746315060201 274.33407127479313 L 344.3742288315125 259.64686559487825 L 348.97382615700485 291.4992116248591 L 353.5734234824972 263.30375797759905 L 358.1730208079896 278.11063159573075 L 362.7726181334819 274.56169953634054 L 367.3722154589744 264.3340472500366 L 371.9718127844667 274.3003518436393 L 376.57141010995906 267.3611364932593 L 381.1710074354515 257.1401569864081 L 385.77060476094385 249.3682213985208 L 390.3702020864362 261.2428464510297 L 394.9697994119286 233.35583570526822 L 399.569396737421 229.60255736184212 L 404.1689940629134 244.54532372648018 L 408.76859138840575 235.30342889360318 L 413.3681887138982 234.09039110820942 L 417.96778603939055 227.11956552076202 L 422.5673833648829 274.7332460658253 L 427.1669806903753 256.1526070439136 L 431.7665780158677 253.40664414882914 L 436.3661753413601 250.49943120200186 L 440.96577266685244 255.65032603189297 L 445.56536999234487 244.57369323610104 L 450.16496731783724 230.54890055625543 L 454.7645646433296 226.20106985300572 L 459.364161968822 206.65988744320293 L 463.9637592943144 204.90031974793388 L 468.56335661980677 209.64289061264935 L 473.16295394529914 222.89430468552675 L 477.76255127079156 230.14057802127687 L 482.36214859628393 218.3968664165042 L 486.9617459217763 218.82979924903583 L 491.56134324726867 222.82434266348673 L 496.1609405727611 214.98762814843693 L 500.76053789825346 228.79652991325702 L 505.36013522374583 235.05574858979216" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g><g class="toyplot-Series"><path d="M 50.0 345.77241809643766 L 54.59959732549238 337.41741617132186 L 59.19919465098476 329.9153765578214 L 63.79879197647714 325.37159231958105 L 68.39838930196953 318.13114749557167 L 72.99798662746191 298.97624837605395 L 77.5975839529543 308.88387562867604 L 82.19718127844668 314.54867291005473 L 86.79677860393906 297.27618439277626 L 91.39637592943143 313.95963911664523 L 95.99597325492383 301.4179894621467 L 100.5955705804162 323.92329584101935 L 105.19516790590859 329.3542937378522 L 109.79476523140096 318.5243663933661 L 114.39436255689336 320.61039899826847 L 118.99395988238572 322.40158385231877 L 123.59355720787812 312.50004504055596 L 128.1931545333705 336.46598973535095 L 132.79275185886289 335.1505162992399 L 137.39234918435525 329.1221771390492 L 141.99194650984765 331.8112437807626 L 146.59154383534002 339.50456235356603 L 151.1911411608324 348.08113657811043 L 155.79073848632478 341.49158073647703 L 160.39033581181715 363.8925054412262 L 164.98993313730955 357.8795284832372 L 169.58953046280195 363.69754442881595 L 174.18912778829431 367.0721071160168 L 178.7887251137867 356.9883364513949 L 183.38832243927908 347.11425760939903 L 187.98791976477148 343.1903181556519 L 192.58751709026387 340.46338062558135 L 197.18711441575624 328.72599344801444 L 201.7867117412486 302.3880425552496 L 206.38630906674095 293.0424332265391 L 210.98590639223335 305.40185930721685 L 215.58550371772574 332.98291198707494 L 220.1851010432181 306.1474516509526 L 224.7846983687105 328.98658140813075 L 229.38429569420288 311.9063985354938 L 233.98389301969527 300.4223148550607 L 238.58349034518764 304.89177005586697 L 243.18308767068004 294.6933674908644 L 247.78268499617243 305.53931910711293 L 252.3822823216648 288.9140795735637 L 256.9818796471572 295.34208030423804 L 261.58147697264957 285.16609872449595 L 266.18107429814194 271.1512226959483 L 270.7806716236343 272.12325552406656 L 275.38026894912673 239.38578851461097 L 279.9798662746191 231.9846923098543 L 284.57946360011147 220.51199944227363 L 289.1790609256039 226.25814985423378 L 293.77865825109626 226.34888735082578 L 298.37825557658863 207.27101882356885 L 302.97785290208105 217.50020379083847 L 307.5774502275734 245.60102176007211 L 312.1770475530658 249.44292602192195 L 316.7766448785582 260.7817901296638 L 321.3762422040506 255.57530349110402 L 325.97583952954295 247.62345914636654 L 330.5754368550353 257.02595262579234 L 335.17503418052775 260.6876404940279 L 339.7746315060201 272.42599834246033 L 344.3742288315125 283.3982781141295 L 348.97382615700485 279.6582404055625 L 353.5734234824972 270.45975965586285 L 358.1730208079896 267.2548890203009 L 362.7726181334819 253.66972968057473 L 367.3722154589744 239.60133155018622 L 371.9718127844667 239.90770978676753 L 376.57141010995906 246.69166728143193 L 381.1710074354515 258.72753303286197 L 385.77060476094385 274.8413241416654 L 390.3702020864362 272.27081724306936 L 394.9697994119286 274.61549675573735 L 399.569396737421 245.15855057222734 L 404.1689940629134 242.82397440324957 L 408.76859138840575 261.24641403841355 L 413.3681887138982 241.28513610037388 L 417.96778603939055 269.7143735967044 L 422.5673833648829 287.29798129237 L 427.1669806903753 281.6935306537181 L 431.7665780158677 281.2158662933261 L 436.3661753413601 263.2953317104425 L 440.96577266685244 282.261661986534 L 445.56536999234487 297.78531158346476 L 450.16496731783724 305.12840768765227 L 454.7645646433296 310.06802199817156 L 459.364161968822 328.712205948576 L 463.9637592943144 325.196998325626 L 468.56335661980677 332.5539581057958 L 473.16295394529914 351.83942529841215 L 477.76255127079156 363.3119250375934 L 482.36214859628393 347.6686444748514 L 486.9617459217763 352.8392409167292 L 491.56134324726867 354.3453209376954 L 496.1609405727611 341.6182587878501 L 500.76053789825346 337.03271994253396 L 505.36013522374583 350.60514883160675" style="stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:2.0"></path></g><g class="toyplot-Series"><path d="M 50.0 354.0492689519482 L 54.59959732549238 361.773572381557 L 59.19919465098476 358.9684185936348 L 63.79879197647714 366.03495930000844 L 68.39838930196953 351.02478640478773 L 72.99798662746191 361.07312677495736 L 77.5975839529543 367.50507431066967 L 82.19718127844668 365.853435057874 L 86.79677860393906 339.28205885170655 L 91.39637592943143 327.9263185536471 L 95.99597325492383 320.29566928201024 L 100.5955705804162 327.0228911708947 L 105.19516790590859 312.19821937000114 L 109.79476523140096 282.9568344916053 L 114.39436255689336 262.4949406972464 L 118.99395988238572 248.0570199417397 L 123.59355720787812 237.22681079220558 L 128.1931545333705 245.70361131008457 L 132.79275185886289 239.0597300908775 L 137.39234918435525 229.04549839724237 L 141.99194650984765 232.11691013178165 L 146.59154383534002 205.35887600079386 L 151.1911411608324 199.10883564830323 L 155.79073848632478 186.35998985707465 L 160.39033581181715 182.61483316997763 L 164.98993313730955 210.105798396128 L 169.58953046280195 214.68468862589557 L 174.18912778829431 215.1875464701919 L 178.7887251137867 199.24566711020435 L 183.38832243927908 195.21933574315332 L 187.98791976477148 192.8996883799532 L 192.58751709026387 188.1704068004819 L 197.18711441575624 189.62176866411457 L 201.7867117412486 198.97871062638708 L 206.38630906674095 215.2087926752603 L 210.98590639223335 211.15070320848463 L 215.58550371772574 202.59866649117504 L 220.1851010432181 164.4666506043478 L 224.7846983687105 158.37758375662938 L 229.38429569420288 148.64093826200127 L 233.98389301969527 151.7005276221945 L 238.58349034518764 144.24061794047694 L 243.18308767068004 131.8671520405445 L 247.78268499617243 145.44078596124783 L 252.3822823216648 163.62773092043105 L 256.9818796471572 147.31268975155993 L 261.58147697264957 130.6179082041199 L 266.18107429814194 124.6366304198452 L 270.7806716236343 135.8986264733813 L 275.38026894912673 131.22224990972393 L 279.9798662746191 105.2872334572967 L 284.57946360011147 127.8136613251782 L 289.1790609256039 146.20429278504744 L 293.77865825109626 143.8086294809625 L 298.37825557658863 143.0800989327024 L 302.97785290208105 159.5993896323587 L 307.5774502275734 170.28945274822894 L 312.1770475530658 162.10536930195525 L 316.7766448785582 168.25836273296486 L 321.3762422040506 178.26538943680865 L 325.97583952954295 156.86202453739085 L 330.5754368550353 153.40020921577093 L 335.17503418052775 148.4808099851764 L 339.7746315060201 136.06051185732977 L 344.3742288315125 131.33005679216228 L 348.97382615700485 116.06365804749782 L 353.5734234824972 110.46445470376295 L 358.1730208079896 84.12453398192578 L 362.7726181334819 90.02966948204522 L 367.3722154589744 84.09849176666091 L 371.9718127844667 83.10167037624618 L 376.57141010995906 91.3712405465333 L 381.1710074354515 95.01234421556377 L 385.77060476094385 104.12797561793714 L 390.3702020864362 101.04652769474927 L 394.9697994119286 87.04080360478534 L 399.569396737421 86.0447007798958 L 404.1689940629134 77.86257246764862 L 408.76859138840575 72.39086305647331 L 413.3681887138982 75.44801184748097 L 417.96778603939055 81.4172577728095 L 422.5673833648829 85.81388432415733 L 427.1669806903753 117.62625785030562 L 431.7665780158677 96.06529751379102 L 436.3661753413601 94.53282403135667 L 440.96577266685244 97.70986427605777 L 445.56536999234487 114.18316474916836 L 450.16496731783724 89.275648001398 L 454.7645646433296 93.40222025070301 L 459.364161968822 94.1443196547635 L 463.9637592943144 88.23239556274584 L 468.56335661980677 76.40491561942504 L 473.16295394529914 84.99376521166703 L 477.76255127079156 69.98941748744542 L 482.36214859628393 68.87981497773062 L 486.9617459217763 50.0 L 491.56134324726867 50.007313642783224 L 496.1609405727611 54.262642759371886 L 500.76053789825346 74.63529751342996 L 505.36013522374583 78.28470656591847" style="stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0;stroke-width:2.0"></path></g><g class="toyplot-Series"><path d="M 50.0 342.5764001289674 L 54.59959732549238 332.2621292309892 L 59.19919465098476 334.53263418525466 L 63.79879197647714 298.1088330652886 L 68.39838930196953 321.03996115252613 L 72.99798662746191 321.64212273171904 L 77.5975839529543 301.5697517084814 L 82.19718127844668 292.85936314403295 L 86.79677860393906 289.87399349524634 L 91.39637592943143 312.9347873397237 L 95.99597325492383 308.3464775413839 L 100.5955705804162 315.0217052481085 L 105.19516790590859 312.0186442004259 L 109.79476523140096 298.0223371004952 L 114.39436255689336 297.68827592599666 L 118.99395988238572 300.9074854887883 L 123.59355720787812 287.70225099678714 L 128.1931545333705 287.8546560601101 L 132.79275185886289 297.0837297052662 L 137.39234918435525 310.2663444163507 L 141.99194650984765 296.09149341996823 L 146.59154383534002 282.4646008225201 L 151.1911411608324 272.1133561921591 L 155.79073848632478 269.6283910536704 L 160.39033581181715 279.8874516080013 L 164.98993313730955 283.8446572874071 L 169.58953046280195 257.3001100695952 L 174.18912778829431 254.50952578191934 L 178.7887251137867 243.53745968995972 L 183.38832243927908 248.59228114571314 L 187.98791976477148 245.45275082543336 L 192.58751709026387 241.055365784994 L 197.18711441575624 239.45746776459742 L 201.7867117412486 239.28106441890114 L 206.38630906674095 240.91810850911702 L 210.98590639223335 236.62262234933547 L 215.58550371772574 217.20325428614103 L 220.1851010432181 216.83005577941069 L 224.7846983687105 214.37186306205686 L 229.38429569420288 207.80697676619792 L 233.98389301969527 203.54454510699478 L 238.58349034518764 195.20140558024374 L 243.18308767068004 186.5950140573955 L 247.78268499617243 188.2794496554402 L 252.3822823216648 202.12060264793837 L 256.9818796471572 202.09974003456523 L 261.58147697264957 212.87717649124423 L 266.18107429814194 206.57433192064997 L 270.7806716236343 200.13014398724283 L 275.38026894912673 212.74292386393267 L 279.9798662746191 217.86306230055902 L 284.57946360011147 196.87750217159729 L 289.1790609256039 201.08061185079953 L 293.77865825109626 206.61291164073458 L 298.37825557658863 224.06691057288282 L 302.97785290208105 223.9501846282584 L 307.5774502275734 212.14611391291473 L 312.1770475530658 183.04003298944554 L 316.7766448785582 164.97668964008102 L 321.3762422040506 160.63560657832872 L 325.97583952954295 146.3638971740523 L 330.5754368550353 131.0685941762073 L 335.17503418052775 125.77328030153625 L 339.7746315060201 127.77992905412417 L 344.3742288315125 93.4746832556086 L 348.97382615700485 74.02472078881156 L 353.5734234824972 88.99380236034472 L 358.1730208079896 105.50055506666901 L 362.7726181334819 96.58548705862792 L 367.3722154589744 110.54491563607422 L 371.9718127844667 118.15116570997353 L 376.57141010995906 116.09085065598636 L 381.1710074354515 134.88110977655626 L 385.77060476094385 131.34798338220256 L 390.3702020864362 142.82486780622662 L 394.9697994119286 165.5155292917499 L 399.569396737421 140.54893358783238 L 404.1689940629134 157.6606780988672 L 408.76859138840575 149.4500854033253 L 413.3681887138982 158.01307158728795 L 417.96778603939055 136.0223534076573 L 422.5673833648829 136.7629682609318 L 427.1669806903753 111.00958708348054 L 431.7665780158677 114.84943132066562 L 436.3661753413601 111.55010777307584 L 440.96577266685244 117.6042047964387 L 445.56536999234487 102.93160116529373 L 450.16496731783724 125.83110214126683 L 454.7645646433296 135.39664555126348 L 459.364161968822 146.65951758458309 L 463.9637592943144 140.64407879654235 L 468.56335661980677 152.8408413098501 L 473.16295394529914 147.65727456656154 L 477.76255127079156 139.81166664742307 L 482.36214859628393 154.31891096932418 L 486.9617459217763 152.98727631108972 L 491.56134324726867 151.46965655204963 L 496.1609405727611 164.7165323998255 L 500.76053789825346 167.2687730159564 L 505.36013522374583 140.40713914140326" style="stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0;stroke-width:2.0"></path></g><g class="toyplot-Series"><path d="M 50.0 352.7899333057595 L 54.59959732549238 364.63171485392746 L 59.19919465098476 359.13195770322034 L 63.79879197647714 375.6657380480258 L 68.39838930196953 377.6371181937034 L 72.99798662746191 383.2396017185636 L 77.5975839529543 369.1538946413516 L 82.19718127844668 349.65795838647 L 86.79677860393906 334.24014665110207 L 91.39637592943143 327.6161202308019 L 95.99597325492383 339.96976533170925 L 100.5955705804162 322.4122115709145 L 105.19516790590859 314.9192005775065 L 109.79476523140096 322.79806906651567 L 114.39436255689336 331.6642140076002 L 118.99395988238572 334.2455521740776 L 123.59355720787812 325.63218116478924 L 128.1931545333705 320.17359962245376 L 132.79275185886289 344.0996851006974 L 137.39234918435525 355.7557169268957 L 141.99194650984765 365.2218700818857 L 146.59154383534002 366.00955431635987 L 151.1911411608324 361.60828991693353 L 155.79073848632478 357.7142483586908 L 160.39033581181715 360.5579606825247 L 164.98993313730955 364.11446523100574 L 169.58953046280195 357.35887363396256 L 174.18912778829431 357.48804675771305 L 178.7887251137867 363.1799085249946 L 183.38832243927908 357.7651499061129 L 187.98791976477148 371.0113911872914 L 192.58751709026387 374.4892465575188 L 197.18711441575624 354.75576804573757 L 201.7867117412486 371.01354747536936 L 206.38630906674095 391.4784416871073 L 210.98590639223335 369.69567369724973 L 215.58550371772574 377.0590080176646 L 220.1851010432181 378.6891066773589 L 224.7846983687105 355.34480224433526 L 229.38429569420288 361.9959120896104 L 233.98389301969527 370.5893489754621 L 238.58349034518764 361.78133975917825 L 243.18308767068004 364.04715105339176 L 247.78268499617243 358.8768662592791 L 252.3822823216648 363.3944809904751 L 256.9818796471572 373.3117407620725 L 261.58147697264957 369.02622618522605 L 266.18107429814194 364.5619579782542 L 270.7806716236343 380.4122269783731 L 275.38026894912673 389.54529550362156 L 279.9798662746191 412.37669318095203 L 284.57946360011147 408.0176833027019 L 289.1790609256039 405.9969807911671 L 293.77865825109626 410.23984178398695 L 298.37825557658863 417.5336610473877 L 302.97785290208105 416.5045313072885 L 307.5774502275734 423.58255019218933 L 312.1770475530658 407.9225281108139 L 316.7766448785582 423.6154619514603 L 321.3762422040506 441.0929408557677 L 325.97583952954295 412.29333384403793 L 330.5754368550353 431.79960073063165 L 335.17503418052775 446.7192475190724 L 339.7746315060201 440.3627486588739 L 344.3742288315125 434.0828778269395 L 348.97382615700485 423.68100232949433 L 353.5734234824972 419.4566401396645 L 358.1730208079896 422.0689942586304 L 362.7726181334819 428.1843876915976 L 367.3722154589744 436.96755542279425 L 371.9718127844667 417.5267364109009 L 376.57141010995906 420.7306728709233 L 381.1710074354515 413.27636425966637 L 385.77060476094385 386.1582659423614 L 390.3702020864362 389.25300446602716 L 394.9697994119286 388.07691407190634 L 399.569396737421 381.35733220819543 L 404.1689940629134 399.79222598038695 L 408.76859138840575 393.01642142245515 L 413.3681887138982 385.3532837929311 L 417.96778603939055 400.3153588618919 L 422.5673833648829 418.34130187570173 L 427.1669806903753 424.3830407763764 L 431.7665780158677 429.3060439591145 L 436.3661753413601 451.9279120851416 L 440.96577266685244 451.6509301491086 L 445.56536999234487 461.35439751946626 L 450.16496731783724 459.32325948901286 L 454.7645646433296 468.30827761016764 L 459.364161968822 497.79809628525146 L 463.9637592943144 487.2859486427053 L 468.56335661980677 474.1818981189988 L 473.16295394529914 481.14591966936666 L 477.76255127079156 501.0962696731397 L 482.36214859628393 500.61219103875305 L 486.9617459217763 503.2780675827328 L 491.56134324726867 504.8409635023288 L 496.1609405727611 502.5492028758945 L 500.76053789825346 529.9908755052037 L 505.36013522374583 542.9022082018927" style="stroke:rgb(65.1%,84.7%,32.9%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g><g class="toyplot-mark-Text" id="t13943d847dc84812845eba54443f74a6"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(505.36013522374583,235.05574858979216)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="5.0" y="3.066">Series 0</text></g></g></g><g class="toyplot-mark-Text" id="td8e0fb5890e543dcad380cc9ee29b8f3"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(505.36013522374583,350.60514883160675)"><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="5.0" y="3.066">Series 1</text></g></g></g><g class="toyplot-mark-Text" id="t26a1447a433445e7a5e2b6bf3ccc84b2"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(505.36013522374583,78.28470656591847)"><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="5.0" y="3.066">Series 2</text></g></g></g><g class="toyplot-mark-Text" id="t623f8681193247b086446cc776546292"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(505.36013522374583,140.40713914140326)"><text style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="5.0" y="3.066">Series 3</text></g></g></g><g class="toyplot-mark-Text" id="t39a1e6e5f9f74ca789a8cdeedc2545c9"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(505.36013522374583,542.9022082018927)"><text style="fill:rgb(65.1%,84.7%,32.9%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="5.0" y="3.066">Series 4</text></g></g></g></g><g class="toyplot-coordinates-Axis" id="td1ddfc2a78a547e78b075b4de5d33881" transform="translate(50.0,550.0)translate(0,10.0)"><line style="" x1="0" x2="455.3601352237458" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(229.9798662746191,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g><g transform="translate(459.9597325492382,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="8.555">100</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t278ffce28ec543b0a1bbe0b7d38c5a18" transform="translate(50.0,550.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="7.09779179810732" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(64.08797363935915,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-7.2250000000000005" y="-4.440892098500626e-16">-10</text></g><g transform="translate(199.6037122685794,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="-4.440892098500626e-16">0</text></g><g transform="translate(335.11945089779965,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">10</text></g><g transform="translate(470.6351895270198,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t89d610a233bc4923a99aa49f99edeb1e";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t1c0a0ea4401447d0ac9f7918763dec18";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tdb513cd0765349e98d8bdb254cf3f029","data","plot data",["x", "y0", "y1", "y2", "y3", "y4"],[[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0, 64.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 71.0, 72.0, 73.0, 74.0, 75.0, 76.0, 77.0, 78.0, 79.0, 80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0], [0.5214351637324931, -0.6195405309739713, 0.8631664374521261, 0.6005145413604132, -0.07007419200459841, 0.8670887483031402, 1.7766771620205568, 1.190153657603208, 1.255850029717637, -0.9368349244677687, 0.2632008002520494, 1.3051468225947271, 2.3084709507071572, 0.3372161305121868, 0.05313876470408979, 0.10525712938757628, 0.5607105409577673, 0.8998024819378025, 2.2709606740671884, 0.7740551208379483, 0.6214087962087664, 0.015439452069832549, 0.2588608285401908, 0.8622997394969327, 2.2304512936770697, 1.8111460089711702, 2.536700094093551, 0.7696728675033542, 0.6365643273243555, 1.745533514895506, 1.3976932866955147, 1.785130940309487, 2.882709513202209, 3.978647768829874, 4.892365060514713, 4.820273485667039, 4.994986439435255, 4.722191633826959, 5.613866346823101, 8.054826862286134, 8.18102645012337, 7.664580519658414, 7.750722456342487, 5.725744855652458, 6.023537055401005, 5.176380270961306, 5.0895854376999585, 5.157874629049178, 5.963288611447313, 6.228557192416756, 7.119565987348147, 5.723755910303841, 4.371782628802997, 4.320864428854083, 3.822621979667228, 3.728002471297844, 4.132022803497081, 4.146509778218941, 4.762248084281536, 6.3579068889070935, 5.433670555139778, 5.413325678035675, 5.77129453325171, 5.61279577014583, 6.696596502701329, 4.346142868889033, 6.426746489727833, 5.334115200705069, 5.59599858748277, 6.350719211799879, 5.615284000036682, 6.12734373719873, 6.881571962660905, 7.455079930554715, 6.5788256170244885, 8.636668567802488, 8.913631109673384, 7.8109720004224314, 8.492951446231562, 8.582464132924928, 9.096856457975823, 5.583339797351088, 6.954445412821293, 7.157075965025828, 7.371605507958226, 6.991509817081739, 7.80887855283415, 8.843798394744047, 9.16463424357085, 10.606620437017257, 10.736462750025886, 10.386498169329364, 9.408647610647458, 8.87392939938667, 9.740523325934511, 9.708576274107847, 9.413810259853202, 9.992098405150596, 8.973109621670464, 8.511228312543649], [0.3412053597430635, 0.9577390560966359, 1.511330815207839, 1.8466264999896962, 2.380914612739446, 3.7943961251655915, 3.0632908415401996, 2.645273175202714, 3.919847530328888, 2.6887392551848457, 3.6142147594591703, 1.9534994354296413, 1.5527343322933669, 2.351898138212432, 2.1979652721111806, 2.0657898604454465, 2.796445864826903, 1.0279468744352886, 1.1250185097609997, 1.569862719088204, 1.3714306647073573, 0.8037240167103407, 0.17084002026100675, 0.6570976246019236, -0.9959151495113143, -0.5522045503726491, -0.9815285539481464, -1.2305448469142268, -0.4864415592354625, 0.24218811447439403, 0.5317441094782909, 0.7329707387727407, 1.5990979721327816, 3.5426324397289823, 4.232265202922685, 3.3202363710174936, 1.2849707288973837, 3.2652174963629594, 1.5798686218925668, 2.8402523267970814, 3.687687746224955, 3.357876962177576, 4.1104391861791765, 3.3100929145240614, 4.53690536462899, 4.062569261996534, 4.813476992912138, 5.847665063634553, 5.775936654967732, 8.19170528380777, 8.737848210055365, 9.584443076720317, 9.160422186594632, 9.153726470103702, 10.56152372821076, 9.806690004044057, 7.733069754951127, 7.449567314517879, 6.612847962032501, 6.99704589293151, 7.58382971783426, 6.8899993498980585, 6.6197954676571795, 5.753596606390639, 4.943928306408898, 5.219913793142653, 5.8986896196809475, 6.135183968454022, 7.137662313563144, 8.175799896156454, 8.153191582193777, 7.652588658630358, 6.764436044537254, 5.5753644819424615, 5.7650477559737565, 5.592028774091281, 7.765720662684833, 7.937994096943662, 6.578562357020893, 8.051548309793136, 5.9536932721495255, 4.656160758691771, 5.0697253154984185, 5.104973203693824, 6.4273682822400335, 5.027801673376646, 3.8822779317096754, 3.3404149585624263, 2.9759101150302367, 1.6001153815922153, 1.8595101691281393, 1.3166241652892139, -0.10649224817643343, -0.9530728634783044, 0.20127870638200818, -0.1802708091340366, -0.29140771737809545, 0.6477497766947783, 0.9861266244100437, -0.015412313159994362], [-0.2695613998402315, -0.8395544875614336, -0.6325561111147446, -1.1540114621945339, -0.04637827898991964, -0.7878670884678051, -1.2624944343962752, -1.1406163950259065, 0.8201430322512764, 1.6581077153888908, 2.221189859855883, 1.724773579582289, 2.818718235077612, 4.976503387870983, 6.486430869456276, 7.551836327268797, 8.351020928192995, 7.725499449756306, 8.215765841425036, 8.954737697751979, 8.72809157047499, 10.70262489049028, 11.163828911197506, 12.104593867370623, 12.38095709462233, 10.352339200920154, 10.014452968952979, 9.97734599898898, 11.153731821126254, 11.45084353728399, 11.622015342615532, 11.970999278157578, 11.863900141310927, 11.173431118530209, 9.975778195478975, 10.275233410631424, 10.90630673125203, 13.720150811101597, 14.169476248081173, 14.887964417286979, 14.662190688630673, 15.212673588785046, 16.12573844937567, 15.124110589910458, 13.782056512417372, 14.985978753029597, 16.21792285902883, 16.65929430745076, 15.828247215249192, 16.173327175035432, 18.087128237167935, 16.42485431269668, 15.067769766953456, 15.244550953280427, 15.298310801075923, 14.07931654500253, 13.29047362358224, 13.89439487502196, 13.440352156939998, 12.701911972422119, 14.28131264690605, 14.53676750083203, 14.89978062981289, 15.81630134198119, 16.165371871575566, 17.29191251542169, 17.70508986296614, 19.648769688517984, 19.213016944235175, 19.650691400012775, 19.72424901040533, 19.11401950836105, 18.845334578783035, 18.172672385108662, 18.40005910449326, 19.433571833836425, 19.50707641972182, 20.110853397585185, 20.514622691581824, 20.28902905781414, 19.84854546633546, 19.52410886614268, 17.176604890003862, 18.7676348732818, 18.880719412239106, 18.64627872831281, 17.4306781907116, 19.26865782316735, 18.964149115097975, 18.90938799203087, 19.34564168121992, 20.218417054985295, 19.584627232554286, 20.691830563768416, 20.773710537337447, 22.166892994866387, 22.166353305317614, 21.852343349010503, 20.349001009579442, 20.07970320775928], [0.5770464509549642, 1.338158850319787, 1.1706133698293109, 3.8584045805331746, 2.1662669499382092, 2.121832142196765, 3.603015894451329, 4.245774341001998, 4.466071236328286, 2.7643652885362617, 3.1029466108794694, 2.61036709397269, 2.8319694759586853, 3.86478730520179, 3.889438403139021, 3.651885953854913, 4.626328821198279, 4.615082521331964, 3.934049178746758, 2.9612754740516154, 4.007268444297368, 5.0128263769248225, 5.7766671481198655, 5.960038110313987, 5.202999801841174, 4.910989019961959, 6.869768678053146, 7.075691939506273, 7.885344471599235, 7.512338243179987, 7.7440109885036685, 8.068503559250072, 8.186415916630828, 8.19943310175491, 8.078632071057287, 8.395605302597154, 9.82860255145008, 9.856141677938654, 10.03753704516457, 10.521974230266801, 10.8365082985838, 11.452166642857625, 12.087250922359349, 11.962952769607261, 10.941584098152171, 10.943123595599788, 10.147833206033544, 10.612933764415125, 11.088464355812983, 10.157739998312397, 9.779913888340378, 11.328483843478915, 11.018327272609888, 10.610086883272395, 9.322118481321425, 9.330731941706553, 10.201779897814468, 12.34958067858616, 13.682513925460682, 14.002851851200054, 15.055992213244986, 16.18466576456539, 16.575418449695157, 16.42734349007159, 18.958801912947244, 20.39405678913645, 19.28945582374678, 18.0713867733697, 18.72924895957918, 17.699152476421588, 17.137870801625827, 17.289905913918158, 15.90333197714604, 16.164049029651697, 15.317144858954185, 13.642751779962351, 15.485090976609294, 14.222378270017064, 14.828255696402689, 14.196374390911558, 15.819117136667362, 15.764465561819597, 17.664863363429497, 17.381512936680096, 17.624977170499967, 17.178232232635057, 18.260955448370918, 16.57115165084836, 15.865289475225453, 15.034177742577517, 15.478070005490192, 14.578044470693909, 14.960551092856159, 15.539495501712207, 14.468974507719482, 14.56723871464514, 14.679227165166918, 13.70171149194905, 13.513376126481724, 15.49555429606307], [-0.17663229367683592, -1.050463013853759, -0.6446240163809387, -1.8646874947672272, -2.010159907463986, -2.4235793066814493, -1.3841644593955986, 0.0544829222361185, 1.1921966587602597, 1.6809979217946505, 0.7693956809134145, 2.0650056180612606, 2.617931135731893, 2.036532357353374, 1.3822803102651138, 1.1917977735067715, 1.8273970844366292, 2.2301976445450356, 0.46463995211294984, -0.39548389358219205, -1.0940118469212514, -1.1521367734015144, -0.8273579363493466, -0.5400081718399214, -0.74985186620331, -1.0122940433597098, -0.5137843008473031, -0.5233162655517036, -0.9433310789494903, -0.5437643073218248, -1.5212331544954376, -1.7778716383650484, -0.3216954988707805, -1.5213922716651334, -3.031541160550366, -1.4241435099013435, -1.9674999048778317, -2.087788417207332, -0.3651616087526257, -0.8559614164025009, -1.4900897451690853, -0.8401276591870923, -1.0073267843317304, -0.6258002659795775, -0.9591648461304054, -1.6909809342035165, -1.37474352737568, -1.0453155028429428, -2.214941198016713, -2.8888901147722175, -4.573668422316152, -4.252007637942128, -4.102895620993038, -4.415985527430296, -4.954212255718815, -4.878270542194683, -5.4005728929398416, -4.24498593014268, -5.403001522972327, -6.692702562947243, -4.567517156215461, -6.006926857546471, -7.107879923172435, -6.638820098498469, -6.175414822073972, -5.407837889485689, -5.096113049805784, -5.2888843209061465, -5.740152453657814, -6.388281432626669, -4.953701271787595, -5.19012668572335, -4.640057100695124, -2.638953864155063, -2.8673213257480716, -2.780535067117361, -2.2846825608563597, -3.645033318537029, -3.145032017841554, -2.5795524870476556, -3.683636427430258, -5.013809822502097, -5.4596428277152595, -5.822921900134131, -7.49223856806168, -7.471799470814765, -8.187839354337594, -8.037957277834966, -8.70098123446471, -10.877098855442297, -10.101384702320342, -9.134408419251107, -9.648298659662363, -11.120478216485534, -11.084757005113095, -11.28147781193198, -11.39680728844926, -11.227693305850918, -13.252673792020966, -14.205429009037882]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"td1ddfc2a78a547e78b075b4de5d33881",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 108.70516799999999, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t278ffce28ec543b0a1bbe0b7d38c5a18",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 22.166892994866387, "min": -14.729190445894108}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Note that we are using the last point in each series as the anchor for
the corresponding label - by default, Toyplot renders text centered on
its anchor, so in this case we've chosen a text style that left-aligns
the text and offsets it slightly to avoid overlapping the data.

Canvas Text
-----------

When adding text to axes, you specify the text coordinates using the
same domain as your data. Naturally, this limits the added text to the
bounds defined by the axes. For the ultimate in labeling flexibility,
you can add text to the canvas directly, using canvas units, outside
and/or overlapping coordinate systems:

.. code:: python

    label_style={"font-size":"18px", "font-weight":"bold"}
    
    canvas = toyplot.Canvas(width=600, height=300)
    canvas.cartesian(grid=(1,2,0)).plot(numpy.linspace(1, 0)**2)
    canvas.cartesian(grid=(1,2,1), yshow=False).plot(numpy.linspace(0, 1)**2)
    canvas.text(300, 120, "This label overlaps two sets of axes!", style=label_style);



.. raw:: html

    <div class="toyplot" id="t23109b5430d1442996e84534440f6c48" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="te6db9e2027d94d298527041fa495f1be" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t1c4a33ebb0ab4f5faba4e468733861f7"><clipPath id="tfb9a3b00eac348d6b7095994ea380b9d"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tfb9a3b00eac348d6b7095994ea380b9d)"><g class="toyplot-mark-Plot" id="t519beb31695148af8d86142f1c22a05f" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 50.0 L 54.0 58.079966680549774 L 58.0 65.99333610995419 L 62.0 73.74010828821322 L 66.0 81.32028321532694 L 70.0 88.7338608912953 L 74.0 95.9808413161183 L 78.0 103.0612244897959 L 82.0 109.97501041232817 L 86.0 116.72219908371511 L 90.0 123.30279050395669 L 94.0 129.7167846730529 L 98.0 135.96418159100375 L 102.0 142.04498125780924 L 106.0 147.9591836734694 L 110.0 153.70678883798413 L 114.0 159.2877967513536 L 118.0 164.70220741357767 L 122.0 169.9500208246564 L 126.0 175.03123698458975 L 130.0 179.94585589337777 L 134.0 184.69387755102045 L 138.0 189.27530195751768 L 142.0 193.69012911286964 L 146.0 197.9383590170762 L 150.0 202.01999167013744 L 154.0 205.9350270720533 L 158.0 209.68346522282383 L 162.0 213.265306122449 L 166.0 216.68054977092876 L 170.0 219.92919616826322 L 174.0 223.0112453144523 L 178.0 225.926697209496 L 182.0 228.6755518533944 L 186.0 231.25780924614742 L 190.0 233.6734693877551 L 194.0 235.9225322782174 L 198.0 238.00499791753435 L 202.0 239.92086630570594 L 206.0 241.67013744273217 L 210.0 243.25281132861306 L 214.0 244.6688879633486 L 218.0 245.91836734693877 L 222.0 247.00124947938357 L 226.0 247.91753436068305 L 230.0 248.66722199083716 L 234.0 249.2503123698459 L 238.0 249.66680549770925 L 242.0 249.9167013744273 L 246.0 250.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="t54ac6c79304d473b91f063b4d7881eff" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="196.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(40.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(80.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g><g transform="translate(120.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">30</text></g><g transform="translate(160.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">40</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="te00131137f574b818cd66da8da63a887" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t519c7a7bdafa459989500e457263a3b1"><clipPath id="tdb4bbed6a80a4dbe92bfea664d8ecef6"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#tdb4bbed6a80a4dbe92bfea664d8ecef6)"><g class="toyplot-mark-Plot" id="t5fa7b65db4e746d7a61eb405c9a13892" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 250.0 L 354.0 249.9167013744273 L 358.0 249.66680549770928 L 362.0 249.2503123698459 L 366.0 248.66722199083716 L 370.0 247.91753436068305 L 374.0 247.0012494793836 L 378.0 245.91836734693877 L 382.0 244.6688879633486 L 386.0 243.25281132861306 L 390.0 241.6701374427322 L 394.0 239.92086630570594 L 398.0 238.00499791753435 L 402.0 235.92253227821743 L 406.0 233.67346938775512 L 410.0 231.25780924614745 L 414.0 228.67555185339444 L 418.0 225.92669720949604 L 422.0 223.0112453144523 L 426.0 219.92919616826322 L 430.0 216.6805497709288 L 434.0 213.26530612244898 L 438.0 209.68346522282383 L 442.0 205.93502707205332 L 446.0 202.01999167013744 L 450.0 197.9383590170762 L 454.0 193.69012911286964 L 458.0 189.2753019575177 L 462.0 184.69387755102045 L 466.0 179.94585589337777 L 470.0 175.03123698458978 L 474.0 169.9500208246564 L 478.0 164.7022074135777 L 482.0 159.2877967513536 L 486.0 153.70678883798416 L 490.0 147.9591836734694 L 494.0 142.04498125780927 L 498.0 135.96418159100375 L 502.0 129.7167846730529 L 506.0 123.30279050395671 L 510.0 116.72219908371514 L 514.0 109.97501041232822 L 518.0 103.06122448979593 L 522.0 95.9808413161183 L 526.0 88.73386089129534 L 530.0 81.32028321532698 L 534.0 73.74010828821326 L 538.0 65.99333610995419 L 542.0 58.079966680549774 L 546.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="t619d2da60a0d4b40a895bb9de7755dc3" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="196.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(40.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(80.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g><g transform="translate(120.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">30</text></g><g transform="translate(160.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">40</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-mark-Text" id="t7848d5babc684da3a5320fc758abf180"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,120.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:18.0px;font-weight:bold;opacity:1;stroke:none;vertical-align:baseline;white-space:pre" x="-156.06" y="4.599">This label overlaps two sets of axes!</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t23109b5430d1442996e84534440f6c48";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "te6db9e2027d94d298527041fa495f1be";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t519beb31695148af8d86142f1c22a05f","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [1.0, 0.9596001665972511, 0.920033319450229, 0.8812994585589339, 0.8433985839233653, 0.8063306955435235, 0.7700957934194085, 0.7346938775510206, 0.7001249479383591, 0.6663890045814245, 0.6334860474802165, 0.6014160766347355, 0.5701790920449812, 0.5397750937109538, 0.5102040816326531, 0.4814660558100793, 0.4535610162432321, 0.4264889629321117, 0.40024989587671805, 0.3748438150770512, 0.3502707205331112, 0.32653061224489793, 0.3036234902124116, 0.2815493544356518, 0.2603082049146189, 0.23990004164931278, 0.22032486463973353, 0.20158267388588094, 0.18367346938775514, 0.16659725114535612, 0.15035401915868396, 0.1349437734277385, 0.12036651395251982, 0.10662224073302792, 0.0937109537692628, 0.08163265306122454, 0.070387338608913, 0.05997501041232822, 0.050395668471470235, 0.04164931278633907, 0.033735943356934646, 0.026655560183256998, 0.020408163265306135, 0.014993752603082056, 0.01041232819658478, 0.006663890045814259, 0.0037484381507705204, 0.0016659725114535648, 0.0004164931278633912, 0.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t54ac6c79304d473b91f063b4d7881eff",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"te00131137f574b818cd66da8da63a887",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t5fa7b65db4e746d7a61eb405c9a13892","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t619d2da60a0d4b40a895bb9de7755dc3",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


... remember when placing labels directly on the canvas that, unlike
Cartesian coordinates, canvas coordinates increase from top-to-bottom.

Coordinate System Color Scales
------------------------------

Since we often use color in visualization to add an additional dimension
to our plots, we need a way to help viewers map between colors and
values. For this case, Toyplot allows a color scale to be added to a set
of :ref:`cartesian-coordinates`:

.. code:: python

    data = toyplot.data.cars()
    
    colormap = toyplot.color.brewer.map(
        name="BlueGreenBrown",
        reverse=True,
        domain_min = data["MPG"].min(),
        domain_max = data["MPG"].max(),
    )
    canvas = toyplot.Canvas(width=600, height=400)
    axes = canvas.cartesian(xlabel="Year", ylabel="Horsepower", margin=75)
    axes.scatterplot(
        data["Year"],
        data["Horsepower"],
        color=(data["MPG"], colormap),
        size=8,
        mstyle={"stroke":"black", "stroke-opacity":0.3}
    )
    axes.color_scale(colormap, label="MPG");



.. raw:: html

    <div class="toyplot" id="t2d21e3d402fd45668fb81795cacfb872" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="tde58afcb17b64ebdb86475aa796f7fe0" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 400.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t5e605f50c44d46e8b9e6b78cecb972c7"><clipPath id="t1887a778bfbc4b2fbcc37a2321d2d0a7"><rect height="270.0" width="470.0" x="65.0" y="65.0"></rect></clipPath><g clip-path="url(#t1887a778bfbc4b2fbcc37a2321d2d0a7)"><g class="toyplot-mark-Point" id="t7d2d774d046c4e9c9c66b9d9a60e8263"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 222.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 179.16666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 209.8039215686275)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 138.72549019607843)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 111.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 117.89215686274508)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 105.63725490196079)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 148.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 173.03921568627453)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 185.2941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 105.63725490196079)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 325.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 274.7549019607843)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 242.8921568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(38.8%,22.3%,2.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 117.89215686274508)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(38.8%,22.3%,2.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 136.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 124.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(32.9%,18.8%,2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 144.8529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 252.6960784313725)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 179.16666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 166.91176470588238)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 193.87254901960785)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 160.7843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 173.03921568627453)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 166.91176470588238)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 293.1372549019608)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 275.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 295.5882352941176)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 288.235294117647)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(52.6%,81.4%,76.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 296.813725490196)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 307.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 295.5882352941176)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 283.33333333333337)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 315.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 275.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 179.16666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 166.91176470588238)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 193.87254901960785)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 126.47058823529412)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 191.42156862745097)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 185.2941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 148.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 222.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 209.8039215686275)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 244.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 288.235294117647)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 274.7549019607843)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 296.813725490196)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 275.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 268.62745098039215)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 283.33333333333337)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 166.91176470588238)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 203.67647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 213.48039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 138.72549019607843)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 187.7450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 117.89215686274508)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 105.63725490196079)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 166.91176470588238)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 252.6960784313725)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 325.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 176.71568627450978)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 173.03921568627453)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 160.7843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 293.1372549019608)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 266.17647058823525)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 250.2450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 203.67647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 99.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 321.32352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 289.4607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 269.8529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 244.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 231.8627450980392)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 160.7843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 299.264705882353)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 283.33333333333337)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 289.4607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 252.6960784313725)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 209.8039215686275)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 209.8039215686275)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 279.65686274509807)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 299.264705882353)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 285.78431372549016)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 317.6470588235294)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 306.61764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 289.4607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 289.4607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 289.4607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 267.4019607843137)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 299.264705882353)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 252.6960784313725)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 293.1372549019608)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 293.1372549019608)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 173.03921568627453)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 203.67647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 200.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 252.6960784313725)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 223.28431372549022)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 289.4607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 279.65686274509807)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 285.78431372549016)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 263.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 294.3627450980392)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 295.5882352941176)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 261.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 240.44117647058823)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 316.421568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 275.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 282.1078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 268.62745098039215)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 284.55882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 279.65686274509807)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 209.8039215686275)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 234.31372549019608)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(64.2%,40.5%,10.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 195.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 252.6960784313725)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 282.1078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.8%,84.9%,65.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 317.6470588235294)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.6%,78.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 307.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 295.5882352941176)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 316.421568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 285.78431372549016)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.9%,94.1%,93.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 294.3627450980392)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 295.5882352941176)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 289.4607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.3%,89.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 293.1372549019608)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 256.37254901960785)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 249.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 234.31372549019608)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 160.7843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 203.67647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 222.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.3%,91.8%,89.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 298.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 283.33333333333337)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 310.29411764705884)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93%,84.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 263.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 295.5882352941176)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 203.67647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 203.67647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 222.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 252.6960784313725)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 261.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 160.7843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 173.03921568627453)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 148.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 198.77450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 285.78431372549016)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.6%,78.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 289.4607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93%,84.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 272.30392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.1%,93%,91.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 304.16666666666663)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 279.65686274509807)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 299.264705882353)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.1%,93%,91.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 285.78431372549016)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.4%,38.9%,35.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 322.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.1%,76%,71.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 300.4901960784314)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(68.9%,88%,85.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 317.6470588235294)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(19%,57.6%,54.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 295.5882352941176)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.1%,76%,71.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 307.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.2%,73.5%,45.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(84.5%,70.1%,41.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 209.8039215686275)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 211.0294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 252.6960784313725)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.4%,82%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(84.5%,70.1%,41.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.2%,77.3%,51.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 252.6960784313725)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.7%,78.1%,52.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.8%,64.7%,35%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.2%,61.3%,30.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 234.31372549019608)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 203.67647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.8%,58.6%,27.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 179.16666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.2%,61.3%,30.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 211.0294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 209.8039215686275)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 298.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.7%,94.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.2%,92.5%,90.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 289.4607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.4%,79.3%,55%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94.5%,87.7%,70.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 252.6960784313725)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.9%,90%,74.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,90.4%,75.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.5%,76.2%,49.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 255.14705882352942)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 228.18627450980392)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,81.3%,58.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 240.44117647058823)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(73.2%,49%,16.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 218.38235294117646)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.3%,91.8%,89.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 294.3627450980392)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.9%,94.1%,93.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 298.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 240.44117647058823)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.8%,72.8%,45%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.3%,84.1%,63.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.2%,77.3%,51.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 222.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.5%,57.9%,26.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 223.28431372549022)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 212.2549019607843)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.5%,62%,31.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 215.9313725490196)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.2%,53.2%,20.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 191.42156862745097)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 207.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 228.18627450980392)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(75.5%,90.7%,88.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 294.3627450980392)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(59.2%,84.1%,80.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(47.2%,78.3%,73.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 283.33333333333337)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.5%,94%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 283.33333333333337)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,92.8%,83.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 287.0098039215686)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 228.18627450980392)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 294.3627450980392)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,90.4%,75.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(58.5%,83.8%,79.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 295.5882352941176)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.3%,82.9%,78.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 295.5882352941176)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.3%,91%,88.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(34.7%,69.2%,65.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 296.813725490196)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(93.2%,95.4%,95.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.3%,94.9%,94.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 240.44117647058823)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.7%,90.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 240.44117647058823)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(7.7%,46.8%,43.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 288.235294117647)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(28.5%,64.7%,61.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 307.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74%,90.1%,87.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 295.5882352941176)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(35.5%,69.8%,65.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.2%,88.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.3%,77.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.5%,68.1%,39.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(57.7%,83.5%,79.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 285.78431372549016)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,93.8%,92.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.3%,92.1%,90.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 289.4607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 268.62745098039215)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(73.3%,89.8%,87.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 289.4607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0%,23.5%,18.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.6%,96%,95.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 252.6960784313725)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(11.5%,50.4%,47.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.2%,33.6%,29.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 322.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.3%,37.5%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 322.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(41.7%,74.3%,70.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 299.264705882353)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 299.264705882353)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.2%,32.3%,28.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 299.264705882353)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,85%,81.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 299.264705882353)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,93.8%,92.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 305.3921568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.6%,88.3%,85.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 219.6078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.7%,89.6%,74%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(52.6%,81.4%,76.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(71.8%,89.2%,86.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 293.1372549019608)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 278.4313725490196)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.5%,89.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 278.4313725490196)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.4%,85.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 268.62745098039215)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.2%,88.8%,72.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 278.4313725490196)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(20.7%,59.1%,56%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 310.29411764705884)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(21.4%,59.7%,56.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 302.94117647058823)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(51.8%,81.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 307.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.6%,89.5%,87%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 299.264705882353)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(31.6%,67%,63.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 305.3921568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(59.2%,84.1%,80.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 298.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(54.8%,82.3%,78%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 304.16666666666663)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(57%,83.2%,79.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86%,93.7%,92.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 290.686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(62.2%,85.3%,81.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 289.4607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(71.8%,89.2%,86.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 289.4607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(68.1%,87.7%,84.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(77.7%,91.6%,89.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 290.686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94.6%,95.7%,95.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 283.33333333333337)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(82.2%,92.8%,91.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 288.235294117647)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,92.8%,83.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 239.21568627450978)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.5%,91.2%,77.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 234.31372549019608)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.5%,84.5%,64.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.5%,89.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 252.6960784313725)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.5%,57.9%,26.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(60%,84.4%,80.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 278.4313725490196)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 268.62745098039215)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 290.686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 298.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 298.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 304.16666666666663)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 295.5882352941176)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 273.5294117647059)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 289.4607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(60%,84.4%,80.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 295.5882352941176)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 299.264705882353)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 299.264705882353)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 299.264705882353)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 246.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 268.62745098039215)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 244.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 263.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 278.4313725490196)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 271.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 275.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.3%,34.9%,31.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 317.6470588235294)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 278.4313725490196)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 284.55882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 280.88235294117646)"><circle r="4.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="td962e798520d40d3a03c32195d21336c" transform="translate(75.0,325.0)translate(0,10.0)"><line style="" x1="0" x2="450.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">70</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">74</text></g><g transform="translate(300.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">78</text></g><g transform="translate(450.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">82</text></g></g><g transform="translate(225.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-13.008000000000001" y="10.265999999999998">Year</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tf337f74a28244a7cb9019d584c41fff2" transform="translate(75.0,325.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="225.49019607843138" y1="0" y2="0"></line><g><g transform="translate(4.901960784313726,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">50</text></g><g transform="translate(66.17647058823529,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.440892098500626e-16">100</text></g><g transform="translate(127.45098039215685,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.440892098500626e-16">150</text></g><g transform="translate(188.72549019607843,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.440892098500626e-16">200</text></g><g transform="translate(250.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.440892098500626e-16">250</text></g></g><g transform="translate(125.0,-22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-34.674" y="0.0">Horsepower</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t7932767e3527437d9042eb66893fe68a"><clipPath id="ta076ff948ebf416cb75f30903480aef4"><rect height="20.0" width="250.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#ta076ff948ebf416cb75f30903480aef4)" transform="translate(545.0,325.0)rotate(-90.0)"><g class="toyplot-color-Map" id="t6952fd7130cd478380bf068005430acb"><defs><linearGradient gradientUnits="userSpaceOnUse" id="tcf15ed96ea7e40b7867c5b8bf72a2037" x1="0.0" x2="229.26829268292684" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(32.9%,18.8%,1.96%)" stop-opacity="1.0"></stop><stop offset="0.01587301587301586" stop-color="rgb(36.4%,20.9%,2.27%)" stop-opacity="1.0"></stop><stop offset="0.03174603174603172" stop-color="rgb(39.9%,22.9%,2.58%)" stop-opacity="1.0"></stop><stop offset="0.04761904761904764" stop-color="rgb(43.4%,25%,2.89%)" stop-opacity="1.0"></stop><stop offset="0.0634920634920635" stop-color="rgb(46.9%,27%,3.21%)" stop-opacity="1.0"></stop><stop offset="0.07936507936507936" stop-color="rgb(50.4%,29.1%,3.52%)" stop-opacity="1.0"></stop><stop offset="0.09523809523809522" stop-color="rgb(53.9%,31.1%,3.83%)" stop-opacity="1.0"></stop><stop offset="0.11111111111111109" stop-color="rgb(57.1%,33.9%,5.45%)" stop-opacity="1.0"></stop><stop offset="0.126984126984127" stop-color="rgb(60.3%,36.8%,7.63%)" stop-opacity="1.0"></stop><stop offset="0.1428571428571428" stop-color="rgb(63.5%,39.8%,9.8%)" stop-opacity="1.0"></stop><stop offset="0.15873015873015872" stop-color="rgb(66.6%,42.8%,12%)" stop-opacity="1.0"></stop><stop offset="0.1746031746031746" stop-color="rgb(69.8%,45.8%,14.2%)" stop-opacity="1.0"></stop><stop offset="0.19047619047619044" stop-color="rgb(73%,48.8%,16.3%)" stop-opacity="1.0"></stop><stop offset="0.20634920634920637" stop-color="rgb(75.7%,52.2%,19.6%)" stop-opacity="1.0"></stop><stop offset="0.22222222222222218" stop-color="rgb(77.7%,56.3%,24.6%)" stop-opacity="1.0"></stop><stop offset="0.2380952380952381" stop-color="rgb(79.7%,60.3%,29.6%)" stop-opacity="1.0"></stop><stop offset="0.253968253968254" stop-color="rgb(81.7%,64.3%,34.6%)" stop-opacity="1.0"></stop><stop offset="0.2698412698412698" stop-color="rgb(83.7%,68.4%,39.6%)" stop-opacity="1.0"></stop><stop offset="0.2857142857142856" stop-color="rgb(85.7%,72.4%,44.5%)" stop-opacity="1.0"></stop><stop offset="0.3015873015873016" stop-color="rgb(87.6%,76.3%,49.5%)" stop-opacity="1.0"></stop><stop offset="0.31746031746031744" stop-color="rgb(89%,78.7%,53.8%)" stop-opacity="1.0"></stop><stop offset="0.3333333333333333" stop-color="rgb(90.5%,81%,58.2%)" stop-opacity="1.0"></stop><stop offset="0.3492063492063492" stop-color="rgb(91.9%,83.4%,62.5%)" stop-opacity="1.0"></stop><stop offset="0.36507936507936506" stop-color="rgb(93.3%,85.8%,66.9%)" stop-opacity="1.0"></stop><stop offset="0.3809523809523809" stop-color="rgb(94.8%,88.1%,71.2%)" stop-opacity="1.0"></stop><stop offset="0.3968253968253968" stop-color="rgb(96.2%,90.5%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.41269841269841273" stop-color="rgb(96.4%,91.6%,79%)" stop-opacity="1.0"></stop><stop offset="0.4285714285714285" stop-color="rgb(96.4%,92.4%,82.1%)" stop-opacity="1.0"></stop><stop offset="0.4444444444444444" stop-color="rgb(96.3%,93.2%,85.2%)" stop-opacity="1.0"></stop><stop offset="0.46031746031746024" stop-color="rgb(96.2%,94.1%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.4761904761904762" stop-color="rgb(96.2%,94.9%,91.4%)" stop-opacity="1.0"></stop><stop offset="0.49206349206349204" stop-color="rgb(96.1%,95.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.5079365079365079" stop-color="rgb(94.6%,95.7%,95.6%)" stop-opacity="1.0"></stop><stop offset="0.5238095238095238" stop-color="rgb(91.8%,95.1%,94.6%)" stop-opacity="1.0"></stop><stop offset="0.5396825396825397" stop-color="rgb(88.9%,94.4%,93.6%)" stop-opacity="1.0"></stop><stop offset="0.5555555555555555" stop-color="rgb(86.1%,93.7%,92.6%)" stop-opacity="1.0"></stop><stop offset="0.5714285714285713" stop-color="rgb(83.2%,93%,91.6%)" stop-opacity="1.0"></stop><stop offset="0.5873015873015872" stop-color="rgb(80.3%,92.3%,90.6%)" stop-opacity="1.0"></stop><stop offset="0.6031746031746031" stop-color="rgb(77.2%,91.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.6190476190476191" stop-color="rgb(72.7%,89.6%,87.1%)" stop-opacity="1.0"></stop><stop offset="0.6349206349206349" stop-color="rgb(68.3%,87.8%,84.9%)" stop-opacity="1.0"></stop><stop offset="0.6507936507936508" stop-color="rgb(63.9%,86%,82.6%)" stop-opacity="1.0"></stop><stop offset="0.6666666666666666" stop-color="rgb(59.5%,84.2%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.6825396825396826" stop-color="rgb(55.1%,82.4%,78.2%)" stop-opacity="1.0"></stop><stop offset="0.6984126984126984" stop-color="rgb(50.6%,80.6%,75.9%)" stop-opacity="1.0"></stop><stop offset="0.7142857142857143" stop-color="rgb(46%,77.4%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.7301587301587301" stop-color="rgb(41.3%,74%,69.8%)" stop-opacity="1.0"></stop><stop offset="0.7460317460317459" stop-color="rgb(36.7%,70.6%,66.7%)" stop-opacity="1.0"></stop><stop offset="0.7619047619047618" stop-color="rgb(32%,67.3%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.7777777777777777" stop-color="rgb(27.3%,63.9%,60.4%)" stop-opacity="1.0"></stop><stop offset="0.7936507936507936" stop-color="rgb(22.7%,60.6%,57.3%)" stop-opacity="1.0"></stop><stop offset="0.8095238095238094" stop-color="rgb(18.8%,57.4%,54.2%)" stop-opacity="1.0"></stop><stop offset="0.8253968253968255" stop-color="rgb(15.6%,54.3%,51.2%)" stop-opacity="1.0"></stop><stop offset="0.8412698412698413" stop-color="rgb(12.4%,51.3%,48.1%)" stop-opacity="1.0"></stop><stop offset="0.857142857142857" stop-color="rgb(9.13%,48.2%,45.1%)" stop-opacity="1.0"></stop><stop offset="0.8730158730158728" stop-color="rgb(5.89%,45.2%,42%)" stop-opacity="1.0"></stop><stop offset="0.8888888888888888" stop-color="rgb(2.66%,42.1%,39%)" stop-opacity="1.0"></stop><stop offset="0.9047619047619048" stop-color="rgb(0.373%,39.2%,36%)" stop-opacity="1.0"></stop><stop offset="0.9206349206349205" stop-color="rgb(0.311%,36.6%,33.1%)" stop-opacity="1.0"></stop><stop offset="0.9365079365079366" stop-color="rgb(0.249%,34%,30.3%)" stop-opacity="1.0"></stop><stop offset="0.9523809523809524" stop-color="rgb(0.187%,31.4%,27.4%)" stop-opacity="1.0"></stop><stop offset="0.9682539682539683" stop-color="rgb(0.124%,28.8%,24.6%)" stop-opacity="1.0"></stop><stop offset="0.9841269841269841" stop-color="rgb(0.0622%,26.1%,21.7%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(0%,23.5%,18.8%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#tcf15ed96ea7e40b7867c5b8bf72a2037);stroke:none;stroke-width:1.0" width="229.26829268292684" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="tc0f1bb9bff17498bac046b7fc3baa6a3" transform="translate(545.0,325.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="229.26829268292684" y1="0" y2="0"></line><g><g transform="translate(6.097560975609756,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(67.07317073170732,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g><g transform="translate(128.0487804878049,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">30</text></g><g transform="translate(189.02439024390245,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">40</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g></g><g transform="translate(125.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-13.668" y="10.265999999999998">MPG</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t2d21e3d402fd45668fb81795cacfb872";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tde58afcb17b64ebdb86475aa796f7fe0";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t7d2d774d046c4e9c9c66b9d9a60e8263","data","point",["x", "y0"],[[70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0], [130.0, 165.0, 150.0, 150.0, 140.0, 198.0, 220.0, 215.0, 225.0, 190.0, 170.0, 160.0, 150.0, 225.0, 95.0, 95.0, 97.0, 85.0, 88.0, 46.0, 87.0, 90.0, 95.0, 113.0, 90.0, 215.0, 200.0, 210.0, 193.0, 88.0, 90.0, 95.0, 100.0, 105.0, 100.0, 88.0, 100.0, 165.0, 175.0, 153.0, 150.0, 180.0, 170.0, 175.0, 110.0, 72.0, 100.0, 88.0, 86.0, 90.0, 70.0, 76.0, 65.0, 69.0, 60.0, 70.0, 95.0, 80.0, 54.0, 90.0, 86.0, 165.0, 175.0, 150.0, 153.0, 150.0, 208.0, 155.0, 160.0, 190.0, 97.0, 150.0, 130.0, 140.0, 150.0, 112.0, 76.0, 87.0, 69.0, 86.0, 92.0, 97.0, 80.0, 88.0, 175.0, 150.0, 145.0, 137.0, 150.0, 198.0, 150.0, 158.0, 150.0, 215.0, 225.0, 175.0, 105.0, 100.0, 100.0, 88.0, 95.0, 46.0, 150.0, 167.0, 170.0, 180.0, 100.0, 88.0, 72.0, 94.0, 90.0, 85.0, 107.0, 90.0, 145.0, 230.0, 49.0, 75.0, 91.0, 112.0, 150.0, 110.0, 122.0, 180.0, 95.0, 100.0, 100.0, 67.0, 80.0, 65.0, 75.0, 100.0, 110.0, 105.0, 140.0, 150.0, 150.0, 140.0, 150.0, 83.0, 67.0, 78.0, 52.0, 61.0, 75.0, 75.0, 75.0, 97.0, 93.0, 67.0, 95.0, 105.0, 72.0, 72.0, 170.0, 145.0, 150.0, 148.0, 110.0, 105.0, 110.0, 95.0, 110.0, 110.0, 129.0, 75.0, 83.0, 100.0, 78.0, 96.0, 71.0, 97.0, 97.0, 70.0, 90.0, 95.0, 88.0, 98.0, 115.0, 53.0, 86.0, 81.0, 92.0, 79.0, 83.0, 140.0, 150.0, 120.0, 152.0, 100.0, 105.0, 81.0, 90.0, 52.0, 60.0, 70.0, 53.0, 100.0, 78.0, 110.0, 95.0, 71.0, 70.0, 75.0, 72.0, 102.0, 150.0, 88.0, 108.0, 120.0, 180.0, 145.0, 130.0, 150.0, 68.0, 80.0, 58.0, 96.0, 70.0, 145.0, 110.0, 145.0, 130.0, 110.0, 105.0, 100.0, 98.0, 180.0, 170.0, 190.0, 149.0, 78.0, 88.0, 75.0, 89.0, 63.0, 83.0, 67.0, 78.0, 97.0, 110.0, 110.0, 48.0, 66.0, 52.0, 70.0, 60.0, 110.0, 140.0, 139.0, 105.0, 95.0, 85.0, 88.0, 100.0, 90.0, 105.0, 85.0, 110.0, 120.0, 145.0, 165.0, 139.0, 140.0, 68.0, 95.0, 97.0, 75.0, 95.0, 105.0, 85.0, 97.0, 103.0, 125.0, 115.0, 133.0, 71.0, 68.0, 115.0, 85.0, 88.0, 90.0, 110.0, 130.0, 129.0, 138.0, 135.0, 155.0, 142.0, 125.0, 150.0, 71.0, 65.0, 80.0, 80.0, 77.0, 125.0, 71.0, 90.0, 70.0, 70.0, 65.0, 69.0, 90.0, 115.0, 115.0, 90.0, 76.0, 60.0, 70.0, 65.0, 90.0, 88.0, 90.0, 90.0, 78.0, 90.0, 75.0, 92.0, 75.0, 65.0, 105.0, 65.0, 48.0, 48.0, 67.0, 67.0, 67.0, 67.0, 62.0, 132.0, 100.0, 88.0, 72.0, 84.0, 84.0, 92.0, 110.0, 84.0, 58.0, 64.0, 60.0, 67.0, 65.0, 62.0, 68.0, 63.0, 65.0, 65.0, 74.0, 75.0, 75.0, 100.0, 74.0, 80.0, 76.0, 116.0, 120.0, 110.0, 105.0, 88.0, 85.0, 88.0, 88.0, 88.0, 85.0, 84.0, 90.0, 92.0, 74.0, 68.0, 68.0, 63.0, 70.0, 88.0, 75.0, 70.0, 67.0, 67.0, 67.0, 110.0, 85.0, 92.0, 112.0, 96.0, 84.0, 90.0, 86.0, 52.0, 84.0, 79.0, 82.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"td962e798520d40d3a03c32195d21336c",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 82.0, "min": 70.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tf337f74a28244a7cb9019d584c41fff2",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 46.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tc0f1bb9bff17498bac046b7fc3baa6a3",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 9.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Note that a colormap must be explicitly specified when creating a color
scale - this is necessary to avoid ambiguity when a single coordinate
system contains multiple visualizations or data series.

Canvas Color Scales
-------------------

For situations where displaying a vertical color scale with a single set
of Cartesian axes is too limiting, you can add horizontal color scales
directly to a canvas using any :ref:`canvas-layout` that makes sense.
For example, the following figure uses a single horizontal color scale
to display a colormap that is shared between two coordinate systems:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=400)
    
    axes = canvas.cartesian(bounds=("10%", "45%", "10%", "65%"), xlabel="Year", ylabel="Horsepower")
    axes.scatterplot(
        data["Year"],
        data["Horsepower"],
        color=(data["MPG"], colormap),
        size=8,
        mstyle={"stroke":"black", "stroke-opacity":0.3}
    )
    
    axes = canvas.cartesian(bounds=("-45%", "-10%", "10%", "65%"), xlabel="Weight", ylabel="Horsepower")
    axes.y.spine.position="high"
    axes.scatterplot(
        data["Weight"],
        data["Horsepower"],
        color=(data["MPG"], colormap),
        size=8,
        mstyle={"stroke":"black", "stroke-opacity":0.3}
    )
    
    canvas.color_scale(colormap, bounds=("10%", "-10%", "75%", "90%"), label="MPG");




.. raw:: html

    <div class="toyplot" id="tb9c36cb72fff46098f7c18d35bd07c03" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="tc71ea151e62b415eb35209660ddc4b0d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 400.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="td7e14901c9744579aedfab856471b39a"><clipPath id="t4db124f2f8d34a66b811f2bc3a9ac7e4"><rect height="240.0" width="230.0" x="50.0" y="30.0"></rect></clipPath><g clip-path="url(#t4db124f2f8d34a66b811f2bc3a9ac7e4)"><g class="toyplot-mark-Point" id="t411611e07f2144178048413baaf97d26"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 131.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 96.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 72.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 77.74509803921568)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 66.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 104.70588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 137.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 66.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 260.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 215.7843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 187.7450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(38.8%,22.3%,2.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 77.74509803921568)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(38.8%,22.3%,2.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 93.921568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 83.13725490196077)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(32.9%,18.8%,2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 101.47058823529413)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 131.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 144.6078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 227.6470588235294)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(52.6%,81.4%,76.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 235.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 251.37254901960785)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 131.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 144.6078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 85.29411764705883)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 142.45098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 137.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 104.70588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 188.82352941176472)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 227.6470588235294)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 215.7843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 235.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 210.3921568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 161.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 96.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 139.21568627450978)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 77.74509803921568)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 66.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 260.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 129.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 208.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 194.2156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 61.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 256.7647058823529)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 211.47058823529412)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 188.82352941176472)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 178.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 220.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 253.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 243.82352941176472)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 209.3137254901961)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 150.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 170.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 220.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 206.07843137254903)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 203.92156862745097)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 252.45098039215688)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 222.2549019607843)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 210.3921568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 224.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 220.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 180.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(64.2%,40.5%,10.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 145.68627450980392)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 222.2549019607843)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.8%,84.9%,65.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 253.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.6%,78.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 252.45098039215688)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.9%,94.1%,93.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.3%,89.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 199.6078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 193.13725490196077)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 180.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.3%,91.8%,89.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 247.05882352941174)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93%,84.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 206.07843137254903)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 203.92156862745097)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 104.70588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 148.92156862745097)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.6%,78.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93%,84.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 213.62745098039215)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.1%,93%,91.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 241.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 220.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.1%,93%,91.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.4%,38.9%,35.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 257.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.1%,76%,71.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 238.43137254901958)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(68.9%,88%,85.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 253.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(19%,57.6%,54.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.1%,76%,71.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.2%,73.5%,45.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(84.5%,70.1%,41.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 159.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.4%,82%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(84.5%,70.1%,41.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.2%,77.3%,51.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.7%,78.1%,52.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.8%,64.7%,35%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.2%,61.3%,30.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 180.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.8%,58.6%,27.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 131.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.2%,61.3%,30.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 159.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.7%,94.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.2%,92.5%,90.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.4%,79.3%,55%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94.5%,87.7%,70.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.9%,90%,74.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,90.4%,75.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.5%,76.2%,49.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 198.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 174.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,81.3%,58.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(73.2%,49%,16.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 166.17647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.3%,91.8%,89.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.9%,94.1%,93.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.8%,72.8%,45%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.3%,84.1%,63.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.2%,77.3%,51.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.5%,57.9%,26.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 170.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 160.7843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.5%,62%,31.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 164.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.2%,53.2%,20.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 142.45098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 156.47058823529412)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 174.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(75.5%,90.7%,88.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(59.2%,84.1%,80.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(47.2%,78.3%,73.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.5%,94%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,92.8%,83.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 226.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 174.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,90.4%,75.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(58.5%,83.8%,79.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.3%,82.9%,78.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.3%,91%,88.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(34.7%,69.2%,65.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 235.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(93.2%,95.4%,95.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.3%,94.9%,94.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.7%,90.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(7.7%,46.8%,43.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 227.6470588235294)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(28.5%,64.7%,61.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74%,90.1%,87.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(35.5%,69.8%,65.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.2%,88.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.3%,77.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.5%,68.1%,39.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(57.7%,83.5%,79.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,93.8%,92.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.3%,92.1%,90.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 210.3921568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(73.3%,89.8%,87.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0%,23.5%,18.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.6%,96%,95.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(11.5%,50.4%,47.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.2%,33.6%,29.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 257.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.3%,37.5%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 257.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(41.7%,74.3%,70.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.2%,32.3%,28.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,85%,81.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,93.8%,92.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 242.7450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.6%,88.3%,85.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 167.2549019607843)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.7%,89.6%,74%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(52.6%,81.4%,76.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(71.8%,89.2%,86.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.5%,89.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.4%,85.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 210.3921568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.2%,88.8%,72.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(20.7%,59.1%,56%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 247.05882352941174)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(21.4%,59.7%,56.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 240.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(51.8%,81.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.6%,89.5%,87%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(31.6%,67%,63.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 242.7450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(59.2%,84.1%,80.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(54.8%,82.3%,78%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 241.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(57%,83.2%,79.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86%,93.7%,92.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 229.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(62.2%,85.3%,81.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(71.8%,89.2%,86.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(68.1%,87.7%,84.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(77.7%,91.6%,89.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 229.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94.6%,95.7%,95.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(82.2%,92.8%,91.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 227.6470588235294)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,92.8%,83.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 184.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.5%,91.2%,77.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 180.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.5%,84.5%,64.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.5%,89.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.5%,57.9%,26.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(60%,84.4%,80.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 210.3921568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 229.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 241.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(60%,84.4%,80.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 210.3921568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 188.82352941176472)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 206.07843137254903)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.3%,34.9%,31.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 253.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 224.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 221.17647058823528)"><circle r="4.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="tfd770a2cbb084b009a5be284f2f58a98" transform="translate(60.0,260.0)translate(0,10.0)"><line style="" x1="0" x2="210.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">70</text></g><g transform="translate(70.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">74</text></g><g transform="translate(140.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">78</text></g><g transform="translate(210.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">82</text></g></g><g transform="translate(105.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-13.008000000000001" y="10.265999999999998">Year</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t34ecd9b4af814409931dabc124bb051a" transform="translate(60.0,260.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="198.4313725490196" y1="0" y2="0"></line><g><g transform="translate(4.313725490196078,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.440892098500626e-16">50</text></g><g transform="translate(58.23529411764706,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.440892098500626e-16">100</text></g><g transform="translate(112.15686274509804,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.440892098500626e-16">150</text></g><g transform="translate(166.078431372549,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.440892098500626e-16">200</text></g><g transform="translate(220.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.440892098500626e-16">250</text></g></g><g transform="translate(110.0,-22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-34.674" y="0.0">Horsepower</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="td22f6b4df1794dc9a598dd013ef8ff47"><clipPath id="tca983458dc1546cb99e3f46d8df524f5"><rect height="240.0" width="230.0" x="320.0" y="30.0"></rect></clipPath><g clip-path="url(#tca983458dc1546cb99e3f46d8df524f5)"><g class="toyplot-mark-Point" id="t3f88922d8619465eb78d5c6124569693"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(442.59143748227956, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(453.8446271618939, 131.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(438.5426708250638, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(438.3640487666572, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(439.31669974482566, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(492.42699177771476, 96.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(493.2010206974766, 72.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(490.7003118797845, 77.74509803921568)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(497.42840941309896, 66.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(463.19251488517153, 104.70588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(446.1043379642756, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(448.8432095265098, 137.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(457.89339381910975, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(417.70343067762974, 66.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.1913807768642, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(402.63963708534163, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(399.12673660334565, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(387.99262829600224, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.7825347320669, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(343.2180323220868, 260.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(393.053586617522, 215.7843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(378.6447405727247, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.3700028352707, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(366.97476609016155, 187.7450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(391.62461015026935, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(38.8%,22.3%,2.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(508.7411397788489, 77.74509803921568)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(38.8%,22.3%,2.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(494.51091579245815, 93.921568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(494.86815990927136, 83.13725490196077)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(32.9%,18.8%,2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(515.7074000567054, 101.47058823529413)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.7825347320669, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(368.7609866742274, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(366.61752197334846, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(390.791040544372, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(438.72129288347037, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(432.1718174085625, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(430.56421888290333, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(429.7306492770059, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(484.5676212078253, 131.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(499.75049617238443, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(481.2928834703714, 144.6078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(477.83952367451093, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(528.9849730649277, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(516.5409696626027, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(540.0, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(410.3203855968245, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(377.3348454777431, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(429.37340516019276, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(420.8590870428126, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(366.14119648426424, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.36574992911824, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(357.4482563084774, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(356.91239013325776, 227.6470588235294)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(339.5265097816841, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(52.6%,81.4%,76.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(330.0, 235.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(343.15849163595124, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(350.3629146583499, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(369.5945562801248, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.5443719875248, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(368.1655798128721, 251.37254901960785)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(377.3348454777431, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(366.4984406010774, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(488.43776580663456, 131.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(495.04678196767793, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(480.16161043379645, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(479.80436631698325, 144.6078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(452.5942727530479, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(509.81287212928834, 85.29411764705883)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(502.0130422455344, 142.45098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(499.2741706833002, 137.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(497.24978735469233, 104.70588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(372.6906719591721, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(465.69322370286363, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(477.958605046782, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(489.6285795293451, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(476.7082506379359, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(408.59370569889427, 188.82352941176472)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(383.46753614970225, 227.6470588235294)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(411.33257726112845, 215.7843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(364.29543521406293, 235.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(376.5608165579813, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(370.18996314148, 210.3921568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(383.16983271902467, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(362.80691806067483, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(358.9963141480011, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(478.07768641905307, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(452.5942727530479, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(471.40912957187413, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(474.6243266231925, 161.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(458.8460447972781, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(528.8063510065211, 96.078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(499.75049617238443, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(493.73688687269635, 139.21568627450978)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(486.23476041962005, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(515.886022115112, 77.74509803921568)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(528.7468103203856, 66.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(461.4658349872413, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(419.7873546923731, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(429.13524241565074, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(409.30819393252057, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(413.8332860788205, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(406.867025800964, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(350.06521122767225, 260.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(531.4856818826198, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(526.067479444287, 129.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(511.0632265381344, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(501.8344201871279, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(400.01984689537846, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(369.6540969662603, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(376.91806067479445, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.60816557981286, 208.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.42529061525374, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(371.4998582364616, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(381.1454493904168, 194.2156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(368.8205273603629, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(477.00595406861356, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(488.67592855117664, 61.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(345.1233342784236, 256.7647058823529)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(362.4496739438616, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(387.69492486532465, 211.47058823529412)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(404.7235611000851, 188.82352941176472)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(436.33966543804934, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(392.3390983838957, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(401.09157924581797, 178.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(452.1179472639637, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(418.6560816557982, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(406.6884037425574, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(432.5886022115112, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(350.06521122767225, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(379.89509498157076, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(343.27757300822225, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(385.3132974199036, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(459.0842075418202, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.2126453076269, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(449.08137227105186, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(480.51885455060955, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(513.742557414233, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(499.3337113694358, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(510.110575559966, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.4255741423306, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(366.08165579812874, 220.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(350.83924014743405, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(370.9044513751063, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(332.14346470087895, 253.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(353.2208675928551, 243.82352941176472)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.48483130138925, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(359.4726396370853, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(367.6892543237879, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(382.1576410547207, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(376.32265381343916, 209.3137254901961)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(353.04224553444857, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(428.3016728097533, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(439.91210660618094, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(438.3045080805217, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(421.9903600793876, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(511.8967961440317, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(498.32151970513183, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(501.7748795009923, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(511.241848596541, 150.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(466.5863339948965, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(465.9909271335413, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(456.04763254890844, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(459.32237028636234, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(414.90501842925994, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(425.74142330592576, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(422.6453076268784, 170.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(363.22370286362343, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(391.0887439750496, 220.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(407.46243266231926, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(388.29033172667994, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(394.83980720158775, 206.07843137254903)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(366.3198185426708, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(385.49191947831014, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(411.6302806918061, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(349.29118230791045, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(425.1460164445704, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(394.3634817125036, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(410.02268216614686, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(409.30819393252057, 203.92156862745097)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(392.9940459313865, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(340.8364048766657, 252.45098039215688)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(380.66912390133257, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(366.14119648426424, 222.2549019607843)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(387.09951800396937, 210.3921568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(368.22512049900763, 224.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(365.0694641338248, 220.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(484.9248653246385, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(483.43634817125036, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(469.8610717323504, 180.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(64.2%,40.5%,10.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(484.9248653246385, 145.68627450980392)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(426.455911539552, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(433.6007938758151, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(413.2974199036008, 222.2549019607843)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.8%,84.9%,65.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(417.6438899914942, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(355.126169549192, 253.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.6%,78.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(362.80691806067483, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(349.29118230791045, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(340.8364048766657, 252.45098039215688)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(451.34391834420194, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(446.7592855117664, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.98667422738873, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(424.074284094131, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.9%,94.1%,93.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(342.6226254607315, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(352.4468386730933, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(362.27105188545505, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.3%,89.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(386.6827332010207, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(421.51403459030337, 199.6078431372549)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(468.5511766373689, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(428.65891692656646, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(408.41508364048764, 193.13725490196077)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(461.40629430110573, 180.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(494.7490785370003, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(475.3983555429544, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(464.38332860788205, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(457.5361497022966, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.3%,91.8%,89.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(355.7215764105472, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(362.27105188545505, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(342.6226254607315, 247.05882352941174)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93%,84.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(370.9044513751063, 206.07843137254903)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(349.7675077969946, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(464.97873546923734, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(475.696058973632, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(480.45931386447404, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(489.6881202154806, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(443.54408846044794, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(437.88772327757306, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0935639353558, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(443.8417918911256, 203.92156862745097)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(485.2225687553161, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(481.9478310178622, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(491.4743407995463, 104.70588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(492.0697476609016, 148.92156862745097)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(349.46980436631696, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.6%,78.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(397.10235327473777, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(368.8205273603629, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93%,84.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(397.99546356677064, 213.62745098039215)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.1%,93%,91.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(356.0788205273604, 241.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(357.507796994613, 220.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(352.14913524241564, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.1%,93%,91.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(364.3549759001985, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(401.5679047349022, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(388.7666572157641, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(395.9115395520272, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.4%,38.9%,35.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(352.14913524241564, 257.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.1%,76%,71.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(341.13410830734335, 238.43137254901958)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(68.9%,88%,85.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(352.14913524241564, 253.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(19%,57.6%,54.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(357.21009356393535, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.1%,76%,71.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(341.13410830734335, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.2%,73.5%,45.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(434.31528210944145, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(84.5%,70.1%,41.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(456.345335979586, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(446.5211227672243, 159.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(444.43719875248087, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(421.811738020981, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(410.499007655231, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.4%,82%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(395.9115395520272, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(438.1854267082507, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(84.5%,70.1%,41.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(425.086475758435, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.2%,77.3%,51.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(435.2083924014743, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.7%,78.1%,52.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(416.7507796994613, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.8%,64.7%,35%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(449.4981570740006, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.2%,61.3%,30.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(436.99461298554013, 180.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(437.88772327757306, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.8%,58.6%,27.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(439.0785370002835, 131.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.2%,61.3%,30.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(424.7887723277573, 159.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(476.88687269634255, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(362.27105188545505, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.7%,94.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(386.38502977034307, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(370.9044513751063, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.2%,92.5%,90.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(366.7366033456195, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.4%,79.3%,55%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(383.7056988942444, 207.156862745098)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94.5%,87.7%,70.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(397.4000567054154, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.9%,90%,74.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(403.9495321803232, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,90.4%,75.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(377.1562234193366, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.5%,76.2%,49.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(402.46101502693506, 198.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(420.9186277289481, 174.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,81.3%,58.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(400.37709101219167, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(73.2%,49%,16.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(436.99461298554013, 166.17647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.3%,91.8%,89.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(352.4468386730933, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.9%,94.1%,93.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(361.08023816274454, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(427.17039977317836, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.8%,72.8%,45%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(411.98752480861924, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.3%,84.1%,63.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(406.0334561950666, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(428.3612134958889, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.2%,77.3%,51.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(434.0175786787638, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(462.59710802381625, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.5%,57.9%,26.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(455.7499291182308, 170.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(469.44428692940176, 160.7843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.5%,62%,31.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(462.001701162461, 164.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.2%,53.2%,20.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(493.55826481428977, 142.45098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(475.3388148568189, 156.47058823529412)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(448.60504678196764, 174.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(468.5511766373689, 147.843137254902)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(75.5%,90.7%,88.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(348.5766940742841, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(59.2%,84.1%,80.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(351.5537283810604, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(47.2%,78.3%,73.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(347.98128721292886, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.5%,94%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(392.9345052452509, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,92.8%,83.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(444.1394953218032, 226.5686274509804)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(466.1695491919478, 174.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(423.8956620357244, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,90.4%,75.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(437.59001984689536, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(58.5%,83.8%,79.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(364.95038276155367, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.3%,82.9%,78.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(361.9733484547774, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.3%,91%,88.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(354.233059257159, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(34.7%,69.2%,65.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.7825347320669, 235.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(93.2%,95.4%,95.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(392.9345052452509, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.3%,94.9%,94.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(388.46895378508646, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.7%,90.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(394.72072582931673, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(386.14686702580093, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(7.7%,46.8%,43.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(361.6161043379643, 227.6470588235294)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(28.5%,64.7%,61.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(351.1369435781117, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74%,90.1%,87.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.1871278707116, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(35.5%,69.8%,65.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(354.1735185710235, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(393.41083073433515, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.2%,88.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(404.8426424723561, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.3%,77.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.76155372838105, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.5%,68.1%,39.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(435.2679330876099, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(57.7%,83.5%,79.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(364.23589452792737, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,93.8%,92.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(395.3756733768075, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.3%,92.1%,90.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(385.3132974199036, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(378.88290331726677, 210.3921568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(73.3%,89.8%,87.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(368.8205273603629, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0%,23.5%,18.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(359.59172100935643, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.6%,96%,95.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(400.67479444286926, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(11.5%,50.4%,47.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(359.59172100935643, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.2%,33.6%,29.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(358.1032038559683, 257.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.3%,37.5%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(372.9883753898497, 257.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(41.7%,74.3%,70.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(409.60589736319815, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(427.468103203856, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.2%,32.3%,28.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(344.1111426141197, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,85%,81.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(361.6756450240998, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,93.8%,92.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(343.813439183442, 242.7450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.6%,88.3%,85.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(407.2242699177771, 167.2549019607843)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.7%,89.6%,74%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(378.04933371136946, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(52.6%,81.4%,76.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(382.8125886022115, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(71.8%,89.2%,86.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(370.3090445137511, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(382.2171817408563, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.5%,89.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(390.8505812305075, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.4%,85.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(389.9574709384746, 210.3921568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.2%,88.8%,72.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(396.20924298270484, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.965409696626, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(20.7%,59.1%,56%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(338.4547774312447, 247.05882352941174)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(21.4%,59.7%,56.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(345.5996597675078, 240.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(51.8%,81.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(338.75248086192227, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.6%,89.5%,87%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(356.91239013325776, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(351.5537283810604, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(31.6%,67%,63.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(356.01927984122483, 242.7450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(59.2%,84.1%,80.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(352.14913524241564, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(54.8%,82.3%,78%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(365.8434930535866, 241.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(57%,83.2%,79.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(355.7215764105472, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86%,93.7%,92.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.66770626594837, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(364.3549759001985, 229.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(62.2%,85.3%,81.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(365.545789622909, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(71.8%,89.2%,86.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(373.8814856818826, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(68.1%,87.7%,84.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(389.65976750779697, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(77.7%,91.6%,89.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(390.8505812305075, 229.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94.6%,95.7%,95.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(426.27728948114543, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(82.2%,92.8%,91.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(422.10944145165865, 227.6470588235294)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,92.8%,83.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(406.6288630564219, 184.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.5%,91.2%,77.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(408.41508364048764, 180.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.5%,84.5%,64.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(437.2923164162178, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.5%,89.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(455.7499291182308, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(416.155372838106, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.5%,57.9%,26.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(440.2693507229941, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(389.06436064644174, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(391.14828466118513, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(60%,84.4%,80.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(376.5608165579813, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(387.27814006237594, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(384.3011057555997, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(396.8046498440601, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(404.5449390416785, 210.3921568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(351.85143181173805, 229.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(354.53076268783667, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(351.25602495038277, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.48483130138925, 241.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.48483130138925, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(362.5687553161327, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(365.2480861922313, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(60%,84.4%,80.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(367.6297136376524, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(350.9583215197051, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(350.9583215197051, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(352.7445421037709, 237.3529411764706)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(409.30819393252057, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(413.47604196200734, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(387.87354692373117, 210.3921568627451)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(402.7587184576127, 188.82352941176472)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(392.6368018145733, 206.07843137254903)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.07229940459314, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(409.60589736319815, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(400.079387581514, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.3%,34.9%,31.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.7825347320669, 253.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(370.60674794442866, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(390.25517436915226, 224.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(395.9115395520272, 221.17647058823528)"><circle r="4.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t014f46945f7f47edba92eca7b3f3d2cb" transform="translate(330.0,260.0)translate(0,10.0)"><line style="" x1="0" x2="210.0" y1="0" y2="0"></line><g><g transform="translate(23.04224553444854,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="8.555">2000</text></g><g transform="translate(82.58293166997449,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="8.555">3000</text></g><g transform="translate(142.12361780550043,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="8.555">4000</text></g><g transform="translate(201.66430394102636,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="8.555">5000</text></g></g><g transform="translate(105.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-19.998" y="10.265999999999998">Weight</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t782897efbeff4622bf40386966b237b0" transform="translate(540.0,260.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="198.4313725490196" y1="0" y2="0"></line><g><g transform="translate(4.313725490196078,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g><g transform="translate(58.23529411764706,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="8.555">100</text></g><g transform="translate(112.15686274509804,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="8.555">150</text></g><g transform="translate(166.078431372549,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="8.555">200</text></g><g transform="translate(220.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="8.555">250</text></g></g><g transform="translate(110.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-34.674" y="10.265999999999998">Horsepower</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="tb5d4e8e6abd54ef385a2eea448dfa417"><clipPath id="t7eb08be454274104a53fa0ddf18d0784"><rect height="20.0" width="480.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#t7eb08be454274104a53fa0ddf18d0784)" transform="translate(60.0,330.0)"><g class="toyplot-color-Map" id="t15ab67f51a884d14b82e4b1134e562e3"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t2d4a9aae41054ccc887d66e38627fb69" x1="0.0" x2="440.1951219512195" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(32.9%,18.8%,1.96%)" stop-opacity="1.0"></stop><stop offset="0.015873015873015865" stop-color="rgb(36.4%,20.9%,2.27%)" stop-opacity="1.0"></stop><stop offset="0.03174603174603173" stop-color="rgb(39.9%,22.9%,2.58%)" stop-opacity="1.0"></stop><stop offset="0.04761904761904764" stop-color="rgb(43.4%,25%,2.89%)" stop-opacity="1.0"></stop><stop offset="0.0634920634920635" stop-color="rgb(46.9%,27%,3.21%)" stop-opacity="1.0"></stop><stop offset="0.07936507936507937" stop-color="rgb(50.4%,29.1%,3.52%)" stop-opacity="1.0"></stop><stop offset="0.09523809523809523" stop-color="rgb(53.9%,31.1%,3.83%)" stop-opacity="1.0"></stop><stop offset="0.11111111111111109" stop-color="rgb(57.1%,33.9%,5.45%)" stop-opacity="1.0"></stop><stop offset="0.126984126984127" stop-color="rgb(60.3%,36.8%,7.63%)" stop-opacity="1.0"></stop><stop offset="0.14285714285714282" stop-color="rgb(63.5%,39.8%,9.8%)" stop-opacity="1.0"></stop><stop offset="0.15873015873015875" stop-color="rgb(66.6%,42.8%,12%)" stop-opacity="1.0"></stop><stop offset="0.1746031746031746" stop-color="rgb(69.8%,45.8%,14.2%)" stop-opacity="1.0"></stop><stop offset="0.19047619047619047" stop-color="rgb(73%,48.8%,16.3%)" stop-opacity="1.0"></stop><stop offset="0.2063492063492064" stop-color="rgb(75.7%,52.2%,19.6%)" stop-opacity="1.0"></stop><stop offset="0.22222222222222218" stop-color="rgb(77.7%,56.3%,24.6%)" stop-opacity="1.0"></stop><stop offset="0.2380952380952381" stop-color="rgb(79.7%,60.3%,29.6%)" stop-opacity="1.0"></stop><stop offset="0.253968253968254" stop-color="rgb(81.7%,64.3%,34.6%)" stop-opacity="1.0"></stop><stop offset="0.2698412698412698" stop-color="rgb(83.7%,68.4%,39.6%)" stop-opacity="1.0"></stop><stop offset="0.28571428571428564" stop-color="rgb(85.7%,72.4%,44.5%)" stop-opacity="1.0"></stop><stop offset="0.3015873015873016" stop-color="rgb(87.6%,76.3%,49.5%)" stop-opacity="1.0"></stop><stop offset="0.3174603174603175" stop-color="rgb(89%,78.7%,53.8%)" stop-opacity="1.0"></stop><stop offset="0.3333333333333333" stop-color="rgb(90.5%,81%,58.2%)" stop-opacity="1.0"></stop><stop offset="0.3492063492063492" stop-color="rgb(91.9%,83.4%,62.5%)" stop-opacity="1.0"></stop><stop offset="0.3650793650793651" stop-color="rgb(93.3%,85.8%,66.9%)" stop-opacity="1.0"></stop><stop offset="0.38095238095238093" stop-color="rgb(94.8%,88.1%,71.2%)" stop-opacity="1.0"></stop><stop offset="0.3968253968253968" stop-color="rgb(96.2%,90.5%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.4126984126984128" stop-color="rgb(96.4%,91.6%,79%)" stop-opacity="1.0"></stop><stop offset="0.42857142857142855" stop-color="rgb(96.4%,92.4%,82.1%)" stop-opacity="1.0"></stop><stop offset="0.4444444444444445" stop-color="rgb(96.3%,93.2%,85.2%)" stop-opacity="1.0"></stop><stop offset="0.4603174603174603" stop-color="rgb(96.2%,94.1%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.4761904761904762" stop-color="rgb(96.2%,94.9%,91.4%)" stop-opacity="1.0"></stop><stop offset="0.49206349206349204" stop-color="rgb(96.1%,95.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.507936507936508" stop-color="rgb(94.6%,95.7%,95.6%)" stop-opacity="1.0"></stop><stop offset="0.5238095238095238" stop-color="rgb(91.8%,95.1%,94.6%)" stop-opacity="1.0"></stop><stop offset="0.5396825396825397" stop-color="rgb(88.9%,94.4%,93.6%)" stop-opacity="1.0"></stop><stop offset="0.5555555555555556" stop-color="rgb(86.1%,93.7%,92.6%)" stop-opacity="1.0"></stop><stop offset="0.5714285714285714" stop-color="rgb(83.2%,93%,91.6%)" stop-opacity="1.0"></stop><stop offset="0.5873015873015873" stop-color="rgb(80.3%,92.3%,90.6%)" stop-opacity="1.0"></stop><stop offset="0.6031746031746031" stop-color="rgb(77.2%,91.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.6190476190476191" stop-color="rgb(72.7%,89.6%,87.1%)" stop-opacity="1.0"></stop><stop offset="0.634920634920635" stop-color="rgb(68.3%,87.8%,84.9%)" stop-opacity="1.0"></stop><stop offset="0.6507936507936508" stop-color="rgb(63.9%,86%,82.6%)" stop-opacity="1.0"></stop><stop offset="0.6666666666666666" stop-color="rgb(59.5%,84.2%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.6825396825396826" stop-color="rgb(55.1%,82.4%,78.2%)" stop-opacity="1.0"></stop><stop offset="0.6984126984126984" stop-color="rgb(50.6%,80.6%,75.9%)" stop-opacity="1.0"></stop><stop offset="0.7142857142857143" stop-color="rgb(46%,77.4%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.7301587301587302" stop-color="rgb(41.3%,74%,69.8%)" stop-opacity="1.0"></stop><stop offset="0.746031746031746" stop-color="rgb(36.7%,70.6%,66.7%)" stop-opacity="1.0"></stop><stop offset="0.7619047619047619" stop-color="rgb(32%,67.3%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.7777777777777777" stop-color="rgb(27.3%,63.9%,60.4%)" stop-opacity="1.0"></stop><stop offset="0.7936507936507936" stop-color="rgb(22.7%,60.6%,57.3%)" stop-opacity="1.0"></stop><stop offset="0.8095238095238094" stop-color="rgb(18.8%,57.4%,54.2%)" stop-opacity="1.0"></stop><stop offset="0.8253968253968256" stop-color="rgb(15.6%,54.3%,51.2%)" stop-opacity="1.0"></stop><stop offset="0.8412698412698414" stop-color="rgb(12.4%,51.3%,48.1%)" stop-opacity="1.0"></stop><stop offset="0.8571428571428571" stop-color="rgb(9.13%,48.2%,45.1%)" stop-opacity="1.0"></stop><stop offset="0.8730158730158729" stop-color="rgb(5.89%,45.2%,42%)" stop-opacity="1.0"></stop><stop offset="0.888888888888889" stop-color="rgb(2.66%,42.1%,39%)" stop-opacity="1.0"></stop><stop offset="0.9047619047619048" stop-color="rgb(0.373%,39.2%,36%)" stop-opacity="1.0"></stop><stop offset="0.9206349206349206" stop-color="rgb(0.311%,36.6%,33.1%)" stop-opacity="1.0"></stop><stop offset="0.9365079365079366" stop-color="rgb(0.249%,34%,30.3%)" stop-opacity="1.0"></stop><stop offset="0.9523809523809524" stop-color="rgb(0.187%,31.4%,27.4%)" stop-opacity="1.0"></stop><stop offset="0.9682539682539683" stop-color="rgb(0.124%,28.8%,24.6%)" stop-opacity="1.0"></stop><stop offset="0.9841269841269841" stop-color="rgb(0.0622%,26.1%,21.7%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(0%,23.5%,18.8%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t2d4a9aae41054ccc887d66e38627fb69);stroke:none;stroke-width:1.0" width="440.1951219512195" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t1ca4eee3bba04a88a77b2dbfb2ef5afb" transform="translate(60.0,330.0)translate(0,10.0)"><line style="" x1="0" x2="440.1951219512195" y1="0" y2="0"></line><g><g transform="translate(11.707317073170731,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(128.78048780487805,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g><g transform="translate(245.85365853658539,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">30</text></g><g transform="translate(362.9268292682927,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">40</text></g><g transform="translate(480.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g></g><g transform="translate(240.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-13.668" y="10.265999999999998">MPG</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tb9c36cb72fff46098f7c18d35bd07c03";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tc71ea151e62b415eb35209660ddc4b0d";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t411611e07f2144178048413baaf97d26","data","point",["x", "y0"],[[70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0], [130.0, 165.0, 150.0, 150.0, 140.0, 198.0, 220.0, 215.0, 225.0, 190.0, 170.0, 160.0, 150.0, 225.0, 95.0, 95.0, 97.0, 85.0, 88.0, 46.0, 87.0, 90.0, 95.0, 113.0, 90.0, 215.0, 200.0, 210.0, 193.0, 88.0, 90.0, 95.0, 100.0, 105.0, 100.0, 88.0, 100.0, 165.0, 175.0, 153.0, 150.0, 180.0, 170.0, 175.0, 110.0, 72.0, 100.0, 88.0, 86.0, 90.0, 70.0, 76.0, 65.0, 69.0, 60.0, 70.0, 95.0, 80.0, 54.0, 90.0, 86.0, 165.0, 175.0, 150.0, 153.0, 150.0, 208.0, 155.0, 160.0, 190.0, 97.0, 150.0, 130.0, 140.0, 150.0, 112.0, 76.0, 87.0, 69.0, 86.0, 92.0, 97.0, 80.0, 88.0, 175.0, 150.0, 145.0, 137.0, 150.0, 198.0, 150.0, 158.0, 150.0, 215.0, 225.0, 175.0, 105.0, 100.0, 100.0, 88.0, 95.0, 46.0, 150.0, 167.0, 170.0, 180.0, 100.0, 88.0, 72.0, 94.0, 90.0, 85.0, 107.0, 90.0, 145.0, 230.0, 49.0, 75.0, 91.0, 112.0, 150.0, 110.0, 122.0, 180.0, 95.0, 100.0, 100.0, 67.0, 80.0, 65.0, 75.0, 100.0, 110.0, 105.0, 140.0, 150.0, 150.0, 140.0, 150.0, 83.0, 67.0, 78.0, 52.0, 61.0, 75.0, 75.0, 75.0, 97.0, 93.0, 67.0, 95.0, 105.0, 72.0, 72.0, 170.0, 145.0, 150.0, 148.0, 110.0, 105.0, 110.0, 95.0, 110.0, 110.0, 129.0, 75.0, 83.0, 100.0, 78.0, 96.0, 71.0, 97.0, 97.0, 70.0, 90.0, 95.0, 88.0, 98.0, 115.0, 53.0, 86.0, 81.0, 92.0, 79.0, 83.0, 140.0, 150.0, 120.0, 152.0, 100.0, 105.0, 81.0, 90.0, 52.0, 60.0, 70.0, 53.0, 100.0, 78.0, 110.0, 95.0, 71.0, 70.0, 75.0, 72.0, 102.0, 150.0, 88.0, 108.0, 120.0, 180.0, 145.0, 130.0, 150.0, 68.0, 80.0, 58.0, 96.0, 70.0, 145.0, 110.0, 145.0, 130.0, 110.0, 105.0, 100.0, 98.0, 180.0, 170.0, 190.0, 149.0, 78.0, 88.0, 75.0, 89.0, 63.0, 83.0, 67.0, 78.0, 97.0, 110.0, 110.0, 48.0, 66.0, 52.0, 70.0, 60.0, 110.0, 140.0, 139.0, 105.0, 95.0, 85.0, 88.0, 100.0, 90.0, 105.0, 85.0, 110.0, 120.0, 145.0, 165.0, 139.0, 140.0, 68.0, 95.0, 97.0, 75.0, 95.0, 105.0, 85.0, 97.0, 103.0, 125.0, 115.0, 133.0, 71.0, 68.0, 115.0, 85.0, 88.0, 90.0, 110.0, 130.0, 129.0, 138.0, 135.0, 155.0, 142.0, 125.0, 150.0, 71.0, 65.0, 80.0, 80.0, 77.0, 125.0, 71.0, 90.0, 70.0, 70.0, 65.0, 69.0, 90.0, 115.0, 115.0, 90.0, 76.0, 60.0, 70.0, 65.0, 90.0, 88.0, 90.0, 90.0, 78.0, 90.0, 75.0, 92.0, 75.0, 65.0, 105.0, 65.0, 48.0, 48.0, 67.0, 67.0, 67.0, 67.0, 62.0, 132.0, 100.0, 88.0, 72.0, 84.0, 84.0, 92.0, 110.0, 84.0, 58.0, 64.0, 60.0, 67.0, 65.0, 62.0, 68.0, 63.0, 65.0, 65.0, 74.0, 75.0, 75.0, 100.0, 74.0, 80.0, 76.0, 116.0, 120.0, 110.0, 105.0, 88.0, 85.0, 88.0, 88.0, 88.0, 85.0, 84.0, 90.0, 92.0, 74.0, 68.0, 68.0, 63.0, 70.0, 88.0, 75.0, 70.0, 67.0, 67.0, 67.0, 110.0, 85.0, 92.0, 112.0, 96.0, 84.0, 90.0, 86.0, 52.0, 84.0, 79.0, 82.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tfd770a2cbb084b009a5be284f2f58a98",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 82.0, "min": 70.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 210.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t34ecd9b4af814409931dabc124bb051a",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 46.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 220.0, "min": 0.0}, "scale": "linear"}]);
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t3f88922d8619465eb78d5c6124569693","data","point",["x", "y0"],[[3504.0, 3693.0, 3436.0, 3433.0, 3449.0, 4341.0, 4354.0, 4312.0, 4425.0, 3850.0, 3563.0, 3609.0, 3761.0, 3086.0, 2372.0, 2833.0, 2774.0, 2587.0, 2130.0, 1835.0, 2672.0, 2430.0, 2375.0, 2234.0, 2648.0, 4615.0, 4376.0, 4382.0, 4732.0, 2130.0, 2264.0, 2228.0, 2634.0, 3439.0, 3329.0, 3302.0, 3288.0, 4209.0, 4464.0, 4154.0, 4096.0, 4955.0, 4746.0, 5140.0, 2962.0, 2408.0, 3282.0, 3139.0, 2220.0, 2123.0, 2074.0, 2065.0, 1773.0, 1613.0, 1834.0, 1955.0, 2278.0, 2126.0, 2254.0, 2408.0, 2226.0, 4274.0, 4385.0, 4135.0, 4129.0, 3672.0, 4633.0, 4502.0, 4456.0, 4422.0, 2330.0, 3892.0, 4098.0, 4294.0, 4077.0, 2933.0, 2511.0, 2979.0, 2189.0, 2395.0, 2288.0, 2506.0, 2164.0, 2100.0, 4100.0, 3672.0, 3988.0, 4042.0, 3777.0, 4952.0, 4464.0, 4363.0, 4237.0, 4735.0, 4951.0, 3821.0, 3121.0, 3278.0, 2945.0, 3021.0, 2904.0, 1950.0, 4997.0, 4906.0, 4654.0, 4499.0, 2789.0, 2279.0, 2401.0, 2379.0, 2124.0, 2310.0, 2472.0, 2265.0, 4082.0, 4278.0, 1867.0, 2158.0, 2582.0, 2868.0, 3399.0, 2660.0, 2807.0, 3664.0, 3102.0, 2901.0, 3336.0, 1950.0, 2451.0, 1836.0, 2542.0, 3781.0, 3632.0, 3613.0, 4141.0, 4699.0, 4457.0, 4638.0, 4257.0, 2219.0, 1963.0, 2300.0, 1649.0, 2003.0, 2125.0, 2108.0, 2246.0, 2489.0, 2391.0, 2000.0, 3264.0, 3459.0, 3432.0, 3158.0, 4668.0, 4440.0, 4498.0, 4657.0, 3907.0, 3897.0, 3730.0, 3785.0, 3039.0, 3221.0, 3169.0, 2171.0, 2639.0, 2914.0, 2592.0, 2702.0, 2223.0, 2545.0, 2984.0, 1937.0, 3211.0, 2694.0, 2957.0, 2945.0, 2671.0, 1795.0, 2464.0, 2220.0, 2572.0, 2255.0, 2202.0, 4215.0, 4190.0, 3962.0, 4215.0, 3233.0, 3353.0, 3012.0, 3085.0, 2035.0, 2164.0, 1937.0, 1795.0, 3651.0, 3574.0, 3645.0, 3193.0, 1825.0, 1990.0, 2155.0, 2565.0, 3150.0, 3940.0, 3270.0, 2930.0, 3820.0, 4380.0, 4055.0, 3870.0, 3755.0, 2045.0, 2155.0, 1825.0, 2300.0, 1945.0, 3880.0, 4060.0, 4140.0, 4295.0, 3520.0, 3425.0, 3630.0, 3525.0, 4220.0, 4165.0, 4325.0, 4335.0, 1940.0, 2740.0, 2265.0, 2755.0, 2051.0, 2075.0, 1985.0, 2190.0, 2815.0, 2600.0, 2720.0, 1985.0, 1800.0, 1985.0, 2070.0, 1800.0, 3365.0, 3735.0, 3570.0, 3535.0, 3155.0, 2965.0, 2720.0, 3430.0, 3210.0, 3380.0, 3070.0, 3620.0, 3410.0, 3425.0, 3445.0, 3205.0, 4080.0, 2155.0, 2560.0, 2300.0, 2230.0, 2515.0, 2745.0, 2855.0, 2405.0, 2830.0, 3140.0, 2795.0, 3410.0, 1990.0, 2135.0, 3245.0, 2990.0, 2890.0, 3265.0, 3360.0, 3840.0, 3725.0, 3955.0, 3830.0, 4360.0, 4054.0, 3605.0, 3940.0, 1925.0, 1975.0, 1915.0, 2670.0, 3530.0, 3900.0, 3190.0, 3420.0, 2200.0, 2150.0, 2020.0, 2130.0, 2670.0, 2595.0, 2700.0, 2556.0, 2144.0, 1968.0, 2120.0, 2019.0, 2678.0, 2870.0, 3003.0, 3381.0, 2188.0, 2711.0, 2542.0, 2434.0, 2265.0, 2110.0, 2800.0, 2110.0, 2085.0, 2335.0, 2950.0, 3250.0, 1850.0, 2145.0, 1845.0, 2910.0, 2420.0, 2500.0, 2290.0, 2490.0, 2635.0, 2620.0, 2725.0, 2385.0, 1755.0, 1875.0, 1760.0, 2065.0, 1975.0, 2050.0, 1985.0, 2215.0, 2045.0, 2380.0, 2190.0, 2210.0, 2350.0, 2615.0, 2635.0, 3230.0, 3160.0, 2900.0, 2930.0, 3415.0, 3725.0, 3060.0, 3465.0, 2605.0, 2640.0, 2395.0, 2575.0, 2525.0, 2735.0, 2865.0, 1980.0, 2025.0, 1970.0, 2125.0, 2125.0, 2160.0, 2205.0, 2245.0, 1965.0, 1965.0, 1995.0, 2945.0, 3015.0, 2585.0, 2835.0, 2665.0, 2370.0, 2950.0, 2790.0, 2130.0, 2295.0, 2625.0, 2720.0], [130.0, 165.0, 150.0, 150.0, 140.0, 198.0, 220.0, 215.0, 225.0, 190.0, 170.0, 160.0, 150.0, 225.0, 95.0, 95.0, 97.0, 85.0, 88.0, 46.0, 87.0, 90.0, 95.0, 113.0, 90.0, 215.0, 200.0, 210.0, 193.0, 88.0, 90.0, 95.0, 100.0, 105.0, 100.0, 88.0, 100.0, 165.0, 175.0, 153.0, 150.0, 180.0, 170.0, 175.0, 110.0, 72.0, 100.0, 88.0, 86.0, 90.0, 70.0, 76.0, 65.0, 69.0, 60.0, 70.0, 95.0, 80.0, 54.0, 90.0, 86.0, 165.0, 175.0, 150.0, 153.0, 150.0, 208.0, 155.0, 160.0, 190.0, 97.0, 150.0, 130.0, 140.0, 150.0, 112.0, 76.0, 87.0, 69.0, 86.0, 92.0, 97.0, 80.0, 88.0, 175.0, 150.0, 145.0, 137.0, 150.0, 198.0, 150.0, 158.0, 150.0, 215.0, 225.0, 175.0, 105.0, 100.0, 100.0, 88.0, 95.0, 46.0, 150.0, 167.0, 170.0, 180.0, 100.0, 88.0, 72.0, 94.0, 90.0, 85.0, 107.0, 90.0, 145.0, 230.0, 49.0, 75.0, 91.0, 112.0, 150.0, 110.0, 122.0, 180.0, 95.0, 100.0, 100.0, 67.0, 80.0, 65.0, 75.0, 100.0, 110.0, 105.0, 140.0, 150.0, 150.0, 140.0, 150.0, 83.0, 67.0, 78.0, 52.0, 61.0, 75.0, 75.0, 75.0, 97.0, 93.0, 67.0, 95.0, 105.0, 72.0, 72.0, 170.0, 145.0, 150.0, 148.0, 110.0, 105.0, 110.0, 95.0, 110.0, 110.0, 129.0, 75.0, 83.0, 100.0, 78.0, 96.0, 71.0, 97.0, 97.0, 70.0, 90.0, 95.0, 88.0, 98.0, 115.0, 53.0, 86.0, 81.0, 92.0, 79.0, 83.0, 140.0, 150.0, 120.0, 152.0, 100.0, 105.0, 81.0, 90.0, 52.0, 60.0, 70.0, 53.0, 100.0, 78.0, 110.0, 95.0, 71.0, 70.0, 75.0, 72.0, 102.0, 150.0, 88.0, 108.0, 120.0, 180.0, 145.0, 130.0, 150.0, 68.0, 80.0, 58.0, 96.0, 70.0, 145.0, 110.0, 145.0, 130.0, 110.0, 105.0, 100.0, 98.0, 180.0, 170.0, 190.0, 149.0, 78.0, 88.0, 75.0, 89.0, 63.0, 83.0, 67.0, 78.0, 97.0, 110.0, 110.0, 48.0, 66.0, 52.0, 70.0, 60.0, 110.0, 140.0, 139.0, 105.0, 95.0, 85.0, 88.0, 100.0, 90.0, 105.0, 85.0, 110.0, 120.0, 145.0, 165.0, 139.0, 140.0, 68.0, 95.0, 97.0, 75.0, 95.0, 105.0, 85.0, 97.0, 103.0, 125.0, 115.0, 133.0, 71.0, 68.0, 115.0, 85.0, 88.0, 90.0, 110.0, 130.0, 129.0, 138.0, 135.0, 155.0, 142.0, 125.0, 150.0, 71.0, 65.0, 80.0, 80.0, 77.0, 125.0, 71.0, 90.0, 70.0, 70.0, 65.0, 69.0, 90.0, 115.0, 115.0, 90.0, 76.0, 60.0, 70.0, 65.0, 90.0, 88.0, 90.0, 90.0, 78.0, 90.0, 75.0, 92.0, 75.0, 65.0, 105.0, 65.0, 48.0, 48.0, 67.0, 67.0, 67.0, 67.0, 62.0, 132.0, 100.0, 88.0, 72.0, 84.0, 84.0, 92.0, 110.0, 84.0, 58.0, 64.0, 60.0, 67.0, 65.0, 62.0, 68.0, 63.0, 65.0, 65.0, 74.0, 75.0, 75.0, 100.0, 74.0, 80.0, 76.0, 116.0, 120.0, 110.0, 105.0, 88.0, 85.0, 88.0, 88.0, 88.0, 85.0, 84.0, 90.0, 92.0, 74.0, 68.0, 68.0, 63.0, 70.0, 88.0, 75.0, 70.0, 67.0, 67.0, 67.0, 110.0, 85.0, 92.0, 112.0, 96.0, 84.0, 90.0, 86.0, 52.0, 84.0, 79.0, 82.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t014f46945f7f47edba92eca7b3f3d2cb",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 5140.0, "min": 1613.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 210.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t782897efbeff4622bf40386966b237b0",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 46.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 220.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t1ca4eee3bba04a88a77b2dbfb2ef5afb",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 9.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 480.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Note that when manually adding a color scale to a canvas, you can orient
it any way you like (including diagonally!) by explicitly specifying the
endpoints in canvas coordinates:

.. code:: python

    colormap = toyplot.color.brewer.map(
        name="Spectral",
        domain_min=0,
        domain_max=1,
    )
    canvas = toyplot.Canvas(width=400)
    canvas.color_scale(colormap, x1=50, y1=-50, x2=50, y2=50, label="Bottom to Top")
    canvas.color_scale(colormap, x1=150, y1=50, x2=150, y2=-50, label="Top to Bottom")
    canvas.color_scale(colormap, x1=200, y1=150, x2=350, y2=150, label="Left to Right")
    canvas.color_scale(colormap, x1=350, y1=250, x2=200, y2=250, label="Right to Left");



.. raw:: html

    <div class="toyplot" id="t9fcffed9e5854b6c8cd8f2a70564d97a" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t82357e20ab2a47d4b899f3678ca34b55" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 400.0 400.0" width="400.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t5087c15fbf224dc8a5ed65bf6a3a3b99"><clipPath id="t6fdf27c0d03145b6b9db86e452d3e232"><rect height="20.0" width="300.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#t6fdf27c0d03145b6b9db86e452d3e232)" transform="translate(50.0,350.0)rotate(-90.0)"><g class="toyplot-color-Map" id="t1302f56aee9d43f9941a753794277a76"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t65ac84945566403fbde250ab6db452b2" x1="0.0" x2="300.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(36.9%,31%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.015873015873015872" stop-color="rgb(34.1%,34.5%,65.2%)" stop-opacity="1.0"></stop><stop offset="0.031746031746031744" stop-color="rgb(31.4%,38.1%,66.9%)" stop-opacity="1.0"></stop><stop offset="0.047619047619047616" stop-color="rgb(28.6%,41.6%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.06349206349206349" stop-color="rgb(25.9%,45.2%,70.3%)" stop-opacity="1.0"></stop><stop offset="0.07936507936507936" stop-color="rgb(23.2%,48.7%,71.9%)" stop-opacity="1.0"></stop><stop offset="0.09523809523809523" stop-color="rgb(20.4%,52.3%,73.6%)" stop-opacity="1.0"></stop><stop offset="0.11111111111111109" stop-color="rgb(21.9%,55.9%,73.1%)" stop-opacity="1.0"></stop><stop offset="0.12698412698412698" stop-color="rgb(25.1%,59.5%,71.6%)" stop-opacity="1.0"></stop><stop offset="0.14285714285714285" stop-color="rgb(28.3%,63.1%,70.1%)" stop-opacity="1.0"></stop><stop offset="0.15873015873015872" stop-color="rgb(31.6%,66.7%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.1746031746031746" stop-color="rgb(34.8%,70.3%,67.1%)" stop-opacity="1.0"></stop><stop offset="0.19047619047619047" stop-color="rgb(38.1%,73.9%,65.6%)" stop-opacity="1.0"></stop><stop offset="0.20634920634920634" stop-color="rgb(41.7%,76.8%,64.7%)" stop-opacity="1.0"></stop><stop offset="0.22222222222222218" stop-color="rgb(46%,78.4%,64.6%)" stop-opacity="1.0"></stop><stop offset="0.2380952380952381" stop-color="rgb(50.3%,80.1%,64.6%)" stop-opacity="1.0"></stop><stop offset="0.25396825396825395" stop-color="rgb(54.6%,81.8%,64.5%)" stop-opacity="1.0"></stop><stop offset="0.2698412698412698" stop-color="rgb(58.9%,83.5%,64.4%)" stop-opacity="1.0"></stop><stop offset="0.2857142857142857" stop-color="rgb(63.2%,85.2%,64.4%)" stop-opacity="1.0"></stop><stop offset="0.30158730158730157" stop-color="rgb(67.4%,86.8%,64.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746031744" stop-color="rgb(71.1%,88.3%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.3333333333333333" stop-color="rgb(74.8%,89.8%,62.7%)" stop-opacity="1.0"></stop><stop offset="0.3492063492063492" stop-color="rgb(78.4%,91.3%,62%)" stop-opacity="1.0"></stop><stop offset="0.36507936507936506" stop-color="rgb(82.1%,92.8%,61.3%)" stop-opacity="1.0"></stop><stop offset="0.38095238095238093" stop-color="rgb(85.8%,94.3%,60.5%)" stop-opacity="1.0"></stop><stop offset="0.3968253968253968" stop-color="rgb(89.5%,95.8%,59.8%)" stop-opacity="1.0"></stop><stop offset="0.4126984126984127" stop-color="rgb(91.4%,96.6%,61.5%)" stop-opacity="1.0"></stop><stop offset="0.4285714285714285" stop-color="rgb(93%,97.2%,64%)" stop-opacity="1.0"></stop><stop offset="0.44444444444444436" stop-color="rgb(94.6%,97.8%,66.4%)" stop-opacity="1.0"></stop><stop offset="0.46031746031746024" stop-color="rgb(96.1%,98.4%,68.8%)" stop-opacity="1.0"></stop><stop offset="0.4761904761904762" stop-color="rgb(97.7%,99.1%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.4920634920634921" stop-color="rgb(99.2%,99.7%,73.7%)" stop-opacity="1.0"></stop><stop offset="0.5079365079365079" stop-color="rgb(100%,99%,73.3%)" stop-opacity="1.0"></stop><stop offset="0.5238095238095237" stop-color="rgb(99.9%,97.1%,70%)" stop-opacity="1.0"></stop><stop offset="0.5396825396825397" stop-color="rgb(99.8%,95.2%,66.8%)" stop-opacity="1.0"></stop><stop offset="0.5555555555555556" stop-color="rgb(99.8%,93.2%,63.6%)" stop-opacity="1.0"></stop><stop offset="0.5714285714285714" stop-color="rgb(99.7%,91.3%,60.3%)" stop-opacity="1.0"></stop><stop offset="0.5873015873015872" stop-color="rgb(99.7%,89.4%,57.1%)" stop-opacity="1.0"></stop><stop offset="0.6031746031746031" stop-color="rgb(99.6%,87.2%,54%)" stop-opacity="1.0"></stop><stop offset="0.6190476190476191" stop-color="rgb(99.5%,84.1%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.6349206349206349" stop-color="rgb(99.5%,81%,48.8%)" stop-opacity="1.0"></stop><stop offset="0.6507936507936507" stop-color="rgb(99.4%,77.9%,46.1%)" stop-opacity="1.0"></stop><stop offset="0.6666666666666666" stop-color="rgb(99.3%,74.8%,43.5%)" stop-opacity="1.0"></stop><stop offset="0.6825396825396826" stop-color="rgb(99.3%,71.7%,40.9%)" stop-opacity="1.0"></stop><stop offset="0.6984126984126984" stop-color="rgb(99.2%,68.5%,38.3%)" stop-opacity="1.0"></stop><stop offset="0.7142857142857142" stop-color="rgb(98.7%,64.6%,36.4%)" stop-opacity="1.0"></stop><stop offset="0.7301587301587301" stop-color="rgb(98.2%,60.5%,34.5%)" stop-opacity="1.0"></stop><stop offset="0.746031746031746" stop-color="rgb(97.6%,56.5%,32.6%)" stop-opacity="1.0"></stop><stop offset="0.7619047619047619" stop-color="rgb(97%,52.5%,30.8%)" stop-opacity="1.0"></stop><stop offset="0.7777777777777777" stop-color="rgb(96.5%,48.4%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.7936507936507936" stop-color="rgb(95.9%,44.4%,27%)" stop-opacity="1.0"></stop><stop offset="0.8095238095238095" stop-color="rgb(94.5%,41%,26.7%)" stop-opacity="1.0"></stop><stop offset="0.8253968253968254" stop-color="rgb(92.6%,38.1%,27.5%)" stop-opacity="1.0"></stop><stop offset="0.8412698412698412" stop-color="rgb(90.7%,35.1%,28.2%)" stop-opacity="1.0"></stop><stop offset="0.857142857142857" stop-color="rgb(88.7%,32.2%,29%)" stop-opacity="1.0"></stop><stop offset="0.8730158730158731" stop-color="rgb(86.8%,29.3%,29.7%)" stop-opacity="1.0"></stop><stop offset="0.8888888888888887" stop-color="rgb(84.9%,26.4%,30.5%)" stop-opacity="1.0"></stop><stop offset="0.9047619047619047" stop-color="rgb(82.5%,23.2%,30.7%)" stop-opacity="1.0"></stop><stop offset="0.9206349206349205" stop-color="rgb(79.1%,19.4%,29.9%)" stop-opacity="1.0"></stop><stop offset="0.9365079365079365" stop-color="rgb(75.7%,15.6%,29.1%)" stop-opacity="1.0"></stop><stop offset="0.9523809523809524" stop-color="rgb(72.2%,11.8%,28.3%)" stop-opacity="1.0"></stop><stop offset="0.968253968253968" stop-color="rgb(68.8%,7.99%,27.5%)" stop-opacity="1.0"></stop><stop offset="0.9841269841269842" stop-color="rgb(65.4%,4.19%,26.7%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(62%,0.392%,25.9%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t65ac84945566403fbde250ab6db452b2);stroke:none;stroke-width:1.0" width="300.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t277b3cbdacfb42eeb38fdd2e6a7bcb86" transform="translate(50.0,350.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="300.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(300.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g transform="translate(150.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-40.992" y="10.265999999999998">Bottom to Top</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t0bc7679430fd47e8a04a748e9539dcd9"><clipPath id="tf4143dd4b29f4f50963db1fb37efc463"><rect height="20.0" width="300.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#tf4143dd4b29f4f50963db1fb37efc463)" transform="translate(150.0,50.0)rotate(90.0)"><g class="toyplot-color-Map" id="t1302f56aee9d43f9941a753794277a76"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t4b73338c25eb49188c53b853c6261815" x1="0.0" x2="300.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(36.9%,31%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.015873015873015872" stop-color="rgb(34.1%,34.5%,65.2%)" stop-opacity="1.0"></stop><stop offset="0.031746031746031744" stop-color="rgb(31.4%,38.1%,66.9%)" stop-opacity="1.0"></stop><stop offset="0.047619047619047616" stop-color="rgb(28.6%,41.6%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.06349206349206349" stop-color="rgb(25.9%,45.2%,70.3%)" stop-opacity="1.0"></stop><stop offset="0.07936507936507936" stop-color="rgb(23.2%,48.7%,71.9%)" stop-opacity="1.0"></stop><stop offset="0.09523809523809523" stop-color="rgb(20.4%,52.3%,73.6%)" stop-opacity="1.0"></stop><stop offset="0.11111111111111109" stop-color="rgb(21.9%,55.9%,73.1%)" stop-opacity="1.0"></stop><stop offset="0.12698412698412698" stop-color="rgb(25.1%,59.5%,71.6%)" stop-opacity="1.0"></stop><stop offset="0.14285714285714285" stop-color="rgb(28.3%,63.1%,70.1%)" stop-opacity="1.0"></stop><stop offset="0.15873015873015872" stop-color="rgb(31.6%,66.7%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.1746031746031746" stop-color="rgb(34.8%,70.3%,67.1%)" stop-opacity="1.0"></stop><stop offset="0.19047619047619047" stop-color="rgb(38.1%,73.9%,65.6%)" stop-opacity="1.0"></stop><stop offset="0.20634920634920634" stop-color="rgb(41.7%,76.8%,64.7%)" stop-opacity="1.0"></stop><stop offset="0.22222222222222218" stop-color="rgb(46%,78.4%,64.6%)" stop-opacity="1.0"></stop><stop offset="0.2380952380952381" stop-color="rgb(50.3%,80.1%,64.6%)" stop-opacity="1.0"></stop><stop offset="0.25396825396825395" stop-color="rgb(54.6%,81.8%,64.5%)" stop-opacity="1.0"></stop><stop offset="0.2698412698412698" stop-color="rgb(58.9%,83.5%,64.4%)" stop-opacity="1.0"></stop><stop offset="0.2857142857142857" stop-color="rgb(63.2%,85.2%,64.4%)" stop-opacity="1.0"></stop><stop offset="0.30158730158730157" stop-color="rgb(67.4%,86.8%,64.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746031744" stop-color="rgb(71.1%,88.3%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.3333333333333333" stop-color="rgb(74.8%,89.8%,62.7%)" stop-opacity="1.0"></stop><stop offset="0.3492063492063492" stop-color="rgb(78.4%,91.3%,62%)" stop-opacity="1.0"></stop><stop offset="0.36507936507936506" stop-color="rgb(82.1%,92.8%,61.3%)" stop-opacity="1.0"></stop><stop offset="0.38095238095238093" stop-color="rgb(85.8%,94.3%,60.5%)" stop-opacity="1.0"></stop><stop offset="0.3968253968253968" stop-color="rgb(89.5%,95.8%,59.8%)" stop-opacity="1.0"></stop><stop offset="0.4126984126984127" stop-color="rgb(91.4%,96.6%,61.5%)" stop-opacity="1.0"></stop><stop offset="0.4285714285714285" stop-color="rgb(93%,97.2%,64%)" stop-opacity="1.0"></stop><stop offset="0.44444444444444436" stop-color="rgb(94.6%,97.8%,66.4%)" stop-opacity="1.0"></stop><stop offset="0.46031746031746024" stop-color="rgb(96.1%,98.4%,68.8%)" stop-opacity="1.0"></stop><stop offset="0.4761904761904762" stop-color="rgb(97.7%,99.1%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.4920634920634921" stop-color="rgb(99.2%,99.7%,73.7%)" stop-opacity="1.0"></stop><stop offset="0.5079365079365079" stop-color="rgb(100%,99%,73.3%)" stop-opacity="1.0"></stop><stop offset="0.5238095238095237" stop-color="rgb(99.9%,97.1%,70%)" stop-opacity="1.0"></stop><stop offset="0.5396825396825397" stop-color="rgb(99.8%,95.2%,66.8%)" stop-opacity="1.0"></stop><stop offset="0.5555555555555556" stop-color="rgb(99.8%,93.2%,63.6%)" stop-opacity="1.0"></stop><stop offset="0.5714285714285714" stop-color="rgb(99.7%,91.3%,60.3%)" stop-opacity="1.0"></stop><stop offset="0.5873015873015872" stop-color="rgb(99.7%,89.4%,57.1%)" stop-opacity="1.0"></stop><stop offset="0.6031746031746031" stop-color="rgb(99.6%,87.2%,54%)" stop-opacity="1.0"></stop><stop offset="0.6190476190476191" stop-color="rgb(99.5%,84.1%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.6349206349206349" stop-color="rgb(99.5%,81%,48.8%)" stop-opacity="1.0"></stop><stop offset="0.6507936507936507" stop-color="rgb(99.4%,77.9%,46.1%)" stop-opacity="1.0"></stop><stop offset="0.6666666666666666" stop-color="rgb(99.3%,74.8%,43.5%)" stop-opacity="1.0"></stop><stop offset="0.6825396825396826" stop-color="rgb(99.3%,71.7%,40.9%)" stop-opacity="1.0"></stop><stop offset="0.6984126984126984" stop-color="rgb(99.2%,68.5%,38.3%)" stop-opacity="1.0"></stop><stop offset="0.7142857142857142" stop-color="rgb(98.7%,64.6%,36.4%)" stop-opacity="1.0"></stop><stop offset="0.7301587301587301" stop-color="rgb(98.2%,60.5%,34.5%)" stop-opacity="1.0"></stop><stop offset="0.746031746031746" stop-color="rgb(97.6%,56.5%,32.6%)" stop-opacity="1.0"></stop><stop offset="0.7619047619047619" stop-color="rgb(97%,52.5%,30.8%)" stop-opacity="1.0"></stop><stop offset="0.7777777777777777" stop-color="rgb(96.5%,48.4%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.7936507936507936" stop-color="rgb(95.9%,44.4%,27%)" stop-opacity="1.0"></stop><stop offset="0.8095238095238095" stop-color="rgb(94.5%,41%,26.7%)" stop-opacity="1.0"></stop><stop offset="0.8253968253968254" stop-color="rgb(92.6%,38.1%,27.5%)" stop-opacity="1.0"></stop><stop offset="0.8412698412698412" stop-color="rgb(90.7%,35.1%,28.2%)" stop-opacity="1.0"></stop><stop offset="0.857142857142857" stop-color="rgb(88.7%,32.2%,29%)" stop-opacity="1.0"></stop><stop offset="0.8730158730158731" stop-color="rgb(86.8%,29.3%,29.7%)" stop-opacity="1.0"></stop><stop offset="0.8888888888888887" stop-color="rgb(84.9%,26.4%,30.5%)" stop-opacity="1.0"></stop><stop offset="0.9047619047619047" stop-color="rgb(82.5%,23.2%,30.7%)" stop-opacity="1.0"></stop><stop offset="0.9206349206349205" stop-color="rgb(79.1%,19.4%,29.9%)" stop-opacity="1.0"></stop><stop offset="0.9365079365079365" stop-color="rgb(75.7%,15.6%,29.1%)" stop-opacity="1.0"></stop><stop offset="0.9523809523809524" stop-color="rgb(72.2%,11.8%,28.3%)" stop-opacity="1.0"></stop><stop offset="0.968253968253968" stop-color="rgb(68.8%,7.99%,27.5%)" stop-opacity="1.0"></stop><stop offset="0.9841269841269842" stop-color="rgb(65.4%,4.19%,26.7%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(62%,0.392%,25.9%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t4b73338c25eb49188c53b853c6261815);stroke:none;stroke-width:1.0" width="300.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t69d9211f4b164954a8026f0e121bb5c0" transform="translate(150.0,50.0)rotate(90.0)translate(0,10.0)"><line style="" x1="0" x2="300.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(300.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g transform="translate(150.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-40.992" y="10.265999999999998">Top to Bottom</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t0b74a347a00a46d4bd2db8f9add1e12c"><clipPath id="t1280b0dc8d904534a2e6b4a811708edc"><rect height="20.0" width="150.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#t1280b0dc8d904534a2e6b4a811708edc)" transform="translate(200.0,150.0)"><g class="toyplot-color-Map" id="t1302f56aee9d43f9941a753794277a76"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t26f8bcc825c84cbea47761a1167cf1cc" x1="0.0" x2="150.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(36.9%,31%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.015873015873015872" stop-color="rgb(34.1%,34.5%,65.2%)" stop-opacity="1.0"></stop><stop offset="0.031746031746031744" stop-color="rgb(31.4%,38.1%,66.9%)" stop-opacity="1.0"></stop><stop offset="0.047619047619047616" stop-color="rgb(28.6%,41.6%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.06349206349206349" stop-color="rgb(25.9%,45.2%,70.3%)" stop-opacity="1.0"></stop><stop offset="0.07936507936507936" stop-color="rgb(23.2%,48.7%,71.9%)" stop-opacity="1.0"></stop><stop offset="0.09523809523809523" stop-color="rgb(20.4%,52.3%,73.6%)" stop-opacity="1.0"></stop><stop offset="0.11111111111111109" stop-color="rgb(21.9%,55.9%,73.1%)" stop-opacity="1.0"></stop><stop offset="0.12698412698412698" stop-color="rgb(25.1%,59.5%,71.6%)" stop-opacity="1.0"></stop><stop offset="0.14285714285714285" stop-color="rgb(28.3%,63.1%,70.1%)" stop-opacity="1.0"></stop><stop offset="0.15873015873015872" stop-color="rgb(31.6%,66.7%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.1746031746031746" stop-color="rgb(34.8%,70.3%,67.1%)" stop-opacity="1.0"></stop><stop offset="0.19047619047619047" stop-color="rgb(38.1%,73.9%,65.6%)" stop-opacity="1.0"></stop><stop offset="0.20634920634920634" stop-color="rgb(41.7%,76.8%,64.7%)" stop-opacity="1.0"></stop><stop offset="0.22222222222222218" stop-color="rgb(46%,78.4%,64.6%)" stop-opacity="1.0"></stop><stop offset="0.2380952380952381" stop-color="rgb(50.3%,80.1%,64.6%)" stop-opacity="1.0"></stop><stop offset="0.25396825396825395" stop-color="rgb(54.6%,81.8%,64.5%)" stop-opacity="1.0"></stop><stop offset="0.2698412698412698" stop-color="rgb(58.9%,83.5%,64.4%)" stop-opacity="1.0"></stop><stop offset="0.2857142857142857" stop-color="rgb(63.2%,85.2%,64.4%)" stop-opacity="1.0"></stop><stop offset="0.30158730158730157" stop-color="rgb(67.4%,86.8%,64.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746031744" stop-color="rgb(71.1%,88.3%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.3333333333333333" stop-color="rgb(74.8%,89.8%,62.7%)" stop-opacity="1.0"></stop><stop offset="0.3492063492063492" stop-color="rgb(78.4%,91.3%,62%)" stop-opacity="1.0"></stop><stop offset="0.36507936507936506" stop-color="rgb(82.1%,92.8%,61.3%)" stop-opacity="1.0"></stop><stop offset="0.38095238095238093" stop-color="rgb(85.8%,94.3%,60.5%)" stop-opacity="1.0"></stop><stop offset="0.3968253968253968" stop-color="rgb(89.5%,95.8%,59.8%)" stop-opacity="1.0"></stop><stop offset="0.4126984126984127" stop-color="rgb(91.4%,96.6%,61.5%)" stop-opacity="1.0"></stop><stop offset="0.4285714285714285" stop-color="rgb(93%,97.2%,64%)" stop-opacity="1.0"></stop><stop offset="0.44444444444444436" stop-color="rgb(94.6%,97.8%,66.4%)" stop-opacity="1.0"></stop><stop offset="0.46031746031746024" stop-color="rgb(96.1%,98.4%,68.8%)" stop-opacity="1.0"></stop><stop offset="0.4761904761904762" stop-color="rgb(97.7%,99.1%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.4920634920634921" stop-color="rgb(99.2%,99.7%,73.7%)" stop-opacity="1.0"></stop><stop offset="0.5079365079365079" stop-color="rgb(100%,99%,73.3%)" stop-opacity="1.0"></stop><stop offset="0.5238095238095237" stop-color="rgb(99.9%,97.1%,70%)" stop-opacity="1.0"></stop><stop offset="0.5396825396825397" stop-color="rgb(99.8%,95.2%,66.8%)" stop-opacity="1.0"></stop><stop offset="0.5555555555555556" stop-color="rgb(99.8%,93.2%,63.6%)" stop-opacity="1.0"></stop><stop offset="0.5714285714285714" stop-color="rgb(99.7%,91.3%,60.3%)" stop-opacity="1.0"></stop><stop offset="0.5873015873015872" stop-color="rgb(99.7%,89.4%,57.1%)" stop-opacity="1.0"></stop><stop offset="0.6031746031746031" stop-color="rgb(99.6%,87.2%,54%)" stop-opacity="1.0"></stop><stop offset="0.6190476190476191" stop-color="rgb(99.5%,84.1%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.6349206349206349" stop-color="rgb(99.5%,81%,48.8%)" stop-opacity="1.0"></stop><stop offset="0.6507936507936507" stop-color="rgb(99.4%,77.9%,46.1%)" stop-opacity="1.0"></stop><stop offset="0.6666666666666666" stop-color="rgb(99.3%,74.8%,43.5%)" stop-opacity="1.0"></stop><stop offset="0.6825396825396826" stop-color="rgb(99.3%,71.7%,40.9%)" stop-opacity="1.0"></stop><stop offset="0.6984126984126984" stop-color="rgb(99.2%,68.5%,38.3%)" stop-opacity="1.0"></stop><stop offset="0.7142857142857142" stop-color="rgb(98.7%,64.6%,36.4%)" stop-opacity="1.0"></stop><stop offset="0.7301587301587301" stop-color="rgb(98.2%,60.5%,34.5%)" stop-opacity="1.0"></stop><stop offset="0.746031746031746" stop-color="rgb(97.6%,56.5%,32.6%)" stop-opacity="1.0"></stop><stop offset="0.7619047619047619" stop-color="rgb(97%,52.5%,30.8%)" stop-opacity="1.0"></stop><stop offset="0.7777777777777777" stop-color="rgb(96.5%,48.4%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.7936507936507936" stop-color="rgb(95.9%,44.4%,27%)" stop-opacity="1.0"></stop><stop offset="0.8095238095238095" stop-color="rgb(94.5%,41%,26.7%)" stop-opacity="1.0"></stop><stop offset="0.8253968253968254" stop-color="rgb(92.6%,38.1%,27.5%)" stop-opacity="1.0"></stop><stop offset="0.8412698412698412" stop-color="rgb(90.7%,35.1%,28.2%)" stop-opacity="1.0"></stop><stop offset="0.857142857142857" stop-color="rgb(88.7%,32.2%,29%)" stop-opacity="1.0"></stop><stop offset="0.8730158730158731" stop-color="rgb(86.8%,29.3%,29.7%)" stop-opacity="1.0"></stop><stop offset="0.8888888888888887" stop-color="rgb(84.9%,26.4%,30.5%)" stop-opacity="1.0"></stop><stop offset="0.9047619047619047" stop-color="rgb(82.5%,23.2%,30.7%)" stop-opacity="1.0"></stop><stop offset="0.9206349206349205" stop-color="rgb(79.1%,19.4%,29.9%)" stop-opacity="1.0"></stop><stop offset="0.9365079365079365" stop-color="rgb(75.7%,15.6%,29.1%)" stop-opacity="1.0"></stop><stop offset="0.9523809523809524" stop-color="rgb(72.2%,11.8%,28.3%)" stop-opacity="1.0"></stop><stop offset="0.968253968253968" stop-color="rgb(68.8%,7.99%,27.5%)" stop-opacity="1.0"></stop><stop offset="0.9841269841269842" stop-color="rgb(65.4%,4.19%,26.7%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(62%,0.392%,25.9%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t26f8bcc825c84cbea47761a1167cf1cc);stroke:none;stroke-width:1.0" width="150.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t3614fd2bfb3046d8b540def8ab6bf7fd" transform="translate(200.0,150.0)translate(0,10.0)"><line style="" x1="0" x2="150.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(75.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g transform="translate(75.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-35.327999999999996" y="10.265999999999998">Left to Right</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t6b716f8c43b04807b8679db8e206ee26"><clipPath id="tec7ee47ed0324fd6ae4df52b58b3cd0a"><rect height="20.0" width="150.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#tec7ee47ed0324fd6ae4df52b58b3cd0a)" transform="translate(350.0,250.0)rotate(180.0)"><g class="toyplot-color-Map" id="t1302f56aee9d43f9941a753794277a76"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t0f6ed44a84fe41ada8ecaf7b177ce09d" x1="0.0" x2="150.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(36.9%,31%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.015873015873015872" stop-color="rgb(34.1%,34.5%,65.2%)" stop-opacity="1.0"></stop><stop offset="0.031746031746031744" stop-color="rgb(31.4%,38.1%,66.9%)" stop-opacity="1.0"></stop><stop offset="0.047619047619047616" stop-color="rgb(28.6%,41.6%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.06349206349206349" stop-color="rgb(25.9%,45.2%,70.3%)" stop-opacity="1.0"></stop><stop offset="0.07936507936507936" stop-color="rgb(23.2%,48.7%,71.9%)" stop-opacity="1.0"></stop><stop offset="0.09523809523809523" stop-color="rgb(20.4%,52.3%,73.6%)" stop-opacity="1.0"></stop><stop offset="0.11111111111111109" stop-color="rgb(21.9%,55.9%,73.1%)" stop-opacity="1.0"></stop><stop offset="0.12698412698412698" stop-color="rgb(25.1%,59.5%,71.6%)" stop-opacity="1.0"></stop><stop offset="0.14285714285714285" stop-color="rgb(28.3%,63.1%,70.1%)" stop-opacity="1.0"></stop><stop offset="0.15873015873015872" stop-color="rgb(31.6%,66.7%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.1746031746031746" stop-color="rgb(34.8%,70.3%,67.1%)" stop-opacity="1.0"></stop><stop offset="0.19047619047619047" stop-color="rgb(38.1%,73.9%,65.6%)" stop-opacity="1.0"></stop><stop offset="0.20634920634920634" stop-color="rgb(41.7%,76.8%,64.7%)" stop-opacity="1.0"></stop><stop offset="0.22222222222222218" stop-color="rgb(46%,78.4%,64.6%)" stop-opacity="1.0"></stop><stop offset="0.2380952380952381" stop-color="rgb(50.3%,80.1%,64.6%)" stop-opacity="1.0"></stop><stop offset="0.25396825396825395" stop-color="rgb(54.6%,81.8%,64.5%)" stop-opacity="1.0"></stop><stop offset="0.2698412698412698" stop-color="rgb(58.9%,83.5%,64.4%)" stop-opacity="1.0"></stop><stop offset="0.2857142857142857" stop-color="rgb(63.2%,85.2%,64.4%)" stop-opacity="1.0"></stop><stop offset="0.30158730158730157" stop-color="rgb(67.4%,86.8%,64.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746031744" stop-color="rgb(71.1%,88.3%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.3333333333333333" stop-color="rgb(74.8%,89.8%,62.7%)" stop-opacity="1.0"></stop><stop offset="0.3492063492063492" stop-color="rgb(78.4%,91.3%,62%)" stop-opacity="1.0"></stop><stop offset="0.36507936507936506" stop-color="rgb(82.1%,92.8%,61.3%)" stop-opacity="1.0"></stop><stop offset="0.38095238095238093" stop-color="rgb(85.8%,94.3%,60.5%)" stop-opacity="1.0"></stop><stop offset="0.3968253968253968" stop-color="rgb(89.5%,95.8%,59.8%)" stop-opacity="1.0"></stop><stop offset="0.4126984126984127" stop-color="rgb(91.4%,96.6%,61.5%)" stop-opacity="1.0"></stop><stop offset="0.4285714285714285" stop-color="rgb(93%,97.2%,64%)" stop-opacity="1.0"></stop><stop offset="0.44444444444444436" stop-color="rgb(94.6%,97.8%,66.4%)" stop-opacity="1.0"></stop><stop offset="0.46031746031746024" stop-color="rgb(96.1%,98.4%,68.8%)" stop-opacity="1.0"></stop><stop offset="0.4761904761904762" stop-color="rgb(97.7%,99.1%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.4920634920634921" stop-color="rgb(99.2%,99.7%,73.7%)" stop-opacity="1.0"></stop><stop offset="0.5079365079365079" stop-color="rgb(100%,99%,73.3%)" stop-opacity="1.0"></stop><stop offset="0.5238095238095237" stop-color="rgb(99.9%,97.1%,70%)" stop-opacity="1.0"></stop><stop offset="0.5396825396825397" stop-color="rgb(99.8%,95.2%,66.8%)" stop-opacity="1.0"></stop><stop offset="0.5555555555555556" stop-color="rgb(99.8%,93.2%,63.6%)" stop-opacity="1.0"></stop><stop offset="0.5714285714285714" stop-color="rgb(99.7%,91.3%,60.3%)" stop-opacity="1.0"></stop><stop offset="0.5873015873015872" stop-color="rgb(99.7%,89.4%,57.1%)" stop-opacity="1.0"></stop><stop offset="0.6031746031746031" stop-color="rgb(99.6%,87.2%,54%)" stop-opacity="1.0"></stop><stop offset="0.6190476190476191" stop-color="rgb(99.5%,84.1%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.6349206349206349" stop-color="rgb(99.5%,81%,48.8%)" stop-opacity="1.0"></stop><stop offset="0.6507936507936507" stop-color="rgb(99.4%,77.9%,46.1%)" stop-opacity="1.0"></stop><stop offset="0.6666666666666666" stop-color="rgb(99.3%,74.8%,43.5%)" stop-opacity="1.0"></stop><stop offset="0.6825396825396826" stop-color="rgb(99.3%,71.7%,40.9%)" stop-opacity="1.0"></stop><stop offset="0.6984126984126984" stop-color="rgb(99.2%,68.5%,38.3%)" stop-opacity="1.0"></stop><stop offset="0.7142857142857142" stop-color="rgb(98.7%,64.6%,36.4%)" stop-opacity="1.0"></stop><stop offset="0.7301587301587301" stop-color="rgb(98.2%,60.5%,34.5%)" stop-opacity="1.0"></stop><stop offset="0.746031746031746" stop-color="rgb(97.6%,56.5%,32.6%)" stop-opacity="1.0"></stop><stop offset="0.7619047619047619" stop-color="rgb(97%,52.5%,30.8%)" stop-opacity="1.0"></stop><stop offset="0.7777777777777777" stop-color="rgb(96.5%,48.4%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.7936507936507936" stop-color="rgb(95.9%,44.4%,27%)" stop-opacity="1.0"></stop><stop offset="0.8095238095238095" stop-color="rgb(94.5%,41%,26.7%)" stop-opacity="1.0"></stop><stop offset="0.8253968253968254" stop-color="rgb(92.6%,38.1%,27.5%)" stop-opacity="1.0"></stop><stop offset="0.8412698412698412" stop-color="rgb(90.7%,35.1%,28.2%)" stop-opacity="1.0"></stop><stop offset="0.857142857142857" stop-color="rgb(88.7%,32.2%,29%)" stop-opacity="1.0"></stop><stop offset="0.8730158730158731" stop-color="rgb(86.8%,29.3%,29.7%)" stop-opacity="1.0"></stop><stop offset="0.8888888888888887" stop-color="rgb(84.9%,26.4%,30.5%)" stop-opacity="1.0"></stop><stop offset="0.9047619047619047" stop-color="rgb(82.5%,23.2%,30.7%)" stop-opacity="1.0"></stop><stop offset="0.9206349206349205" stop-color="rgb(79.1%,19.4%,29.9%)" stop-opacity="1.0"></stop><stop offset="0.9365079365079365" stop-color="rgb(75.7%,15.6%,29.1%)" stop-opacity="1.0"></stop><stop offset="0.9523809523809524" stop-color="rgb(72.2%,11.8%,28.3%)" stop-opacity="1.0"></stop><stop offset="0.968253968253968" stop-color="rgb(68.8%,7.99%,27.5%)" stop-opacity="1.0"></stop><stop offset="0.9841269841269842" stop-color="rgb(65.4%,4.19%,26.7%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(62%,0.392%,25.9%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t0f6ed44a84fe41ada8ecaf7b177ce09d);stroke:none;stroke-width:1.0" width="150.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t8a22195c2cba46969fd208615e51ffef" transform="translate(350.0,250.0)rotate(180.0)translate(0,10.0)"><line style="" x1="0" x2="150.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(75.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g transform="translate(75.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-35.327999999999996" y="10.265999999999998">Right to Left</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/canvas/id"] = "t82357e20ab2a47d4b899f3678ca34b55";
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
            })(modules["toyplot.coordinates.Axis"],"t277b3cbdacfb42eeb38fdd2e6a7bcb86",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 300.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t69d9211f4b164954a8026f0e121bb5c0",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 300.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t3614fd2bfb3046d8b540def8ab6bf7fd",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 150.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t8a22195c2cba46969fd208615e51ffef",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 150.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Canvas Legends
--------------

Last-but-not-least, Toyplot provides basic support for graphical
legends:

.. code:: python

    observations = numpy.random.power(2, size=(50, 50))
    
    x = numpy.arange(len(observations))
    
    boundaries = numpy.column_stack(
        (numpy.min(observations, axis=1),
         numpy.percentile(observations, 25, axis=1),
         numpy.percentile(observations, 50, axis=1),
         numpy.percentile(observations, 75, axis=1),
         numpy.max(observations, axis=1)))
    
    color = ["blue", "blue", "red", "red"]
    opacity = [0.1, 0.2, 0.2, 0.1]
    
    canvas = toyplot.Canvas(800, 400)
    axes = canvas.cartesian(grid=(1,5,0,1,0,4))
    fill = axes.fill(x, boundaries, color=color, opacity=opacity)
    mean = axes.plot(x, numpy.mean(observations, axis=1), color="blue")
    
    canvas.legend([
        ("Mean", mean),
        ("Quartiles", fill),
        ],
        corner=("right", 100, 100, 50),
        );




.. raw:: html

    <div class="toyplot" id="t9b31df7bae56406a99474bc1a0f79c96" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t858a75fceac64adfa1fe931f3e54f2fb" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 800.0 400.0" width="800.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t5f3060fdd94c40fd92c77b7766b3b7fd"><clipPath id="t6a924c5164514aea8f4699ba0c714eb6"><rect height="320.0" width="560.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t6a924c5164514aea8f4699ba0c714eb6)"><g class="toyplot-mark-FillBoundaries" id="t77481cfde5ab4a8190dac92b448dcf14" style="stroke:none"><polygon points="50.0,310.529681051571 60.8,338.2127767728843 71.6,311.5355328853379 82.4,322.17043210615105 93.2,299.81448759025807 104.0,327.32054709954076 114.8,309.40794168444785 125.60000000000001,325.92889561071263 136.4,301.59217273025746 147.2,337.668277650029 158.0,299.90161002270065 168.8,308.77621001463456 179.6,296.5515581918126 190.4,315.32993678759516 201.20000000000002,329.77175301438626 212.0,307.0096996542961 222.8,345.47755682451844 233.60000000000002,318.59512358790397 244.4,326.8581107935275 255.2,278.87555671117883 266.0,323.8268705884767 276.8,330.85065229962754 287.6,336.0026612016017 298.40000000000003,331.27306243526573 309.2,295.4168002090314 320.0,295.03772432933994 330.8,304.8677184743537 341.6,335.6064233154388 352.40000000000003,326.83055695896473 363.2,329.94017522326396 374.0,321.6121572448151 384.8,308.7756606923613 395.6,300.72983043200446 406.40000000000003,321.0013027092842 417.20000000000005,309.304923774071 428.0,308.49798899483767 438.8,348.0308188594836 449.6,310.558742504479 460.4,307.7402987506902 471.2,295.76300155064314 482.0,284.7102771688584 492.79999999999995,275.3166503109411 503.59999999999997,290.2640011701637 514.4,328.0829003038271 525.2,321.6563642329914 536.0,294.2297217685454 546.8000000000001,320.28285540240495 557.6,305.47084318156624 568.4,279.59350772653613 579.2,339.89354855395294 579.2,177.05982692073246 568.4,201.824533390177 557.6,228.7825261191285 546.8000000000001,176.84007381383924 536.0,199.7288409939153 525.2,184.8834379203086 514.4,208.54701216011208 503.59999999999997,202.76496591342072 492.79999999999995,190.16132728156785 482.0,162.55399241167672 471.2,194.56945380757668 460.4,229.90878304398768 449.6,186.84959820046427 438.8,215.5383739679347 428.0,219.10523540355584 417.20000000000005,187.9842790356855 406.40000000000003,219.97172833448474 395.6,190.88017296052618 384.8,202.8604839324773 374.0,151.41944680044713 363.2,207.89318183264487 352.40000000000003,187.8578033739974 341.6,184.77875137982295 330.8,170.54211777961092 320.0,170.67416705214276 309.2,226.61981088765177 298.40000000000003,217.12879767584374 287.6,240.30611862472537 276.8,238.35762112152938 266.0,188.66478780682553 255.2,197.0406404094242 244.4,215.05635258266966 233.60000000000002,222.22761081943116 222.8,210.32526377147644 212.0,217.27390304117682 201.20000000000002,217.206078716216 190.4,241.27848064499705 179.6,205.43639938205806 168.8,182.49110182672266 158.0,198.47441917051052 147.2,253.4240868528994 136.4,205.45636907396658 125.60000000000001,223.52641820044244 114.8,200.03385763417586 104.0,187.00994987042787 93.2,155.54598387845036 82.4,211.8253325570285 71.6,185.5870393105152 60.8,169.57578085147924 50.0,225.0809880305612" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.1;stroke:none"></polygon><polygon points="50.0,225.0809880305612 60.8,169.57578085147924 71.6,185.5870393105152 82.4,211.8253325570285 93.2,155.54598387845036 104.0,187.00994987042787 114.8,200.03385763417586 125.60000000000001,223.52641820044244 136.4,205.45636907396658 147.2,253.4240868528994 158.0,198.47441917051052 168.8,182.49110182672266 179.6,205.43639938205806 190.4,241.27848064499705 201.20000000000002,217.206078716216 212.0,217.27390304117682 222.8,210.32526377147644 233.60000000000002,222.22761081943116 244.4,215.05635258266966 255.2,197.0406404094242 266.0,188.66478780682553 276.8,238.35762112152938 287.6,240.30611862472537 298.40000000000003,217.12879767584374 309.2,226.61981088765177 320.0,170.67416705214276 330.8,170.54211777961092 341.6,184.77875137982295 352.40000000000003,187.8578033739974 363.2,207.89318183264487 374.0,151.41944680044713 384.8,202.8604839324773 395.6,190.88017296052618 406.40000000000003,219.97172833448474 417.20000000000005,187.9842790356855 428.0,219.10523540355584 438.8,215.5383739679347 449.6,186.84959820046427 460.4,229.90878304398768 471.2,194.56945380757668 482.0,162.55399241167672 492.79999999999995,190.16132728156785 503.59999999999997,202.76496591342072 514.4,208.54701216011208 525.2,184.8834379203086 536.0,199.7288409939153 546.8000000000001,176.84007381383924 557.6,228.7825261191285 568.4,201.824533390177 579.2,177.05982692073246 579.2,128.48497627556466 568.4,157.64044481270375 557.6,121.69759968390767 546.8000000000001,138.93886754435746 536.0,142.56214970318112 525.2,125.18499008443452 514.4,138.61850469919125 503.59999999999997,135.122525766884 492.79999999999995,148.24083868664303 482.0,121.57645881502913 471.2,119.42300581145722 460.4,133.68984404213984 449.6,122.98351294150788 438.8,160.3757240017967 428.0,153.34269168978273 417.20000000000005,122.93869975953083 406.40000000000003,144.34883140701453 395.6,131.18126715388013 384.8,161.0969219163245 374.0,117.84161019250075 363.2,132.41708933609533 352.40000000000003,126.87833060627108 341.6,128.9261177741942 330.8,99.19260465062683 320.0,121.64234098569193 309.2,150.65044425727993 298.40000000000003,112.24237881456817 287.6,171.93232772771103 276.8,141.25263443105564 266.0,131.50013489728835 255.2,142.61747646863338 244.4,131.8023045138103 233.60000000000002,141.6339874677841 222.8,138.51970410763704 212.0,145.34409852546975 201.20000000000002,127.2381706333554 190.4,163.21969573239014 179.6,139.92062057588038 168.8,124.60747233381954 158.0,145.71338218863394 147.2,153.6436100615142 136.4,140.99194501162347 125.60000000000001,141.97697973081202 114.8,155.35973589535524 104.0,126.02934940940057 93.2,116.7430320382328 82.4,161.3282891709094 71.6,117.20755508330123 60.8,117.33062760385113 50.0,152.31565851979357" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.2;stroke:none"></polygon><polygon points="50.0,152.31565851979357 60.8,117.33062760385113 71.6,117.20755508330123 82.4,161.3282891709094 93.2,116.7430320382328 104.0,126.02934940940057 114.8,155.35973589535524 125.60000000000001,141.97697973081202 136.4,140.99194501162347 147.2,153.6436100615142 158.0,145.71338218863394 168.8,124.60747233381954 179.6,139.92062057588038 190.4,163.21969573239014 201.20000000000002,127.2381706333554 212.0,145.34409852546975 222.8,138.51970410763704 233.60000000000002,141.6339874677841 244.4,131.8023045138103 255.2,142.61747646863338 266.0,131.50013489728835 276.8,141.25263443105564 287.6,171.93232772771103 298.40000000000003,112.24237881456817 309.2,150.65044425727993 320.0,121.64234098569193 330.8,99.19260465062683 341.6,128.9261177741942 352.40000000000003,126.87833060627108 363.2,132.41708933609533 374.0,117.84161019250075 384.8,161.0969219163245 395.6,131.18126715388013 406.40000000000003,144.34883140701453 417.20000000000005,122.93869975953083 428.0,153.34269168978273 438.8,160.3757240017967 449.6,122.98351294150788 460.4,133.68984404213984 471.2,119.42300581145722 482.0,121.57645881502913 492.79999999999995,148.24083868664303 503.59999999999997,135.122525766884 514.4,138.61850469919125 525.2,125.18499008443452 536.0,142.56214970318112 546.8000000000001,138.93886754435746 557.6,121.69759968390767 568.4,157.64044481270375 579.2,128.48497627556466 579.2,89.07434048129831 568.4,119.91146738650599 557.6,90.95089187136779 546.8000000000001,87.03647833853981 536.0,70.62083460135526 525.2,89.94760731602142 514.4,96.84776480681464 503.59999999999997,95.27865350602966 492.79999999999995,101.36480336145445 482.0,83.38948046286274 471.2,87.21052919083206 460.4,87.99225761433067 449.6,87.4575595980572 438.8,116.09269020114877 428.0,97.81577284746879 417.20000000000005,85.12032942065 406.40000000000003,91.9250392388605 395.6,71.27700749361836 384.8,107.49471354764972 374.0,81.81345445890989 363.2,76.0431456113538 352.40000000000003,96.71535825791472 341.6,92.32914161947907 330.8,78.43467473800706 320.0,82.98416629358147 309.2,108.04010252234025 298.40000000000003,69.64997447003365 287.6,102.16159230534217 276.8,108.21046552975855 266.0,85.1999384796261 255.2,87.49776189938683 244.4,85.54003932554744 233.60000000000002,112.93489025261817 222.8,87.91368415213498 212.0,113.52188990105878 201.20000000000002,74.71179957519047 190.4,108.85294059319446 179.6,89.52696751091108 168.8,91.09453043342535 158.0,87.66294791785907 147.2,110.99259765503312 136.4,91.90076154285495 125.60000000000001,91.66065754263016 114.8,82.24409417811745 104.0,85.34842641054523 93.2,81.10707597872506 82.4,107.10631628950067 71.6,74.12681415256674 60.8,81.00884958050818 50.0,101.45325820175026" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.2;stroke:none"></polygon><polygon points="50.0,101.45325820175026 60.8,81.00884958050818 71.6,74.12681415256674 82.4,107.10631628950067 93.2,81.10707597872506 104.0,85.34842641054523 114.8,82.24409417811745 125.60000000000001,91.66065754263016 136.4,91.90076154285495 147.2,110.99259765503312 158.0,87.66294791785907 168.8,91.09453043342535 179.6,89.52696751091108 190.4,108.85294059319446 201.20000000000002,74.71179957519047 212.0,113.52188990105878 222.8,87.91368415213498 233.60000000000002,112.93489025261817 244.4,85.54003932554744 255.2,87.49776189938683 266.0,85.1999384796261 276.8,108.21046552975855 287.6,102.16159230534217 298.40000000000003,69.64997447003365 309.2,108.04010252234025 320.0,82.98416629358147 330.8,78.43467473800706 341.6,92.32914161947907 352.40000000000003,96.71535825791472 363.2,76.0431456113538 374.0,81.81345445890989 384.8,107.49471354764972 395.6,71.27700749361836 406.40000000000003,91.9250392388605 417.20000000000005,85.12032942065 428.0,97.81577284746879 438.8,116.09269020114877 449.6,87.4575595980572 460.4,87.99225761433067 471.2,87.21052919083206 482.0,83.38948046286274 492.79999999999995,101.36480336145445 503.59999999999997,95.27865350602966 514.4,96.84776480681464 525.2,89.94760731602142 536.0,70.62083460135526 546.8000000000001,87.03647833853981 557.6,90.95089187136779 568.4,119.91146738650599 579.2,89.07434048129831 579.2,53.422623380005355 568.4,60.773310556639636 557.6,55.86514051499483 546.8000000000001,54.99185020635411 536.0,52.17555176850165 525.2,52.87103767053741 514.4,58.49653007299324 503.59999999999997,50.34092995630386 492.79999999999995,52.61093886947391 482.0,54.25670068913006 471.2,50.61868156885288 460.4,51.18143928545789 449.6,51.38534021504325 438.8,57.57670828613125 428.0,51.131687873893924 417.20000000000005,50.44908361918985 406.40000000000003,52.945568324263824 395.6,52.61846968920639 384.8,52.696731607617 374.0,50.58929481883607 363.2,50.91739872223255 352.40000000000003,62.94762161726808 341.6,50.84388184633239 330.8,51.64001927826537 320.0,53.49434024853362 309.2,54.13571557381628 298.40000000000003,51.49187993120317 287.6,56.21466240240344 276.8,58.64348328426734 266.0,50.36728250280489 255.2,55.867768014243865 244.4,53.308438233906315 233.60000000000002,50.289832627880436 222.8,55.494434598347034 212.0,51.63919956512344 201.20000000000002,51.542271963665065 190.4,50.97002042212052 179.6,53.917202462575716 168.8,50.607689328977216 158.0,60.353855635465926 147.2,56.56229171450048 136.4,53.975116705867364 125.60000000000001,52.65755334421287 114.8,50.329103317891 104.0,52.02499346636848 93.2,50.205456449904084 82.4,52.61372972894763 71.6,50.00544148255365 60.8,54.382062228934636 50.0,59.12956046639162" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.1;stroke:none"></polygon></g><g class="toyplot-mark-Plot" id="t072803de7e584d069bcf4d7af355e571" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 163.49667814173617 L 60.8 137.71154754170277 L 71.6 139.90158895299604 L 82.4 159.84360929778228 L 93.2 126.70521032892651 L 104.0 147.6983684190605 L 114.8 148.88918754095593 L 125.60000000000001 157.61645449104185 L 136.4 151.27347123236322 L 147.2 177.8778114194378 L 158.0 154.6504555649364 L 168.8 137.27643129769862 L 179.6 151.1281099128105 L 190.4 173.7526114207107 L 201.20000000000002 147.9796540490893 L 212.0 162.69420943878464 L 222.8 152.75929313579127 L 233.60000000000002 167.35176858608597 L 244.4 149.78294773342697 L 255.2 148.66843657840053 L 266.0 149.54757028800805 L 276.8 167.29987457499024 L 287.6 175.23121548310593 L 298.40000000000003 147.42507457048487 L 309.2 161.6073086181612 L 320.0 137.8716536946415 L 330.8 132.2977597610217 L 341.6 146.1821641348436 L 352.40000000000003 146.38168973117547 L 363.2 149.79202673056622 L 374.0 128.48147974635066 L 384.8 161.24664087699065 L 395.6 140.0481215484159 L 406.40000000000003 152.3127059357053 L 417.20000000000005 145.72459407416423 L 428.0 161.94524974279014 L 438.8 171.5237978525154 L 449.6 142.18109227494182 L 460.4 157.03757114504492 L 471.2 140.47878190760736 L 482.0 135.97458774882278 L 492.79999999999995 148.43991202910274 L 503.59999999999997 151.64646140177766 L 514.4 157.5971875160467 L 525.2 140.1290515817769 L 536.0 145.17663656436693 L 546.8000000000001 145.1463833510219 L 557.6 154.56715103662162 L 568.4 162.22660535858168 L 579.2 140.87554354633366" style="stroke:rgb(0%,0%,100%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="td39cfc911f324a688a23f0b1342b29fc" transform="translate(50.0,350.0)translate(0,10.0)"><line style="" x1="0" x2="529.2" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(108.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(216.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g><g transform="translate(324.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">30</text></g><g transform="translate(432.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">40</text></g><g transform="translate(540.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tdcb806f04edc4949b2d2cf8ef1a26f54" transform="translate(50.0,350.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="1.9691811405164148" x2="299.99455851744636" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.0</text></g><g transform="translate(150.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.5</text></g><g transform="translate(300.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Table" id="tc21be0b83874426eb012f0fc822512e6"><g transform="translate(645.0,187.5)"><g style="fill:rgb(0%,0%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0;stroke-width:2" transform="translate(-5.55, -4.440892098500626e-16)"><line transform="rotate(45)" y1="-5.55" y2="5.55"></line></g></g><g transform="translate(655.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">Mean</text></g><g transform="translate(645.0,212.5)"><g style="fill:rgb(0%,0%,100%);fill-opacity:0.1;stroke:none" transform="translate(-48.858000000000004, -4.440892098500626e-16)"><rect height="11.1" width="11.1" x="-5.55" y="-5.55"></rect></g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-43.308" y="3.066"> </text><g style="fill:rgb(0%,0%,100%);fill-opacity:0.2;stroke:none" transform="translate(-34.422, -4.440892098500626e-16)"><rect height="11.1" width="11.1" x="-5.55" y="-5.55"></rect></g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-28.872" y="3.066"> </text><g style="fill:rgb(100%,0%,0%);fill-opacity:0.2;stroke:none" transform="translate(-19.986, -4.440892098500626e-16)"><rect height="11.1" width="11.1" x="-5.55" y="-5.55"></rect></g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-14.436000000000002" y="3.066"> </text><g style="fill:rgb(100%,0%,0%);fill-opacity:0.1;stroke:none" transform="translate(-5.550000000000002, -4.440892098500626e-16)"><rect height="11.1" width="11.1" x="-5.55" y="-5.55"></rect></g></g><g transform="translate(655.0,212.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">Quartiles</text></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t9b31df7bae56406a99474bc1a0f79c96";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t858a75fceac64adfa1fe931f3e54f2fb";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t77481cfde5ab4a8190dac92b448dcf14","data","fill data",["x", "y0", "y1", "y2", "y3", "y4"],[[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0], [0.13156772982809672, 0.039290744090385535, 0.12821489038220688, 0.09276522631282974, 0.16728504136580646, 0.07559817633486413, 0.13530686105184053, 0.08023701463095784, 0.16135942423247518, 0.041105741166569905, 0.16699463325766464, 0.13741263328455153, 0.17816147269395805, 0.11556687737468288, 0.06742748995204582, 0.14330100115234617, 0.015074810584938663, 0.10468292137365344, 0.0771396306882418, 0.23708147762940388, 0.08724376470507762, 0.06383115900124144, 0.046657795994660925, 0.06242312521578101, 0.1819439993032287, 0.18320758556886693, 0.1504409384188211, 0.04797858894853724, 0.07723147680345079, 0.06686608258912034, 0.09462614251728298, 0.13741446435879556, 0.16423389855998521, 0.09666232430238615, 0.1356502540864299, 0.13834003668387446, 0.006563937135054716, 0.1314708583184031, 0.14086567083103252, 0.18078999483118946, 0.21763240943713863, 0.24894449896352963, 0.19911999609945458, 0.07305699898724302, 0.09447878589002875, 0.18590092743818212, 0.0990571486586501, 0.1484305227281125, 0.2346883075782129, 0.0336881714868235], [0.41639670656479594, 0.6014140638284026, 0.5480432022982826, 0.46058222480990507, 0.6481800537384989, 0.5433001670985738, 0.4998871412194138, 0.42157860599852515, 0.481812103086778, 0.3219197104903353, 0.5050852694316316, 0.5583629939109245, 0.48187866872647306, 0.3624050645166765, 0.4426464042792799, 0.44242032319607727, 0.46558245409507865, 0.4259079639352295, 0.4498121580577679, 0.5098645319685859, 0.5377840406439148, 0.37214126292823546, 0.3656462712509155, 0.4429040077471876, 0.41126729704116083, 0.5977527764928574, 0.5981929407346303, 0.5507374954005901, 0.5404739887533421, 0.4736893938911837, 0.6619351773318429, 0.49046505355840897, 0.5303994234649128, 0.4334275722183842, 0.5400524032143817, 0.43631588198814714, 0.4482054201068843, 0.5438346726651191, 0.4003040565200411, 0.5181018206414111, 0.6248200252944109, 0.5327955757281072, 0.4907834469552642, 0.47150995946629304, 0.550388540265638, 0.5009038633536156, 0.5771997539538691, 0.40405824626957165, 0.49391822203274327, 0.5764672435975585], [0.6589478049340214, 0.7755645746538296, 0.7759748163889959, 0.6289057027636353, 0.777523226539224, 0.7465688353019981, 0.6488008803488159, 0.69341006756396, 0.6966935166279218, 0.6545212997949527, 0.6809553927045535, 0.7513084255539348, 0.7002645980803988, 0.6226010142253663, 0.7425394312221487, 0.6821863382484341, 0.7049343196412099, 0.6945533751073864, 0.7273256516206323, 0.6912750784378887, 0.7283328836757055, 0.6958245518964812, 0.5935589075742966, 0.7925254039514394, 0.6644985191424002, 0.7611921967143602, 0.8360246511645772, 0.736912940752686, 0.7437388979790964, 0.7252763688796822, 0.7738612993583308, 0.6296769269455851, 0.7293957761537329, 0.6855038953099516, 0.7568710008015639, 0.6555243610340576, 0.632080919994011, 0.7567216235283071, 0.7210338531928672, 0.7685899806284759, 0.7614118039499029, 0.6725305377111899, 0.71625824744372, 0.7046049843360291, 0.7493833663852183, 0.6914595009893962, 0.7035371081854751, 0.7610080010536411, 0.6411985172909875, 0.7383834124147844], [0.8284891393274991, 0.8966371680649727, 0.9195772861581109, 0.8096456123683311, 0.8963097467375831, 0.8821719119648492, 0.8925196860729419, 0.8611311415245662, 0.8603307948571501, 0.7966913411498896, 0.8744568402738031, 0.8630182318885822, 0.8682434416302964, 0.8038235313560185, 0.9176273347493651, 0.7882603669964707, 0.8736210528262167, 0.7902170324912727, 0.8815332022481752, 0.8750074603353772, 0.8826668717345797, 0.8059651149008048, 0.8261280256488595, 0.9345000850998878, 0.8065329915921992, 0.8900527790213951, 0.9052177508733098, 0.8589028612684031, 0.8442821391402843, 0.9131895146288207, 0.8939551518036337, 0.8083509548411676, 0.9290766416879388, 0.8602498692037983, 0.8829322352645, 0.8406140905084374, 0.7796910326628375, 0.875141468006476, 0.8733591412855645, 0.8759649026972265, 0.8887017317904575, 0.8287839887951518, 0.8490711549799012, 0.8438407839772846, 0.8668413089465953, 0.9312638846621492, 0.8765450722048673, 0.8634970270954407, 0.7669617753783133, 0.8697521983956723], [0.9695681317786946, 0.9853931259035512, 0.9999818617248212, 0.9912875675701746, 0.9993151451669864, 0.9932500217787718, 0.9989029889403633, 0.9911414888526238, 0.9867496109804421, 0.9781256942849984, 0.9654871478817802, 0.9979743689034093, 0.9869426584580809, 0.9967665985929316, 0.9948590934544498, 0.9945360014495885, 0.9816852180055099, 0.9990338912403985, 0.9889718725536456, 0.9804407732858538, 0.9987757249906504, 0.9711883890524422, 0.9792844586586552, 0.9950270668959894, 0.9862142814206124, 0.9883521991715546, 0.9945332690724488, 0.9971870605122254, 0.9568412612757731, 0.9969420042592249, 0.9980356839372131, 0.9910108946412767, 0.9912717677026454, 0.9901814389191206, 0.9985030546027005, 0.9962277070870202, 0.9747443057128958, 0.9953821992831892, 0.9960618690484737, 0.9979377281038238, 0.9858109977028998, 0.991296870435087, 0.9988635668123205, 0.9716782330900225, 0.990429874431542, 0.9927481607716612, 0.983360499312153, 0.9804495316166839, 0.9640889648112012, 0.9885912553999822]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t072803de7e584d069bcf4d7af355e571","data","plot data",["x", "y0"],[[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0], [0.6216777395275461, 0.7076281748609907, 0.7003280368233465, 0.6338546356740591, 0.7443159655702449, 0.674338771936465, 0.6703693748634802, 0.6412784850298605, 0.6624217625587893, 0.573740628601874, 0.6511651481168786, 0.7090785623410046, 0.6629063002906317, 0.5874912952642977, 0.6734011531697023, 0.6243526352040513, 0.6574690228806958, 0.6088274380463801, 0.6673901742219102, 0.6711052114053315, 0.6681747657066398, 0.6090004180833659, 0.5825626150563136, 0.6752497514317171, 0.6279756379394626, 0.7070944876845283, 0.7256741341299277, 0.679392786217188, 0.6787277008960818, 0.6673599108981126, 0.7383950675121644, 0.6291778637433645, 0.6998395948386137, 0.6589576468809824, 0.6809180197527859, 0.6268491675240329, 0.5949206738249487, 0.6927296924168607, 0.6432080961831835, 0.6984040603079754, 0.7134180408372574, 0.6718669599029908, 0.6611784619940745, 0.6413427082798444, 0.6995698280607436, 0.6827445447854436, 0.682845388829927, 0.6514428298779279, 0.6259113154713943, 0.6970815215122211]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"td39cfc911f324a688a23f0b1342b29fc",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tdcb806f04edc4949b2d2cf8ef1a26f54",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 300.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


The call to :func:`toyplot.canvas.Canvas.legend` always includes an
explicit list of entries to add to the legend, plus a
:ref:`canvas-layout` specification of where the layout should appear
on the canvas. Currently, each entry to be displayed in a legend must be
one of the following:

-  A (label, mark) tuple, which will get its appearance from the mark,
   or:
-  A (label, marker) tuple, which can be used to specify an arbitrary
   :ref:`Marker<Markers>`.

Of course, ``label`` is the human-readable text to be displayed next to
an item in the legend, while ``mark`` is a mark that has been added to
the canvas. However, not all marks can map cleanly to a single entry in
the legend - note in the example above that the fill mark added multiple
markers to the "Quartiles" entry in the legend, one for each data
series. While the interpretation is reasonably clear in this case, there
will be occasions when there isn't a sensible one-to-one mapping between
a mark and an entry in the legend. For example, the meaning of multiple
series may not be clear, or you may be plotting categorical information
using custom markers in a line or scatter plot. In these cases use the
second form of legend entry to specify as many explicit :ref:`Markers`
as needed.

There are some subtleties here worth noting, many of which are driven by
Toyplot's deliberate embrace of the philosophy that *explicit is better
than implicit*:

-  You can have as many or as few legends on your canvas as you like.
-  Callers explicitly specify the order and contents of each legend.
-  There is no relationship between axes and legends - you can combine
   marks from multiple axes in a single legend.

Here's an example with all these ideas at work. Note that the legend
overlaps two coordinate systems and its first entry derives directly
from the mark in the first coordinate system, while the second and third
entries document the individual series in the second mark:

.. code:: python

    x = numpy.linspace(0, 1)
    y1 = (1 - x) ** 2
    y2 = numpy.column_stack((1 - (x ** 2), x ** 2))
    
    canvas = toyplot.Canvas(width=600, height=300)
    m1 = canvas.cartesian(grid=(1,2,0), margin=25).scatterplot(x, y1, marker="o", color="rgb(255,0,0)")
    m2 = canvas.cartesian(grid=(1,2,1), margin=25, yshow=False).scatterplot(x, y2, marker="s", color=["green", "blue"])
    
    if True:
        canvas.legend([
            ("Experiment 1", m1),
            ("Experiment 2", m2.markers[0]),
            ("Experiment 3", m2.markers[1]),
            ],
            corner=("top", 100, 100, 70),
            );



.. raw:: html

    <div class="toyplot" id="tee9ad241c67d4b3aa252b79b70c40767" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t74c6b83e52414aaabe64badd09186419" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border-color:#292724;border-style:none;border-width:1.0;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t6c66b6dfcec840718bfa19a6c44c041c"><clipPath id="tc46317b578cd4413bfd5196a5a9b60ea"><rect height="270.0" width="270.0" x="15.0" y="15.0"></rect></clipPath><g clip-path="url(#tc46317b578cd4413bfd5196a5a9b60ea)"><g class="toyplot-mark-Point" id="t8578b58cd4a74dbcabfd5e6c1750be3c"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(25.0, 25.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(30.10204081632653, 35.099958350687224)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(35.20408163265306, 44.99167013744274)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(40.30612244897959, 54.67513536026652)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(45.40816326530612, 64.15035401915867)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(50.51020408163265, 73.41732611411912)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(55.61224489795918, 82.47605164514789)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(60.714285714285715, 91.32653061224485)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(65.81632653061224, 99.96876301541022)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(70.91836734693877, 108.40274885464387)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(76.0204081632653, 116.62848812994588)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(81.12244897959182, 124.64598084131613)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(86.22448979591836, 132.4552269887547)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(91.3265306122449, 140.05622657226155)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(96.42857142857143, 147.44897959183672)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(101.53061224489795, 154.6334860474802)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(106.63265306122449, 161.60974593919198)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(111.73469387755101, 168.37775926697208)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(116.83673469387755, 174.9375260308205)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(121.93877551020408, 181.2890462307372)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(127.0408163265306, 187.4323198667222)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(132.14285714285714, 193.3673469387755)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(137.24489795918365, 199.09412744689712)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(142.34693877551018, 204.61266139108704)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(147.44897959183672, 209.92294877134526)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(152.55102040816328, 215.0249895876718)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(157.6530612244898, 219.9187838400666)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(162.75510204081633, 224.60433152852977)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(167.85714285714286, 229.08163265306123)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(172.9591836734694, 233.35068721366096)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(178.0612244897959, 237.411495210329)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(183.16326530612244, 241.26405664306537)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(188.26530612244895, 244.90837151187003)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(193.36734693877548, 248.344439816743)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(198.46938775510202, 251.5722615576843)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(203.57142857142856, 254.59183673469386)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(208.6734693877551, 257.40316534777173)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(213.77551020408163, 260.00624739691796)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(218.87755102040816, 262.4010828821324)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(223.97959183673467, 264.5876718034152)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(229.0816326530612, 266.5660141607664)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(234.18367346938774, 268.33610995418576)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(239.28571428571428, 269.89795918367344)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(244.3877551020408, 271.25156184922946)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(249.4897959183673, 272.39691795085383)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(254.59183673469386, 273.33402748854644)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(259.69387755102036, 274.0628904623074)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(264.7959183673469, 274.5835068721366)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(269.89795918367344, 274.8958767180342)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(275.0, 275.0)"><circle r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t6f9fdafc838a4b338f688e27ba76b1fe" transform="translate(25.0,275.0)translate(0,10.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(125.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t78b5c9d2ca3f42f994e9efac2e5bd998" transform="translate(25.0,275.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.0</text></g><g transform="translate(125.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">0.5</text></g><g transform="translate(250.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.440892098500626e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t7c577c441d6442c19314368f0dd63017"><clipPath id="td0f1b2caf1b84e3ab05aa57df369d5fa"><rect height="270.0" width="270.0" x="315.0" y="15.0"></rect></clipPath><g clip-path="url(#td0f1b2caf1b84e3ab05aa57df369d5fa)"><g class="toyplot-mark-Point" id="t10f6599a5c97421fbfc10b0236e682b3"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(325.0, 25.0)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(330.1020408163265, 25.104123281965848)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(335.2040816326531, 25.416493127863376)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(340.30612244897964, 25.93710953769263)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(345.40816326530614, 26.665972511453564)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(350.51020408163265, 27.603082049146195)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(355.61224489795916, 28.7484381507705)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(360.7142857142858, 30.102040816326536)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(365.8163265306123, 31.663890045814245)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(370.91836734693874, 33.43398583923366)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(376.0204081632653, 35.412328196584745)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(381.1224489795918, 37.598917117867565)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(386.2244897959183, 39.99375260308206)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(391.32653061224494, 42.596834652228225)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(396.42857142857144, 45.408163265306115)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(401.53061224489795, 48.427738442315686)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(406.6326530612245, 51.65556018325696)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(411.7346938775511, 55.09162848812993)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(416.83673469387753, 58.73594335693461)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(421.9387755102041, 62.588504789670964)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(427.0408163265306, 66.64931278633901)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(432.1428571428571, 70.91836734693877)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(437.2448979591836, 75.3956684714702)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(442.3469387755102, 80.08121615993336)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(447.44897959183675, 84.97501041232819)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(452.55102040816325, 90.07705122865472)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(457.65306122448976, 95.38733860891294)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(462.7551020408163, 100.90587255310285)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(467.8571428571429, 106.63265306122446)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(472.9591836734694, 112.5676801332778)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(478.0612244897959, 118.71095376926277)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(483.1632653061224, 125.0624739691795)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(488.265306122449, 131.6222407330279)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(493.36734693877554, 138.390254060808)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(498.46938775510205, 145.36651395251977)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(503.57142857142856, 152.55102040816323)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(508.67346938775506, 159.94377342773842)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(513.7755102040816, 167.5447730112453)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(518.8775510204082, 175.35401915868388)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(523.9795918367347, 183.3715118700541)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(529.0816326530612, 191.59725114535607)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(534.1836734693877, 200.03123698458973)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(539.2857142857142, 208.6734693877551)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(544.3877551020408, 217.52394835485214)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(549.4897959183673, 226.58267388588084)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(554.5918367346939, 235.84964598084127)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(559.6938775510204, 245.32486463973342)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(564.795918367347, 255.00832986255728)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(569.8979591836734, 264.90004164931275)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(575.0, 275.0)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g></g><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(325.0, 275.0)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(330.1020408163265, 274.8958767180342)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(335.2040816326531, 274.5835068721366)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(340.30612244897964, 274.0628904623074)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(345.40816326530614, 273.33402748854644)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(350.51020408163265, 272.39691795085383)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(355.61224489795916, 271.2515618492295)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(360.7142857142858, 269.89795918367344)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(365.8163265306123, 268.33610995418576)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(370.91836734693874, 266.5660141607664)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(376.0204081632653, 264.5876718034153)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(381.1224489795918, 262.4010828821324)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(386.2244897959183, 260.00624739691796)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(391.32653061224494, 257.4031653477718)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(396.42857142857144, 254.59183673469389)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(401.53061224489795, 251.57226155768433)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(406.6326530612245, 248.34443981674303)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(411.7346938775511, 244.90837151187006)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(416.83673469387753, 241.2640566430654)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(421.9387755102041, 237.41149521032904)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(427.0408163265306, 233.350687213661)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(432.1428571428571, 229.08163265306123)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(437.2448979591836, 224.6043315285298)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(442.3469387755102, 219.91878384006662)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(447.44897959183675, 215.0249895876718)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(452.55102040816325, 209.92294877134526)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(457.65306122448976, 204.61266139108704)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(462.7551020408163, 199.09412744689715)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(467.8571428571429, 193.3673469387755)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(472.9591836734694, 187.4323198667222)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(478.0612244897959, 181.2890462307372)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(483.1632653061224, 174.9375260308205)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(488.265306122449, 168.3777592669721)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(493.36734693877554, 161.609745939192)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(498.46938775510205, 154.6334860474802)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(503.57142857142856, 147.44897959183677)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(508.67346938775506, 140.05622657226158)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(513.7755102040816, 132.4552269887547)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(518.8775510204082, 124.64598084131613)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(523.9795918367347, 116.62848812994591)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(529.0816326530612, 108.40274885464393)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(534.1836734693877, 99.96876301541027)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(539.2857142857142, 91.32653061224492)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(544.3877551020408, 82.47605164514789)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(549.4897959183673, 73.41732611411916)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(554.5918367346939, 64.15035401915873)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(559.6938775510204, 54.67513536026659)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(564.795918367347, 44.99167013744274)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(569.8979591836734, 35.099958350687224)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(575.0, 25.0)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g></g></g></g><g class="toyplot-coordinates-Axis" id="t366e417995f6418aa965b5be1fcd86ab" transform="translate(325.0,275.0)translate(0,10.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(125.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Table" id="ted7b5aa7a672420386a03e25e821f7aa"><g transform="translate(295.0,111.66666666666666)"><g style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(-5.55, -4.440892098500626e-16)"><circle r="5.55"></circle></g></g><g transform="translate(305.0,111.66666666666666)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">Experiment 1</text></g><g transform="translate(295.0,135.0)"><g style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(-5.55, -4.440892098500626e-16)"><rect height="11.1" width="11.1" x="-5.55" y="-5.55"></rect></g></g><g transform="translate(305.0,135.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">Experiment 2</text></g><g transform="translate(295.0,158.33333333333331)"><g style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(-5.55, -4.440892098500626e-16)"><rect height="11.1" width="11.1" x="-5.55" y="-5.55"></rect></g></g><g transform="translate(305.0,158.33333333333331)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">Experiment 3</text></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "tee9ad241c67d4b3aa252b79b70c40767";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t74c6b83e52414aaabe64badd09186419";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t8578b58cd4a74dbcabfd5e6c1750be3c","data","point",["x", "y0"],[[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0], [1.0, 0.9596001665972511, 0.920033319450229, 0.8812994585589339, 0.8433985839233653, 0.8063306955435235, 0.7700957934194085, 0.7346938775510206, 0.7001249479383591, 0.6663890045814245, 0.6334860474802165, 0.6014160766347355, 0.5701790920449812, 0.5397750937109538, 0.5102040816326531, 0.4814660558100793, 0.4535610162432321, 0.4264889629321117, 0.40024989587671805, 0.3748438150770512, 0.3502707205331112, 0.32653061224489793, 0.3036234902124116, 0.2815493544356518, 0.2603082049146189, 0.23990004164931278, 0.22032486463973353, 0.20158267388588094, 0.18367346938775514, 0.16659725114535612, 0.15035401915868396, 0.1349437734277385, 0.12036651395251982, 0.10662224073302792, 0.0937109537692628, 0.08163265306122454, 0.070387338608913, 0.05997501041232822, 0.050395668471470235, 0.04164931278633907, 0.033735943356934646, 0.026655560183256998, 0.020408163265306135, 0.014993752603082056, 0.01041232819658478, 0.006663890045814259, 0.0037484381507705204, 0.0016659725114535648, 0.0004164931278633912, 0.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t6f9fdafc838a4b338f688e27ba76b1fe",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t78b5c9d2ca3f42f994e9efac2e5bd998",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 0.0}, "scale": "linear"}]);
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t10f6599a5c97421fbfc10b0236e682b3","data","point",["x", "y0", "y1"],[[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0], [1.0, 0.9995835068721366, 0.9983340274885465, 0.9962515618492295, 0.9933361099541858, 0.9895876718034152, 0.985006247396918, 0.9795918367346939, 0.973344439816743, 0.9662640566430654, 0.958350687213661, 0.9496043315285297, 0.9400249895876718, 0.9296126613910871, 0.9183673469387755, 0.9062890462307372, 0.8933777592669722, 0.8796334860474803, 0.8650562265722616, 0.8496459808413162, 0.8334027488546439, 0.8163265306122449, 0.7984173261141192, 0.7796751353602666, 0.7600999583506872, 0.7396917950853811, 0.7184506455643482, 0.6963765097875886, 0.6734693877551021, 0.6497292794668887, 0.6251561849229489, 0.599750104123282, 0.5735110370678884, 0.546438983756768, 0.5185339441899208, 0.48979591836734704, 0.46022490628904633, 0.4298209079550188, 0.3985839233652645, 0.3665139525197836, 0.33361099541857575, 0.2998750520616411, 0.26530612244897966, 0.22990420658059152, 0.19366930445647668, 0.15660141607663491, 0.11870054144106634, 0.07996668054977096, 0.040399833402748886, 0.0], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t366e417995f6418aa965b5be1fcd86ab",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


