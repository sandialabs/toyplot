
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _markers:

Markers
=======

In Toyplot, markers are used to show the individual datums in
scatterplots:

.. code:: python

    import numpy
    import toyplot

.. code:: python

    y = numpy.linspace(0, 1, 20) ** 2
    toyplot.scatterplot(y, width=300);



.. raw:: html

    <div align="center" class="toyplot" id="te1a50ce2247e48afbebe9fe8df7d4b1e"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t56a6feee75884d7e9bf2c2709c9e126d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t366424f867314eb3965832dee67a7d1b"><clipPath id="t8802d41d9cdf449ebc2c41c182f5472a"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t8802d41d9cdf449ebc2c41c182f5472a)"><g class="toyplot-mark-Scatterplot" id="tb8012a2d83ce4ae6a028c8863cbcc959" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="250.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="60.0" cy="249.4459833795014" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="70.0" cy="247.78393351800551" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.0" cy="245.01385041551248" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="90.0" cy="241.13573407202216" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="100.0" cy="236.14958448753461" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="110.0" cy="230.05540166204986" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="120.0" cy="222.85318559556785" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="130.0" cy="214.54293628808864" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="140.0" cy="205.1246537396122" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="150.0" cy="194.5983379501385" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="160.0" cy="182.96398891966757" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="170.0" cy="170.22160664819947" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="180.0" cy="156.37119113573411" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="190.0" cy="141.41274238227149" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="200.0" cy="125.34626038781163" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="210.0" cy="108.17174515235459" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="220.0" cy="89.889196675900322" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="230.0" cy="70.498614958448783" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="240.0" cy="50.0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t68bbd9c9ff7945fc840b850907d872fc" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="taec080341a2847da82a045408fd00942" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tb8012a2d83ce4ae6a028c8863cbcc959", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#te1a50ce2247e48afbebe9fe8df7d4b1e .toyplot-mark-popup");
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
            </script><script>
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
    
                var root_id = "te1a50ce2247e48afbebe9fe8df7d4b1e";
                var axes = {"t68bbd9c9ff7945fc840b850907d872fc": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "taec080341a2847da82a045408fd00942": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Markers can also be added to regular plots to highlight the datums (they
are turned-off by default):

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.cartesian(grid=(1, 2, 0)).plot(y)
    canvas.cartesian(grid=(1, 2, 1)).plot(y, marker="o");



.. raw:: html

    <div align="center" class="toyplot" id="t6778084a8db5426995656ba0e44c7a41"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t411de12ef9334188a38edef1b970457f" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tc702b4e0d3e744a0aa5f4ab3fa3eb1e0"><clipPath id="tce6749baf5a64de4a2e4778d93bb2a42"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tce6749baf5a64de4a2e4778d93bb2a42)"><g class="toyplot-mark-Plot" id="tdc2736decbd14f3e8eb59e48acebf37d" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="tbaaceaed4fb44ac49c8e414039f92250" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t129d6913ce4c486b9bf5ff505aa7f754" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="td229af52f0d04ab3b13e291c5d7b4ba8"><clipPath id="t746a10c7466c47f2a7174d44fb6e1030"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#t746a10c7466c47f2a7174d44fb6e1030)"><g class="toyplot-mark-Plot" id="ta1ba88af47f647d8a19f2e4928e5dcf4" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 250.0 L 360.0 249.4459833795014 L 370.0 247.78393351800551 L 380.0 245.01385041551248 L 390.0 241.13573407202216 L 400.0 236.14958448753461 L 410.0 230.05540166204986 L 420.0 222.85318559556785 L 430.0 214.54293628808864 L 440.0 205.1246537396122 L 450.0 194.5983379501385 L 460.0 182.96398891966757 L 470.0 170.22160664819947 L 480.0 156.37119113573411 L 490.0 141.41274238227149 L 500.0 125.34626038781163 L 510.0 108.17174515235459 L 520.0 89.889196675900322 L 530.0 70.498614958448783 L 540.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="350.0" cy="250.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="360.0" cy="249.4459833795014" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="370.0" cy="247.78393351800551" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="380.0" cy="245.01385041551248" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="390.0" cy="241.13573407202216" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="400.0" cy="236.14958448753461" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="410.0" cy="230.05540166204986" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="420.0" cy="222.85318559556785" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="430.0" cy="214.54293628808864" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="440.0" cy="205.1246537396122" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="450.0" cy="194.5983379501385" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="460.0" cy="182.96398891966757" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="470.0" cy="170.22160664819947" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="480.0" cy="156.37119113573411" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="490.0" cy="141.41274238227149" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="500.0" cy="125.34626038781163" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="510.0" cy="108.17174515235459" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="520.0" cy="89.889196675900322" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="530.0" cy="70.498614958448783" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="540.0" cy="50.0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t76fd5f05b3464f46b19d31bae8751681" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="te751ad32b71a429e8a8461a7a4c43af6" transform="translate(350.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Plot Data", "names": ["x", "y0"], "id": "tdc2736decbd14f3e8eb59e48acebf37d", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}, {"title": "Plot Data", "names": ["x", "y0"], "id": "ta1ba88af47f647d8a19f2e4928e5dcf4", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t6778084a8db5426995656ba0e44c7a41 .toyplot-mark-popup");
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
            </script><script>
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
    
                var root_id = "t6778084a8db5426995656ba0e44c7a41";
                var axes = {"t129d6913ce4c486b9bf5ff505aa7f754": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t76fd5f05b3464f46b19d31bae8751681": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tbaaceaed4fb44ac49c8e414039f92250": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "te751ad32b71a429e8a8461a7a4c43af6": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


You can use the ``size`` argument to control the size of the markers:

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.cartesian(grid=(1, 2, 0)).plot(y, marker="o", size=6)
    canvas.cartesian(grid=(1, 2, 1)).plot(y, marker="o", size=10);



.. raw:: html

    <div align="center" class="toyplot" id="te7f4f098ba9d4fd39460ac75a56f9cac"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t31021b37ad6b45eaa36e66c1fd640fc6" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t6d4a598ff718411fbb52877d1aa5f574"><clipPath id="t30e80dd280fc494083f04c3021229af9"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t30e80dd280fc494083f04c3021229af9)"><g class="toyplot-mark-Plot" id="t185ad2fca5684e4abf1fc91b2f7bcf01" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="250.0" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="60.0" cy="249.4459833795014" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="70.0" cy="247.78393351800551" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.0" cy="245.01385041551248" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="90.0" cy="241.13573407202216" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="100.0" cy="236.14958448753461" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="110.0" cy="230.05540166204986" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="120.0" cy="222.85318559556785" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="130.0" cy="214.54293628808864" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="140.0" cy="205.1246537396122" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="150.0" cy="194.5983379501385" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="160.0" cy="182.96398891966757" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="170.0" cy="170.22160664819947" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="180.0" cy="156.37119113573411" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="190.0" cy="141.41274238227149" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="200.0" cy="125.34626038781163" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="210.0" cy="108.17174515235459" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="220.0" cy="89.889196675900322" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="230.0" cy="70.498614958448783" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="240.0" cy="50.0" r="3.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t12714d18b5e446a1a3bdac6df3c83396" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t5985c469bdc94d249e3106a280c270d5" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="tc3a6316526ee475a8a48f2d08eeef935"><clipPath id="teeaee88e093c495bb39c3818ec5cd2f3"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#teeaee88e093c495bb39c3818ec5cd2f3)"><g class="toyplot-mark-Plot" id="te86d4579656a46be8b93610bf2cc868c" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 250.0 L 360.0 249.4459833795014 L 370.0 247.78393351800551 L 380.0 245.01385041551248 L 390.0 241.13573407202216 L 400.0 236.14958448753461 L 410.0 230.05540166204986 L 420.0 222.85318559556785 L 430.0 214.54293628808864 L 440.0 205.1246537396122 L 450.0 194.5983379501385 L 460.0 182.96398891966757 L 470.0 170.22160664819947 L 480.0 156.37119113573411 L 490.0 141.41274238227149 L 500.0 125.34626038781163 L 510.0 108.17174515235459 L 520.0 89.889196675900322 L 530.0 70.498614958448783 L 540.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="350.0" cy="250.0" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="360.0" cy="249.4459833795014" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="370.0" cy="247.78393351800551" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="380.0" cy="245.01385041551248" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="390.0" cy="241.13573407202216" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="400.0" cy="236.14958448753461" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="410.0" cy="230.05540166204986" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="420.0" cy="222.85318559556785" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="430.0" cy="214.54293628808864" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="440.0" cy="205.1246537396122" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="450.0" cy="194.5983379501385" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="460.0" cy="182.96398891966757" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="470.0" cy="170.22160664819947" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="480.0" cy="156.37119113573411" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="490.0" cy="141.41274238227149" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="500.0" cy="125.34626038781163" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="510.0" cy="108.17174515235459" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="520.0" cy="89.889196675900322" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="530.0" cy="70.498614958448783" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="540.0" cy="50.0" r="5.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t491e0e25ea544153aacedbe1614ead7d" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tff20f0bd98dd4cfd81a5aa81165b89bf" transform="translate(350.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Plot Data", "names": ["x", "y0"], "id": "t185ad2fca5684e4abf1fc91b2f7bcf01", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}, {"title": "Plot Data", "names": ["x", "y0"], "id": "te86d4579656a46be8b93610bf2cc868c", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#te7f4f098ba9d4fd39460ac75a56f9cac .toyplot-mark-popup");
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
            </script><script>
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
    
                var root_id = "te7f4f098ba9d4fd39460ac75a56f9cac";
                var axes = {"t12714d18b5e446a1a3bdac6df3c83396": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t491e0e25ea544153aacedbe1614ead7d": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t5985c469bdc94d249e3106a280c270d5": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tff20f0bd98dd4cfd81a5aa81165b89bf": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


You can use the ``area`` argument instead of ``size`` as an
approximation of the *area* of the markers (this is recommended if
you're using per-datum marker sizes to display data).

By default, the markers are small circles, but there are many
alternatives:

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.cartesian(grid=(1, 2, 0)).scatterplot(y, marker="x", size=10)
    canvas.cartesian(grid=(1, 2, 1)).scatterplot(y, marker="^", size=10, mstyle={"stroke":toyplot.color.near_black});



.. raw:: html

    <div align="center" class="toyplot" id="t3b3b453c547a4c14841f25c5de60cdc3"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t144f3412192d44d285425cbc72f3e1c6" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tce9bb6f4051242b78bfc00071cc0515e"><clipPath id="tda16b5f397934ddca9e791d1b20aa3ef"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tda16b5f397934ddca9e791d1b20aa3ef)"><g class="toyplot-mark-Scatterplot" id="tbc0fc36b937c49248452c3c0450caf48" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 50.0, 250.0)" x1="50.0" x2="50.0" y1="245.0" y2="255.0"></line><line transform="rotate(-45, 50.0, 250.0)" x1="45.0" x2="55.0" y1="250.0" y2="250.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 60.0, 249.4459833795014)" x1="60.0" x2="60.0" y1="244.4459833795014" y2="254.4459833795014"></line><line transform="rotate(-45, 60.0, 249.4459833795014)" x1="55.0" x2="65.0" y1="249.4459833795014" y2="249.4459833795014"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 70.0, 247.78393351800551)" x1="70.0" x2="70.0" y1="242.78393351800551" y2="252.78393351800551"></line><line transform="rotate(-45, 70.0, 247.78393351800551)" x1="65.0" x2="75.0" y1="247.78393351800551" y2="247.78393351800551"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 80.0, 245.01385041551248)" x1="80.0" x2="80.0" y1="240.01385041551248" y2="250.01385041551248"></line><line transform="rotate(-45, 80.0, 245.01385041551248)" x1="75.0" x2="85.0" y1="245.01385041551248" y2="245.01385041551248"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 90.0, 241.13573407202216)" x1="90.0" x2="90.0" y1="236.13573407202216" y2="246.13573407202216"></line><line transform="rotate(-45, 90.0, 241.13573407202216)" x1="85.0" x2="95.0" y1="241.13573407202216" y2="241.13573407202216"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 100.0, 236.14958448753461)" x1="100.0" x2="100.0" y1="231.14958448753461" y2="241.14958448753461"></line><line transform="rotate(-45, 100.0, 236.14958448753461)" x1="95.0" x2="105.0" y1="236.14958448753461" y2="236.14958448753461"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 110.0, 230.05540166204986)" x1="110.0" x2="110.0" y1="225.05540166204986" y2="235.05540166204986"></line><line transform="rotate(-45, 110.0, 230.05540166204986)" x1="105.0" x2="115.0" y1="230.05540166204986" y2="230.05540166204986"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 120.0, 222.85318559556785)" x1="120.0" x2="120.0" y1="217.85318559556785" y2="227.85318559556785"></line><line transform="rotate(-45, 120.0, 222.85318559556785)" x1="115.0" x2="125.0" y1="222.85318559556785" y2="222.85318559556785"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 130.0, 214.54293628808864)" x1="130.0" x2="130.0" y1="209.54293628808864" y2="219.54293628808864"></line><line transform="rotate(-45, 130.0, 214.54293628808864)" x1="125.0" x2="135.0" y1="214.54293628808864" y2="214.54293628808864"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 140.0, 205.1246537396122)" x1="140.0" x2="140.0" y1="200.1246537396122" y2="210.1246537396122"></line><line transform="rotate(-45, 140.0, 205.1246537396122)" x1="135.0" x2="145.0" y1="205.1246537396122" y2="205.1246537396122"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 150.0, 194.5983379501385)" x1="150.0" x2="150.0" y1="189.5983379501385" y2="199.5983379501385"></line><line transform="rotate(-45, 150.0, 194.5983379501385)" x1="145.0" x2="155.0" y1="194.5983379501385" y2="194.5983379501385"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 160.0, 182.96398891966757)" x1="160.0" x2="160.0" y1="177.96398891966757" y2="187.96398891966757"></line><line transform="rotate(-45, 160.0, 182.96398891966757)" x1="155.0" x2="165.0" y1="182.96398891966757" y2="182.96398891966757"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 170.0, 170.22160664819947)" x1="170.0" x2="170.0" y1="165.22160664819947" y2="175.22160664819947"></line><line transform="rotate(-45, 170.0, 170.22160664819947)" x1="165.0" x2="175.0" y1="170.22160664819947" y2="170.22160664819947"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 180.0, 156.37119113573411)" x1="180.0" x2="180.0" y1="151.37119113573411" y2="161.37119113573411"></line><line transform="rotate(-45, 180.0, 156.37119113573411)" x1="175.0" x2="185.0" y1="156.37119113573411" y2="156.37119113573411"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 190.0, 141.41274238227149)" x1="190.0" x2="190.0" y1="136.41274238227149" y2="146.41274238227149"></line><line transform="rotate(-45, 190.0, 141.41274238227149)" x1="185.0" x2="195.0" y1="141.41274238227149" y2="141.41274238227149"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 200.0, 125.34626038781163)" x1="200.0" x2="200.0" y1="120.34626038781163" y2="130.34626038781164"></line><line transform="rotate(-45, 200.0, 125.34626038781163)" x1="195.0" x2="205.0" y1="125.34626038781163" y2="125.34626038781163"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 210.0, 108.17174515235459)" x1="210.0" x2="210.0" y1="103.17174515235459" y2="113.17174515235459"></line><line transform="rotate(-45, 210.0, 108.17174515235459)" x1="205.0" x2="215.0" y1="108.17174515235459" y2="108.17174515235459"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 220.0, 89.889196675900322)" x1="220.0" x2="220.0" y1="84.889196675900322" y2="94.889196675900322"></line><line transform="rotate(-45, 220.0, 89.889196675900322)" x1="215.0" x2="225.0" y1="89.889196675900322" y2="89.889196675900322"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 230.0, 70.498614958448783)" x1="230.0" x2="230.0" y1="65.498614958448783" y2="75.498614958448783"></line><line transform="rotate(-45, 230.0, 70.498614958448783)" x1="225.0" x2="235.0" y1="70.498614958448783" y2="70.498614958448783"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 240.0, 50.0)" x1="240.0" x2="240.0" y1="45.0" y2="55.0"></line><line transform="rotate(-45, 240.0, 50.0)" x1="235.0" x2="245.0" y1="50.0" y2="50.0"></line></g></g></g></g><g class="toyplot-coordinates-Axis" id="t5811344642b840a8a215cfe3f0ae5574" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="te007d2b6b68f4407b0c88e5e0c05b1e3" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t74210489993b4259b74d68e359f9f7da"><clipPath id="td83b562c3e764e21adcc0eabe22d32c3"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#td83b562c3e764e21adcc0eabe22d32c3)"><g class="toyplot-mark-Scatterplot" id="tdbadf2a13196447686d127f3af20c3e6" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="345.0,255.0 350.0,245.0 355.0,255.0" transform="rotate(0, 350.0, 250.0)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="355.0,254.4459833795014 360.0,244.4459833795014 365.0,254.4459833795014" transform="rotate(0, 360.0, 249.4459833795014)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="365.0,252.78393351800551 370.0,242.78393351800551 375.0,252.78393351800551" transform="rotate(0, 370.0, 247.78393351800551)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="375.0,250.01385041551248 380.0,240.01385041551248 385.0,250.01385041551248" transform="rotate(0, 380.0, 245.01385041551248)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="385.0,246.13573407202216 390.0,236.13573407202216 395.0,246.13573407202216" transform="rotate(0, 390.0, 241.13573407202216)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="395.0,241.14958448753461 400.0,231.14958448753461 405.0,241.14958448753461" transform="rotate(0, 400.0, 236.14958448753461)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="405.0,235.05540166204986 410.0,225.05540166204986 415.0,235.05540166204986" transform="rotate(0, 410.0, 230.05540166204986)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="415.0,227.85318559556785 420.0,217.85318559556785 425.0,227.85318559556785" transform="rotate(0, 420.0, 222.85318559556785)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="425.0,219.54293628808864 430.0,209.54293628808864 435.0,219.54293628808864" transform="rotate(0, 430.0, 214.54293628808864)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="435.0,210.1246537396122 440.0,200.1246537396122 445.0,210.1246537396122" transform="rotate(0, 440.0, 205.1246537396122)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="445.0,199.5983379501385 450.0,189.5983379501385 455.0,199.5983379501385" transform="rotate(0, 450.0, 194.5983379501385)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="455.0,187.96398891966757 460.0,177.96398891966757 465.0,187.96398891966757" transform="rotate(0, 460.0, 182.96398891966757)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="465.0,175.22160664819947 470.0,165.22160664819947 475.0,175.22160664819947" transform="rotate(0, 470.0, 170.22160664819947)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="475.0,161.37119113573411 480.0,151.37119113573411 485.0,161.37119113573411" transform="rotate(0, 480.0, 156.37119113573411)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="485.0,146.41274238227149 490.0,136.41274238227149 495.0,146.41274238227149" transform="rotate(0, 490.0, 141.41274238227149)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="495.0,130.34626038781164 500.0,120.34626038781163 505.0,130.34626038781164" transform="rotate(0, 500.0, 125.34626038781163)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="505.0,113.17174515235459 510.0,103.17174515235459 515.0,113.17174515235459" transform="rotate(0, 510.0, 108.17174515235459)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="515.0,94.889196675900322 520.0,84.889196675900322 525.0,94.889196675900322" transform="rotate(0, 520.0, 89.889196675900322)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="525.0,75.498614958448783 530.0,65.498614958448783 535.0,75.498614958448783" transform="rotate(0, 530.0, 70.498614958448783)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="535.0,55.0 540.0,45.0 545.0,55.0" transform="rotate(0, 540.0, 50.0)"></polygon></g></g></g></g><g class="toyplot-coordinates-Axis" id="tdb2cf0509036482ab59d190c5d62340d" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t442a78b302e943818864a03a7240a54f" transform="translate(350.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tbc0fc36b937c49248452c3c0450caf48", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tdbadf2a13196447686d127f3af20c3e6", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t3b3b453c547a4c14841f25c5de60cdc3 .toyplot-mark-popup");
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
            </script><script>
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
    
                var root_id = "t3b3b453c547a4c14841f25c5de60cdc3";
                var axes = {"t442a78b302e943818864a03a7240a54f": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t5811344642b840a8a215cfe3f0ae5574": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tdb2cf0509036482ab59d190c5d62340d": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "te007d2b6b68f4407b0c88e5e0c05b1e3": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Note the use of the *mstyle* argument to override the appearance of the
marker in the second example. For line plots, this allows you to style
the lines and the markers separately:

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.cartesian(grid=(1, 2, 0)).plot(y, marker="o", size=8, style={"stroke":"darkgreen"})
    canvas.cartesian(grid=(1, 2, 1)).plot(y, marker="o", size=8, mstyle={"stroke":"darkgreen"});



.. raw:: html

    <div align="center" class="toyplot" id="t2ed195916ef14620833599a1d85bfc4f"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t16e94f36a3064eaea88d56a6364ee1d4" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t9b3acdc2082e49729b4c6b61c0acb90b"><clipPath id="t7b3d48b47dd5497a92f7892685f60426"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t7b3d48b47dd5497a92f7892685f60426)"><g class="toyplot-mark-Plot" id="ta080bd2cb8014d4bb4a25742b11ca4f7" style="fill:none;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="250.0" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="60.0" cy="249.4459833795014" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="70.0" cy="247.78393351800551" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.0" cy="245.01385041551248" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="90.0" cy="241.13573407202216" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="100.0" cy="236.14958448753461" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="110.0" cy="230.05540166204986" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="120.0" cy="222.85318559556785" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="130.0" cy="214.54293628808864" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="140.0" cy="205.1246537396122" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="150.0" cy="194.5983379501385" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="160.0" cy="182.96398891966757" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="170.0" cy="170.22160664819947" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="180.0" cy="156.37119113573411" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="190.0" cy="141.41274238227149" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="200.0" cy="125.34626038781163" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="210.0" cy="108.17174515235459" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="220.0" cy="89.889196675900322" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="230.0" cy="70.498614958448783" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="240.0" cy="50.0" r="4.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t52aa9acb918644f3baec1350dfe00329" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tb28631194222428c8e0adad3e38b17c6" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t098ca02117214e53a33a408c9d137fcf"><clipPath id="t684e9b3ff156423886bb352a9e5f444f"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#t684e9b3ff156423886bb352a9e5f444f)"><g class="toyplot-mark-Plot" id="t00e17765c8ac44459755f4e89140bafb" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 250.0 L 360.0 249.4459833795014 L 370.0 247.78393351800551 L 380.0 245.01385041551248 L 390.0 241.13573407202216 L 400.0 236.14958448753461 L 410.0 230.05540166204986 L 420.0 222.85318559556785 L 430.0 214.54293628808864 L 440.0 205.1246537396122 L 450.0 194.5983379501385 L 460.0 182.96398891966757 L 470.0 170.22160664819947 L 480.0 156.37119113573411 L 490.0 141.41274238227149 L 500.0 125.34626038781163 L 510.0 108.17174515235459 L 520.0 89.889196675900322 L 530.0 70.498614958448783 L 540.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="350.0" cy="250.0" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="360.0" cy="249.4459833795014" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="370.0" cy="247.78393351800551" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="380.0" cy="245.01385041551248" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="390.0" cy="241.13573407202216" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="400.0" cy="236.14958448753461" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="410.0" cy="230.05540166204986" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="420.0" cy="222.85318559556785" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="430.0" cy="214.54293628808864" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="440.0" cy="205.1246537396122" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="450.0" cy="194.5983379501385" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="460.0" cy="182.96398891966757" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="470.0" cy="170.22160664819947" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="480.0" cy="156.37119113573411" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="490.0" cy="141.41274238227149" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="500.0" cy="125.34626038781163" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="510.0" cy="108.17174515235459" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="520.0" cy="89.889196675900322" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="530.0" cy="70.498614958448783" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="540.0" cy="50.0" r="4.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="tccdbd08f77b44a698197a16684e27468" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="td9ef25f7ff9f48d49ee4057501cd161c" transform="translate(350.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Plot Data", "names": ["x", "y0"], "id": "ta080bd2cb8014d4bb4a25742b11ca4f7", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}, {"title": "Plot Data", "names": ["x", "y0"], "id": "t00e17765c8ac44459755f4e89140bafb", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t2ed195916ef14620833599a1d85bfc4f .toyplot-mark-popup");
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
            </script><script>
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
    
                var root_id = "t2ed195916ef14620833599a1d85bfc4f";
                var axes = {"t52aa9acb918644f3baec1350dfe00329": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tb28631194222428c8e0adad3e38b17c6": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tccdbd08f77b44a698197a16684e27468": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "td9ef25f7ff9f48d49ee4057501cd161c": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


So far, we've been using string codes to specify different marker
shapes. Here is every builtin marker shape in Toyplot, with their string
codes:

.. code:: python

    markers = [None, "|","/","-","\\","+","x","*","^",">","v","<","s","d","o","oo","o|","o-","o+","ox","o*"]
    mstyle = {"stroke":toyplot.color.near_black, "fill":"#feb"}
    labels = [str(marker) for marker in markers]
    
    # This is necessary because "<" and ">" are interpreted as tags when rendering text.
    from xml.sax.saxutils import escape
    labels = [escape(label) for label in labels]
    
    style = {"fill":toyplot.color.near_black, "font-size":"16px", "font-family":"monospace"}
    
    canvas = toyplot.Canvas(700, 200)
    axes = canvas.cartesian(label="Marker Codes and Shapes", ymin=-0.5, ymax=1.5)
    axes.x.show = False
    axes.y.show = False
    axes.scatterplot(numpy.repeat(0, len(markers)), marker=markers, mstyle=mstyle, size=15)
    axes.text(numpy.arange(len(markers)), numpy.repeat(1, len(markers)), text=labels, style=style);



.. raw:: html

    <div align="center" class="toyplot" id="tc6d0d5016e3a4601924f949bbc3330d7"><svg class="toyplot-canvas-Canvas" height="200.0px" id="tacfa956c3a814d519e566e595afee98c" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 200.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tcf99577678504f1ba8019b47a7e56dc4"><clipPath id="tf8c10b6ce1064830892518d3cb7dde44"><rect height="120.0" width="620.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tf8c10b6ce1064830892518d3cb7dde44)"><g class="toyplot-mark-Scatterplot" id="t3c30f1aafabb437681774921f73f9ef1" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(0, 96.946564885496187, 125.0)" x1="96.946564885496187" x2="96.946564885496187" y1="117.5" y2="132.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(45, 125.57251908396947, 125.0)" x1="125.57251908396947" x2="125.57251908396947" y1="117.5" y2="132.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(-90, 154.19847328244276, 125.0)" x1="154.19847328244276" x2="154.19847328244276" y1="117.5" y2="132.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(-45, 182.824427480916, 125.0)" x1="182.824427480916" x2="182.824427480916" y1="117.5" y2="132.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(0, 211.4503816793893, 125.0)" x1="211.4503816793893" x2="211.4503816793893" y1="117.5" y2="132.5"></line><line transform="rotate(0, 211.4503816793893, 125.0)" x1="203.9503816793893" x2="218.9503816793893" y1="125.0" y2="125.0"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(-45, 240.07633587786259, 125.0)" x1="240.07633587786259" x2="240.07633587786259" y1="117.5" y2="132.5"></line><line transform="rotate(-45, 240.07633587786259, 125.0)" x1="232.57633587786259" x2="247.57633587786259" y1="125.0" y2="125.0"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(0, 268.70229007633583, 125.0)" x1="268.70229007633583" x2="268.70229007633583" y1="117.5" y2="132.5"></line><line transform="rotate(60, 268.70229007633583, 125.0)" x1="268.70229007633583" x2="268.70229007633583" y1="117.5" y2="132.5"></line><line transform="rotate(-60, 268.70229007633583, 125.0)" x1="268.70229007633583" x2="268.70229007633583" y1="117.5" y2="132.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="289.82824427480915,132.5 297.32824427480915,117.5 304.82824427480915,132.5" transform="rotate(0, 297.32824427480915, 125.0)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="318.45419847328247,132.5 325.95419847328247,117.5 333.45419847328247,132.5" transform="rotate(90, 325.95419847328247, 125.0)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="347.08015267175574,132.5 354.58015267175574,117.5 362.08015267175574,132.5" transform="rotate(-180, 354.58015267175574, 125.0)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="375.70610687022901,132.5 383.20610687022901,117.5 390.70610687022901,132.5" transform="rotate(-90, 383.20610687022901, 125.0)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><rect height="15.0" transform="rotate(0, 411.83206106870233, 125.0)" width="15.0" x="404.33206106870233" y="117.5"></rect></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><rect height="15.0" transform="rotate(-45, 440.45801526717554, 125.0)" width="15.0" x="432.95801526717554" y="117.5"></rect></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="469.08396946564886" cy="125.0" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="497.70992366412213" cy="125.0" r="7.5"></circle><circle cx="497.70992366412213" cy="125.0" r="3.75"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="526.33587786259534" cy="125.0" r="7.5"></circle><line transform="rotate(0, 526.33587786259534, 125.0)" x1="526.33587786259534" x2="526.33587786259534" y1="117.5" y2="132.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="554.96183206106866" cy="125.0" r="7.5"></circle><line transform="rotate(-90, 554.96183206106866, 125.0)" x1="554.96183206106866" x2="554.96183206106866" y1="117.5" y2="132.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="583.58778625954199" cy="125.0" r="7.5"></circle><line transform="rotate(0, 583.58778625954199, 125.0)" x1="583.58778625954199" x2="583.58778625954199" y1="117.5" y2="132.5"></line><line transform="rotate(0, 583.58778625954199, 125.0)" x1="576.08778625954199" x2="591.08778625954199" y1="125.0" y2="125.0"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="612.21374045801531" cy="125.0" r="7.5"></circle><line transform="rotate(-45, 612.21374045801531, 125.0)" x1="612.21374045801531" x2="612.21374045801531" y1="117.5" y2="132.5"></line><line transform="rotate(-45, 612.21374045801531, 125.0)" x1="604.71374045801531" x2="619.71374045801531" y1="125.0" y2="125.0"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="640.83969465648852" cy="125.0" r="7.5"></circle><line transform="rotate(0, 640.83969465648852, 125.0)" x1="640.83969465648852" x2="640.83969465648852" y1="117.5" y2="132.5"></line><line transform="rotate(60, 640.83969465648852, 125.0)" x1="640.83969465648852" x2="640.83969465648852" y1="117.5" y2="132.5"></line><line transform="rotate(-60, 640.83969465648852, 125.0)" x1="640.83969465648852" x2="640.83969465648852" y1="117.5" y2="132.5"></line></g></g></g><g class="toyplot-mark-Text" id="t043665d3b26a4a989dba3204eb18c4c8"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(68.320610687022892,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-19.2" y="3.776">None</text></g><g class="toyplot-Datum" transform="translate(96.946564885496187,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">|</text></g><g class="toyplot-Datum" transform="translate(125.57251908396947,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">/</text></g><g class="toyplot-Datum" transform="translate(154.19847328244276,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">-</text></g><g class="toyplot-Datum" transform="translate(182.824427480916,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">\</text></g><g class="toyplot-Datum" transform="translate(211.4503816793893,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">+</text></g><g class="toyplot-Datum" transform="translate(240.07633587786259,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">x</text></g><g class="toyplot-Datum" transform="translate(268.70229007633583,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">*</text></g><g class="toyplot-Datum" transform="translate(297.32824427480915,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">^</text></g><g class="toyplot-Datum" transform="translate(325.95419847328247,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">&gt;</text></g><g class="toyplot-Datum" transform="translate(354.58015267175574,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">v</text></g><g class="toyplot-Datum" transform="translate(383.20610687022901,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">&lt;</text></g><g class="toyplot-Datum" transform="translate(411.83206106870233,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">s</text></g><g class="toyplot-Datum" transform="translate(440.45801526717554,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">d</text></g><g class="toyplot-Datum" transform="translate(469.08396946564886,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-4.8" y="3.776">o</text></g><g class="toyplot-Datum" transform="translate(497.70992366412213,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-9.6" y="3.776">oo</text></g><g class="toyplot-Datum" transform="translate(526.33587786259534,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-9.6" y="3.776">o|</text></g><g class="toyplot-Datum" transform="translate(554.96183206106866,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-9.6" y="3.776">o-</text></g><g class="toyplot-Datum" transform="translate(583.58778625954199,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-9.6" y="3.776">o+</text></g><g class="toyplot-Datum" transform="translate(612.21374045801531,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-9.6" y="3.776">ox</text></g><g class="toyplot-Datum" transform="translate(640.83969465648852,75.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16.0;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-9.6" y="3.776">o*</text></g></g></g></g><g transform="translate(350.0,50.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-87.528" y="-10.423">Marker Codes and Shapes</text></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t3c30f1aafabb437681774921f73f9ef1", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#tc6d0d5016e3a4601924f949bbc3330d7 .toyplot-mark-popup");
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


There are several items worth noting - first, you can pass a sequence of
marker codes to the *marker* argument, to specify markers on a
per-series or per-datum basis. Second, you can pass *None* or an empty
string to produce an invisible marker, if you need to hide a datum or
declutter the display. Third, observe that several of the marker shapes
contain internal details that require a contrasting stroke and fill to
be visible.

So far, we've been using the marker shape code to specify our markers,
but this is actually a shortcut. A full marker specification is a Python
dictionary that contains a set of specific attributes:

-  "shape" - the shape code for the marker.
-  "label" - optional text label superimposed on the marker.
-  "mstyle" - optional dictionary of CSS styles to apply to the marker.
-  "lstyle" - optional dictionary of CSS styles to apply to the marker
   label.
-  "angle" - optional angle (in degrees) to rotate the marker.

.. code:: python

    canvas = toyplot.Canvas(600, 300)
    canvas.cartesian(grid=(1, 2, 0)).scatterplot(y, marker={"shape":"|", "angle":45}, size=10)
    canvas.cartesian(grid=(1, 2, 1)).scatterplot(y, marker={"shape":"o", "label":"A", "lstyle":{"fill":"white"}}, size=15);



.. raw:: html

    <div align="center" class="toyplot" id="tbb55c483dbdf4033a30fdbba0f042569"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tf189e94761ed435c880f3258730b7df1" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t4bb5a1fd611344efb8936d707dae8af7"><clipPath id="tc8fb954f4481431ca3c6aba107b931d2"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tc8fb954f4481431ca3c6aba107b931d2)"><g class="toyplot-mark-Scatterplot" id="tdeb07da1fa9948a6b4f0a11010c5c0ca" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 50.0, 250.0)" x1="50.0" x2="50.0" y1="245.0" y2="255.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 60.0, 249.4459833795014)" x1="60.0" x2="60.0" y1="244.4459833795014" y2="254.4459833795014"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 70.0, 247.78393351800551)" x1="70.0" x2="70.0" y1="242.78393351800551" y2="252.78393351800551"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 80.0, 245.01385041551248)" x1="80.0" x2="80.0" y1="240.01385041551248" y2="250.01385041551248"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 90.0, 241.13573407202216)" x1="90.0" x2="90.0" y1="236.13573407202216" y2="246.13573407202216"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 100.0, 236.14958448753461)" x1="100.0" x2="100.0" y1="231.14958448753461" y2="241.14958448753461"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 110.0, 230.05540166204986)" x1="110.0" x2="110.0" y1="225.05540166204986" y2="235.05540166204986"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 120.0, 222.85318559556785)" x1="120.0" x2="120.0" y1="217.85318559556785" y2="227.85318559556785"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 130.0, 214.54293628808864)" x1="130.0" x2="130.0" y1="209.54293628808864" y2="219.54293628808864"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 140.0, 205.1246537396122)" x1="140.0" x2="140.0" y1="200.1246537396122" y2="210.1246537396122"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 150.0, 194.5983379501385)" x1="150.0" x2="150.0" y1="189.5983379501385" y2="199.5983379501385"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 160.0, 182.96398891966757)" x1="160.0" x2="160.0" y1="177.96398891966757" y2="187.96398891966757"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 170.0, 170.22160664819947)" x1="170.0" x2="170.0" y1="165.22160664819947" y2="175.22160664819947"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 180.0, 156.37119113573411)" x1="180.0" x2="180.0" y1="151.37119113573411" y2="161.37119113573411"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 190.0, 141.41274238227149)" x1="190.0" x2="190.0" y1="136.41274238227149" y2="146.41274238227149"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 200.0, 125.34626038781163)" x1="200.0" x2="200.0" y1="120.34626038781163" y2="130.34626038781164"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 210.0, 108.17174515235459)" x1="210.0" x2="210.0" y1="103.17174515235459" y2="113.17174515235459"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 220.0, 89.889196675900322)" x1="220.0" x2="220.0" y1="84.889196675900322" y2="94.889196675900322"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 230.0, 70.498614958448783)" x1="230.0" x2="230.0" y1="65.498614958448783" y2="75.498614958448783"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 240.0, 50.0)" x1="240.0" x2="240.0" y1="45.0" y2="55.0"></line></g></g></g></g><g class="toyplot-coordinates-Axis" id="t008c07b23df246059643b7987432efe0" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t90111db358424524acb30d5596ec0826" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t0cbcbdbca626453aa2bb3dffcaa6e429"><clipPath id="t84f126b53c054efcb5de899c8f7cd3b9"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#t84f126b53c054efcb5de899c8f7cd3b9)"><g class="toyplot-mark-Scatterplot" id="taaea440cef32489da4a8c5f42c73a0bb" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="350.0" cy="250.0" r="7.5"></circle><g transform="translate(350.0,250.0)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="360.0" cy="249.4459833795014" r="7.5"></circle><g transform="translate(360.0,249.4459833795014)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="370.0" cy="247.78393351800551" r="7.5"></circle><g transform="translate(370.0,247.78393351800551)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="380.0" cy="245.01385041551248" r="7.5"></circle><g transform="translate(380.0,245.01385041551248)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="390.0" cy="241.13573407202216" r="7.5"></circle><g transform="translate(390.0,241.13573407202216)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="400.0" cy="236.14958448753461" r="7.5"></circle><g transform="translate(400.0,236.14958448753461)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="410.0" cy="230.05540166204986" r="7.5"></circle><g transform="translate(410.0,230.05540166204986)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="420.0" cy="222.85318559556785" r="7.5"></circle><g transform="translate(420.0,222.85318559556785)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="430.0" cy="214.54293628808864" r="7.5"></circle><g transform="translate(430.0,214.54293628808864)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="440.0" cy="205.1246537396122" r="7.5"></circle><g transform="translate(440.0,205.1246537396122)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="450.0" cy="194.5983379501385" r="7.5"></circle><g transform="translate(450.0,194.5983379501385)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="460.0" cy="182.96398891966757" r="7.5"></circle><g transform="translate(460.0,182.96398891966757)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="470.0" cy="170.22160664819947" r="7.5"></circle><g transform="translate(470.0,170.22160664819947)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="480.0" cy="156.37119113573411" r="7.5"></circle><g transform="translate(480.0,156.37119113573411)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="490.0" cy="141.41274238227149" r="7.5"></circle><g transform="translate(490.0,141.41274238227149)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="500.0" cy="125.34626038781163" r="7.5"></circle><g transform="translate(500.0,125.34626038781163)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="510.0" cy="108.17174515235459" r="7.5"></circle><g transform="translate(510.0,108.17174515235459)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="520.0" cy="89.889196675900322" r="7.5"></circle><g transform="translate(520.0,89.889196675900322)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="530.0" cy="70.498614958448783" r="7.5"></circle><g transform="translate(530.0,70.498614958448783)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="540.0" cy="50.0" r="7.5"></circle><g transform="translate(540.0,50.0)"><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;font-family:helvetica;font-size:11.25;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-3.751875" y="2.874375">A</text></g></g></g></g></g><g class="toyplot-coordinates-Axis" id="tec1650f8622048289f597fcc29dd4153" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(50.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">5</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">15</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t919585fac4e04da9b36395a74dfc39cc" transform="translate(350.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tdeb07da1fa9948a6b4f0a11010c5c0ca", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "taaea440cef32489da4a8c5f42c73a0bb", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#tbb55c483dbdf4033a30fdbba0f042569 .toyplot-mark-popup");
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
            </script><script>
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
    
                var root_id = "tbb55c483dbdf4033a30fdbba0f042569";
                var axes = {"t008c07b23df246059643b7987432efe0": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t90111db358424524acb30d5596ec0826": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t919585fac4e04da9b36395a74dfc39cc": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tec1650f8622048289f597fcc29dd4153": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Using the full marker specification allows you to control the style and
appearance of individual markers, if needed.
