
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

    <div align="center" class="toyplot" id="t2d3a0f3bfa26489aa00ce2e0977ae997"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tcd94b5b1fb3e49bda6128c6a896df215" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tcad2023a4f7846ac856d83234f9beba9"><clipPath id="t05d63f23a8b845419aa4faede8a8d4b0"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t05d63f23a8b845419aa4faede8a8d4b0)"><g class="toyplot-mark-Scatterplot" id="t2285a93fad73487593617bf23b4f92c7" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="250.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="60.0" cy="249.4459833795014" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="70.0" cy="247.78393351800551" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.0" cy="245.01385041551248" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="90.0" cy="241.13573407202216" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="100.0" cy="236.14958448753461" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="110.0" cy="230.05540166204986" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="120.0" cy="222.85318559556785" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="130.0" cy="214.54293628808864" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="140.0" cy="205.1246537396122" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="150.0" cy="194.5983379501385" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="160.0" cy="182.96398891966757" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="170.0" cy="170.22160664819947" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="180.0" cy="156.37119113573411" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="190.0" cy="141.41274238227149" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="200.0" cy="125.34626038781163" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="210.0" cy="108.17174515235459" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="220.0" cy="89.889196675900322" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="230.0" cy="70.498614958448783" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="240.0" cy="50.0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="td2aefd67ed254aaf89c359affd1bb05a" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">10</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">15</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tcb3cac9e33fe4d0b97ac94e4db7e1a31" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="font-size:10.0px">0.0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="font-size:10.0px">0.5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="font-size:10.0px">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t2285a93fad73487593617bf23b4f92c7", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t2d3a0f3bfa26489aa00ce2e0977ae997 .toyplot-mark-popup");
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
    
                var root_id = "t2d3a0f3bfa26489aa00ce2e0977ae997";
                var axes = {"tcb3cac9e33fe4d0b97ac94e4db7e1a31": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "td2aefd67ed254aaf89c359affd1bb05a": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
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

    <div align="center" class="toyplot" id="t45757c007ce64d2ca8fb094986734c81"><svg class="toyplot-canvas-Canvas" height="300.0px" id="te5568089d2ec44d4824de924fb5159e7" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t100767581b1941d0a92ed19efe9416a6"><clipPath id="t5513211a9dc34002ac5663097618d08a"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t5513211a9dc34002ac5663097618d08a)"><g class="toyplot-mark-Plot" id="t5c8c869a03f44d3285c81dcd9b8b0cc7" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="t8f9d57275bca414392c0014c37d229f2" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">10</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">15</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t77a27c3024e94fd6bffdc71a01235239" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="font-size:10.0px">0.0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="font-size:10.0px">0.5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="font-size:10.0px">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t1352865b618a4f718819ebab68a2da53"><clipPath id="t828cdf5fae864ebd96fc4809059052b4"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#t828cdf5fae864ebd96fc4809059052b4)"><g class="toyplot-mark-Plot" id="tefea89f0b44847689f87840ccd51a918" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 250.0 L 360.0 249.4459833795014 L 370.0 247.78393351800551 L 380.0 245.01385041551248 L 390.0 241.13573407202216 L 400.0 236.14958448753461 L 410.0 230.05540166204986 L 420.0 222.85318559556785 L 430.0 214.54293628808864 L 440.0 205.1246537396122 L 450.0 194.5983379501385 L 460.0 182.96398891966757 L 470.0 170.22160664819947 L 480.0 156.37119113573411 L 490.0 141.41274238227149 L 500.0 125.34626038781163 L 510.0 108.17174515235459 L 520.0 89.889196675900322 L 530.0 70.498614958448783 L 540.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="350.0" cy="250.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="360.0" cy="249.4459833795014" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="370.0" cy="247.78393351800551" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="380.0" cy="245.01385041551248" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="390.0" cy="241.13573407202216" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="400.0" cy="236.14958448753461" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="410.0" cy="230.05540166204986" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="420.0" cy="222.85318559556785" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="430.0" cy="214.54293628808864" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="440.0" cy="205.1246537396122" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="450.0" cy="194.5983379501385" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="460.0" cy="182.96398891966757" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="470.0" cy="170.22160664819947" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="480.0" cy="156.37119113573411" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="490.0" cy="141.41274238227149" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="500.0" cy="125.34626038781163" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="510.0" cy="108.17174515235459" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="520.0" cy="89.889196675900322" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="530.0" cy="70.498614958448783" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="540.0" cy="50.0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t90b7b938fc2f48b3a3f758405266ed9f" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">10</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">15</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t9f96090170e74bd9a770dcb4f8dda3af" transform="translate(350.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="font-size:10.0px">0.0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="font-size:10.0px">0.5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="font-size:10.0px">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Plot Data", "names": ["x", "y0"], "id": "t5c8c869a03f44d3285c81dcd9b8b0cc7", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}, {"title": "Plot Data", "names": ["x", "y0"], "id": "tefea89f0b44847689f87840ccd51a918", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t45757c007ce64d2ca8fb094986734c81 .toyplot-mark-popup");
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
    
                var root_id = "t45757c007ce64d2ca8fb094986734c81";
                var axes = {"t77a27c3024e94fd6bffdc71a01235239": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t8f9d57275bca414392c0014c37d229f2": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t90b7b938fc2f48b3a3f758405266ed9f": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t9f96090170e74bd9a770dcb4f8dda3af": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
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

    <div align="center" class="toyplot" id="tdba1dd08bf4b48948604e34d9613214a"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t040d1270c8c14455899b27bf357756cb" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t01636230a35149fa9647862b05ca183a"><clipPath id="t477e9867e4b246aa88ab58934551d981"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t477e9867e4b246aa88ab58934551d981)"><g class="toyplot-mark-Plot" id="t697aa9eaa024490a84f558d4b52e53c0" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="250.0" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="60.0" cy="249.4459833795014" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="70.0" cy="247.78393351800551" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.0" cy="245.01385041551248" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="90.0" cy="241.13573407202216" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="100.0" cy="236.14958448753461" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="110.0" cy="230.05540166204986" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="120.0" cy="222.85318559556785" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="130.0" cy="214.54293628808864" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="140.0" cy="205.1246537396122" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="150.0" cy="194.5983379501385" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="160.0" cy="182.96398891966757" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="170.0" cy="170.22160664819947" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="180.0" cy="156.37119113573411" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="190.0" cy="141.41274238227149" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="200.0" cy="125.34626038781163" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="210.0" cy="108.17174515235459" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="220.0" cy="89.889196675900322" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="230.0" cy="70.498614958448783" r="3.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="240.0" cy="50.0" r="3.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t5b9ac7fc2684432a9790fcc2da30556e" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">10</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">15</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tbc2c3d0eba0c41ecb201cd788e62d1ae" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="font-size:10.0px">0.0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="font-size:10.0px">0.5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="font-size:10.0px">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t4462a7af40ee4a4aaae9376c37a81288"><clipPath id="t17990b2914304548850c38b505029152"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#t17990b2914304548850c38b505029152)"><g class="toyplot-mark-Plot" id="t388f0aeda06a4732acef20492a2efd74" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 250.0 L 360.0 249.4459833795014 L 370.0 247.78393351800551 L 380.0 245.01385041551248 L 390.0 241.13573407202216 L 400.0 236.14958448753461 L 410.0 230.05540166204986 L 420.0 222.85318559556785 L 430.0 214.54293628808864 L 440.0 205.1246537396122 L 450.0 194.5983379501385 L 460.0 182.96398891966757 L 470.0 170.22160664819947 L 480.0 156.37119113573411 L 490.0 141.41274238227149 L 500.0 125.34626038781163 L 510.0 108.17174515235459 L 520.0 89.889196675900322 L 530.0 70.498614958448783 L 540.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="350.0" cy="250.0" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="360.0" cy="249.4459833795014" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="370.0" cy="247.78393351800551" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="380.0" cy="245.01385041551248" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="390.0" cy="241.13573407202216" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="400.0" cy="236.14958448753461" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="410.0" cy="230.05540166204986" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="420.0" cy="222.85318559556785" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="430.0" cy="214.54293628808864" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="440.0" cy="205.1246537396122" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="450.0" cy="194.5983379501385" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="460.0" cy="182.96398891966757" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="470.0" cy="170.22160664819947" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="480.0" cy="156.37119113573411" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="490.0" cy="141.41274238227149" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="500.0" cy="125.34626038781163" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="510.0" cy="108.17174515235459" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="520.0" cy="89.889196675900322" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="530.0" cy="70.498614958448783" r="5.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="540.0" cy="50.0" r="5.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="tf0cc88776b8e4364b131da07f917ee14" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">10</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">15</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t5c2bf8ae2171480bac6061d0ca229a29" transform="translate(350.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="font-size:10.0px">0.0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="font-size:10.0px">0.5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="font-size:10.0px">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Plot Data", "names": ["x", "y0"], "id": "t697aa9eaa024490a84f558d4b52e53c0", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}, {"title": "Plot Data", "names": ["x", "y0"], "id": "t388f0aeda06a4732acef20492a2efd74", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#tdba1dd08bf4b48948604e34d9613214a .toyplot-mark-popup");
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
    
                var root_id = "tdba1dd08bf4b48948604e34d9613214a";
                var axes = {"t5b9ac7fc2684432a9790fcc2da30556e": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t5c2bf8ae2171480bac6061d0ca229a29": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tbc2c3d0eba0c41ecb201cd788e62d1ae": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tf0cc88776b8e4364b131da07f917ee14": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
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

    <div align="center" class="toyplot" id="t9f253d0c58934481b509c8d763e8797f"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t400d33f36f5e4e2685627349ded0389e" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t5e8627c839754dceb7f0820015abed06"><clipPath id="td84310c9ae004fc8b6d9d7458b004f5b"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#td84310c9ae004fc8b6d9d7458b004f5b)"><g class="toyplot-mark-Scatterplot" id="tf8fed45495864e8a9a3e9e3cd109ad07" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 50.0, 250.0)" x1="50.0" x2="50.0" y1="245.0" y2="255.0"></line><line transform="rotate(-45, 50.0, 250.0)" x1="45.0" x2="55.0" y1="250.0" y2="250.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 60.0, 249.4459833795014)" x1="60.0" x2="60.0" y1="244.4459833795014" y2="254.4459833795014"></line><line transform="rotate(-45, 60.0, 249.4459833795014)" x1="55.0" x2="65.0" y1="249.4459833795014" y2="249.4459833795014"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 70.0, 247.78393351800551)" x1="70.0" x2="70.0" y1="242.78393351800551" y2="252.78393351800551"></line><line transform="rotate(-45, 70.0, 247.78393351800551)" x1="65.0" x2="75.0" y1="247.78393351800551" y2="247.78393351800551"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 80.0, 245.01385041551248)" x1="80.0" x2="80.0" y1="240.01385041551248" y2="250.01385041551248"></line><line transform="rotate(-45, 80.0, 245.01385041551248)" x1="75.0" x2="85.0" y1="245.01385041551248" y2="245.01385041551248"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 90.0, 241.13573407202216)" x1="90.0" x2="90.0" y1="236.13573407202216" y2="246.13573407202216"></line><line transform="rotate(-45, 90.0, 241.13573407202216)" x1="85.0" x2="95.0" y1="241.13573407202216" y2="241.13573407202216"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 100.0, 236.14958448753461)" x1="100.0" x2="100.0" y1="231.14958448753461" y2="241.14958448753461"></line><line transform="rotate(-45, 100.0, 236.14958448753461)" x1="95.0" x2="105.0" y1="236.14958448753461" y2="236.14958448753461"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 110.0, 230.05540166204986)" x1="110.0" x2="110.0" y1="225.05540166204986" y2="235.05540166204986"></line><line transform="rotate(-45, 110.0, 230.05540166204986)" x1="105.0" x2="115.0" y1="230.05540166204986" y2="230.05540166204986"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 120.0, 222.85318559556785)" x1="120.0" x2="120.0" y1="217.85318559556785" y2="227.85318559556785"></line><line transform="rotate(-45, 120.0, 222.85318559556785)" x1="115.0" x2="125.0" y1="222.85318559556785" y2="222.85318559556785"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 130.0, 214.54293628808864)" x1="130.0" x2="130.0" y1="209.54293628808864" y2="219.54293628808864"></line><line transform="rotate(-45, 130.0, 214.54293628808864)" x1="125.0" x2="135.0" y1="214.54293628808864" y2="214.54293628808864"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 140.0, 205.1246537396122)" x1="140.0" x2="140.0" y1="200.1246537396122" y2="210.1246537396122"></line><line transform="rotate(-45, 140.0, 205.1246537396122)" x1="135.0" x2="145.0" y1="205.1246537396122" y2="205.1246537396122"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 150.0, 194.5983379501385)" x1="150.0" x2="150.0" y1="189.5983379501385" y2="199.5983379501385"></line><line transform="rotate(-45, 150.0, 194.5983379501385)" x1="145.0" x2="155.0" y1="194.5983379501385" y2="194.5983379501385"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 160.0, 182.96398891966757)" x1="160.0" x2="160.0" y1="177.96398891966757" y2="187.96398891966757"></line><line transform="rotate(-45, 160.0, 182.96398891966757)" x1="155.0" x2="165.0" y1="182.96398891966757" y2="182.96398891966757"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 170.0, 170.22160664819947)" x1="170.0" x2="170.0" y1="165.22160664819947" y2="175.22160664819947"></line><line transform="rotate(-45, 170.0, 170.22160664819947)" x1="165.0" x2="175.0" y1="170.22160664819947" y2="170.22160664819947"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 180.0, 156.37119113573411)" x1="180.0" x2="180.0" y1="151.37119113573411" y2="161.37119113573411"></line><line transform="rotate(-45, 180.0, 156.37119113573411)" x1="175.0" x2="185.0" y1="156.37119113573411" y2="156.37119113573411"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 190.0, 141.41274238227149)" x1="190.0" x2="190.0" y1="136.41274238227149" y2="146.41274238227149"></line><line transform="rotate(-45, 190.0, 141.41274238227149)" x1="185.0" x2="195.0" y1="141.41274238227149" y2="141.41274238227149"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 200.0, 125.34626038781163)" x1="200.0" x2="200.0" y1="120.34626038781163" y2="130.34626038781164"></line><line transform="rotate(-45, 200.0, 125.34626038781163)" x1="195.0" x2="205.0" y1="125.34626038781163" y2="125.34626038781163"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 210.0, 108.17174515235459)" x1="210.0" x2="210.0" y1="103.17174515235459" y2="113.17174515235459"></line><line transform="rotate(-45, 210.0, 108.17174515235459)" x1="205.0" x2="215.0" y1="108.17174515235459" y2="108.17174515235459"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 220.0, 89.889196675900322)" x1="220.0" x2="220.0" y1="84.889196675900322" y2="94.889196675900322"></line><line transform="rotate(-45, 220.0, 89.889196675900322)" x1="215.0" x2="225.0" y1="89.889196675900322" y2="89.889196675900322"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 230.0, 70.498614958448783)" x1="230.0" x2="230.0" y1="65.498614958448783" y2="75.498614958448783"></line><line transform="rotate(-45, 230.0, 70.498614958448783)" x1="225.0" x2="235.0" y1="70.498614958448783" y2="70.498614958448783"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 240.0, 50.0)" x1="240.0" x2="240.0" y1="45.0" y2="55.0"></line><line transform="rotate(-45, 240.0, 50.0)" x1="235.0" x2="245.0" y1="50.0" y2="50.0"></line></g></g></g></g><g class="toyplot-coordinates-Axis" id="t369db48bbeb44a5d97757ce2b423a0c4" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">10</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">15</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="te86e9c3220754ae2b52613ba2e8f54ee" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="font-size:10.0px">0.0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="font-size:10.0px">0.5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="font-size:10.0px">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t9b2e4a24535f432ab504d0a7cbff294a"><clipPath id="t97337aae6334410b91d5832bb9e6b92e"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#t97337aae6334410b91d5832bb9e6b92e)"><g class="toyplot-mark-Scatterplot" id="tb79b80da23664062a568f03c23f4ff88" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="345.0,255.0 350.0,245.0 355.0,255.0" transform="rotate(0, 350.0, 250.0)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="355.0,254.4459833795014 360.0,244.4459833795014 365.0,254.4459833795014" transform="rotate(0, 360.0, 249.4459833795014)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="365.0,252.78393351800551 370.0,242.78393351800551 375.0,252.78393351800551" transform="rotate(0, 370.0, 247.78393351800551)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="375.0,250.01385041551248 380.0,240.01385041551248 385.0,250.01385041551248" transform="rotate(0, 380.0, 245.01385041551248)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="385.0,246.13573407202216 390.0,236.13573407202216 395.0,246.13573407202216" transform="rotate(0, 390.0, 241.13573407202216)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="395.0,241.14958448753461 400.0,231.14958448753461 405.0,241.14958448753461" transform="rotate(0, 400.0, 236.14958448753461)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="405.0,235.05540166204986 410.0,225.05540166204986 415.0,235.05540166204986" transform="rotate(0, 410.0, 230.05540166204986)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="415.0,227.85318559556785 420.0,217.85318559556785 425.0,227.85318559556785" transform="rotate(0, 420.0, 222.85318559556785)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="425.0,219.54293628808864 430.0,209.54293628808864 435.0,219.54293628808864" transform="rotate(0, 430.0, 214.54293628808864)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="435.0,210.1246537396122 440.0,200.1246537396122 445.0,210.1246537396122" transform="rotate(0, 440.0, 205.1246537396122)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="445.0,199.5983379501385 450.0,189.5983379501385 455.0,199.5983379501385" transform="rotate(0, 450.0, 194.5983379501385)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="455.0,187.96398891966757 460.0,177.96398891966757 465.0,187.96398891966757" transform="rotate(0, 460.0, 182.96398891966757)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="465.0,175.22160664819947 470.0,165.22160664819947 475.0,175.22160664819947" transform="rotate(0, 470.0, 170.22160664819947)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="475.0,161.37119113573411 480.0,151.37119113573411 485.0,161.37119113573411" transform="rotate(0, 480.0, 156.37119113573411)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="485.0,146.41274238227149 490.0,136.41274238227149 495.0,146.41274238227149" transform="rotate(0, 490.0, 141.41274238227149)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="495.0,130.34626038781164 500.0,120.34626038781163 505.0,130.34626038781164" transform="rotate(0, 500.0, 125.34626038781163)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="505.0,113.17174515235459 510.0,103.17174515235459 515.0,113.17174515235459" transform="rotate(0, 510.0, 108.17174515235459)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="515.0,94.889196675900322 520.0,84.889196675900322 525.0,94.889196675900322" transform="rotate(0, 520.0, 89.889196675900322)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="525.0,75.498614958448783 530.0,65.498614958448783 535.0,75.498614958448783" transform="rotate(0, 530.0, 70.498614958448783)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="535.0,55.0 540.0,45.0 545.0,55.0" transform="rotate(0, 540.0, 50.0)"></polygon></g></g></g></g><g class="toyplot-coordinates-Axis" id="t96abdff602e44b9fb9b984688ab6d1fd" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">10</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">15</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tb922309a082642cbbed1f80d6cbb78c1" transform="translate(350.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="font-size:10.0px">0.0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="font-size:10.0px">0.5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="font-size:10.0px">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tf8fed45495864e8a9a3e9e3cd109ad07", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tb79b80da23664062a568f03c23f4ff88", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t9f253d0c58934481b509c8d763e8797f .toyplot-mark-popup");
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
    
                var root_id = "t9f253d0c58934481b509c8d763e8797f";
                var axes = {"t369db48bbeb44a5d97757ce2b423a0c4": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t96abdff602e44b9fb9b984688ab6d1fd": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tb922309a082642cbbed1f80d6cbb78c1": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "te86e9c3220754ae2b52613ba2e8f54ee": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
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

    <div align="center" class="toyplot" id="t3313645bcb1a4b1f8893adc678ba16de"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tc678aa612877400d99e499d69aee160b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t52da0fa1c3154125808d3e7156584333"><clipPath id="t0d6851478ab54644abf4058d3197cbf3"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t0d6851478ab54644abf4058d3197cbf3)"><g class="toyplot-mark-Plot" id="tb5280bd04eab45c0ae888b3328c787cf" style="fill:none;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><g class="toyplot-Series"><path d="M 50.0 250.0 L 60.0 249.4459833795014 L 70.0 247.78393351800551 L 80.0 245.01385041551248 L 90.0 241.13573407202216 L 100.0 236.14958448753461 L 110.0 230.05540166204986 L 120.0 222.85318559556785 L 130.0 214.54293628808864 L 140.0 205.1246537396122 L 150.0 194.5983379501385 L 160.0 182.96398891966757 L 170.0 170.22160664819947 L 180.0 156.37119113573411 L 190.0 141.41274238227149 L 200.0 125.34626038781163 L 210.0 108.17174515235459 L 220.0 89.889196675900322 L 230.0 70.498614958448783 L 240.0 50.0" style="stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="250.0" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="60.0" cy="249.4459833795014" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="70.0" cy="247.78393351800551" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.0" cy="245.01385041551248" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="90.0" cy="241.13573407202216" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="100.0" cy="236.14958448753461" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="110.0" cy="230.05540166204986" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="120.0" cy="222.85318559556785" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="130.0" cy="214.54293628808864" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="140.0" cy="205.1246537396122" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="150.0" cy="194.5983379501385" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="160.0" cy="182.96398891966757" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="170.0" cy="170.22160664819947" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="180.0" cy="156.37119113573411" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="190.0" cy="141.41274238227149" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="200.0" cy="125.34626038781163" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="210.0" cy="108.17174515235459" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="220.0" cy="89.889196675900322" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="230.0" cy="70.498614958448783" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="240.0" cy="50.0" r="4.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t8eba07ed418c46699de25ed9c724c9ec" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">10</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">15</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tfc105e232dd44456bfda3a3f49b4f12c" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="font-size:10.0px">0.0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="font-size:10.0px">0.5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="font-size:10.0px">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="tb00494510e754b338378971e445a05d2"><clipPath id="t6707ffe87fd94dfda93b32f0bb84ecc4"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#t6707ffe87fd94dfda93b32f0bb84ecc4)"><g class="toyplot-mark-Plot" id="t95423d2fe5c94b379ab141977dcdc042" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 250.0 L 360.0 249.4459833795014 L 370.0 247.78393351800551 L 380.0 245.01385041551248 L 390.0 241.13573407202216 L 400.0 236.14958448753461 L 410.0 230.05540166204986 L 420.0 222.85318559556785 L 430.0 214.54293628808864 L 440.0 205.1246537396122 L 450.0 194.5983379501385 L 460.0 182.96398891966757 L 470.0 170.22160664819947 L 480.0 156.37119113573411 L 490.0 141.41274238227149 L 500.0 125.34626038781163 L 510.0 108.17174515235459 L 520.0 89.889196675900322 L 530.0 70.498614958448783 L 540.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="350.0" cy="250.0" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="360.0" cy="249.4459833795014" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="370.0" cy="247.78393351800551" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="380.0" cy="245.01385041551248" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="390.0" cy="241.13573407202216" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="400.0" cy="236.14958448753461" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="410.0" cy="230.05540166204986" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="420.0" cy="222.85318559556785" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="430.0" cy="214.54293628808864" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="440.0" cy="205.1246537396122" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="450.0" cy="194.5983379501385" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="460.0" cy="182.96398891966757" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="470.0" cy="170.22160664819947" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="480.0" cy="156.37119113573411" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="490.0" cy="141.41274238227149" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="500.0" cy="125.34626038781163" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="510.0" cy="108.17174515235459" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="520.0" cy="89.889196675900322" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="530.0" cy="70.498614958448783" r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,39.2%,0%);stroke-opacity:1.0"><circle cx="540.0" cy="50.0" r="4.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="tf948667771334477b5e07083c657472b" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">10</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">15</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="td8bfa65a7f064a2096718d9dddf04a37" transform="translate(350.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="font-size:10.0px">0.0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="font-size:10.0px">0.5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="font-size:10.0px">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Plot Data", "names": ["x", "y0"], "id": "tb5280bd04eab45c0ae888b3328c787cf", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}, {"title": "Plot Data", "names": ["x", "y0"], "id": "t95423d2fe5c94b379ab141977dcdc042", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t3313645bcb1a4b1f8893adc678ba16de .toyplot-mark-popup");
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
    
                var root_id = "t3313645bcb1a4b1f8893adc678ba16de";
                var axes = {"t8eba07ed418c46699de25ed9c724c9ec": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "td8bfa65a7f064a2096718d9dddf04a37": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tf948667771334477b5e07083c657472b": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tfc105e232dd44456bfda3a3f49b4f12c": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
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

    <div align="center" class="toyplot" id="tacffb31c0fbc4bf2b725904fe52bc970"><svg class="toyplot-canvas-Canvas" height="200.0px" id="tf1628a3a6e5247f89c302c4c21d78c7a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 700.0 200.0" width="700.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tf5977dd46b9a4b1ba42f7c56ebf095ee"><clipPath id="tbb569616023d4bada46ecc77c06c1d4d"><rect height="120.0" width="620.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tbb569616023d4bada46ecc77c06c1d4d)"><g class="toyplot-mark-Scatterplot" id="t2aaf666217914257afbdf881a11b4ba6" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(0, 107.4074074074074, 125.0)" x1="107.4074074074074" x2="107.4074074074074" y1="117.5" y2="132.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(45, 135.18518518518519, 125.0)" x1="135.18518518518519" x2="135.18518518518519" y1="117.5" y2="132.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(-90, 162.96296296296296, 125.0)" x1="162.96296296296296" x2="162.96296296296296" y1="117.5" y2="132.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(-45, 190.74074074074073, 125.0)" x1="190.74074074074073" x2="190.74074074074073" y1="117.5" y2="132.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(0, 218.51851851851853, 125.0)" x1="218.51851851851853" x2="218.51851851851853" y1="117.5" y2="132.5"></line><line transform="rotate(0, 218.51851851851853, 125.0)" x1="211.01851851851853" x2="226.01851851851853" y1="125.0" y2="125.0"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(-45, 246.2962962962963, 125.0)" x1="246.2962962962963" x2="246.2962962962963" y1="117.5" y2="132.5"></line><line transform="rotate(-45, 246.2962962962963, 125.0)" x1="238.7962962962963" x2="253.7962962962963" y1="125.0" y2="125.0"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><line transform="rotate(0, 274.07407407407408, 125.0)" x1="274.07407407407408" x2="274.07407407407408" y1="117.5" y2="132.5"></line><line transform="rotate(60, 274.07407407407408, 125.0)" x1="274.07407407407408" x2="274.07407407407408" y1="117.5" y2="132.5"></line><line transform="rotate(-60, 274.07407407407408, 125.0)" x1="274.07407407407408" x2="274.07407407407408" y1="117.5" y2="132.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="294.3518518518519,132.5 301.8518518518519,117.5 309.3518518518519,132.5" transform="rotate(0, 301.8518518518519, 125.0)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="322.12962962962962,132.5 329.62962962962962,117.5 337.12962962962962,132.5" transform="rotate(90, 329.62962962962962, 125.0)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="349.90740740740745,132.5 357.40740740740745,117.5 364.90740740740745,132.5" transform="rotate(-180, 357.40740740740745, 125.0)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><polygon points="377.68518518518522,132.5 385.18518518518522,117.5 392.68518518518522,132.5" transform="rotate(-90, 385.18518518518522, 125.0)"></polygon></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><rect height="15.0" transform="rotate(0, 412.96296296296293, 125.0)" width="15.0" x="405.46296296296293" y="117.5"></rect></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><rect height="15.0" transform="rotate(-45, 440.74074074074076, 125.0)" width="15.0" x="433.24074074074076" y="117.5"></rect></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="468.51851851851859" cy="125.0" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="496.29629629629636" cy="125.0" r="7.5"></circle><circle cx="496.29629629629636" cy="125.0" r="3.75"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="524.07407407407413" cy="125.0" r="7.5"></circle><line transform="rotate(0, 524.07407407407413, 125.0)" x1="524.07407407407413" x2="524.07407407407413" y1="117.5" y2="132.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="551.85185185185185" cy="125.0" r="7.5"></circle><line transform="rotate(-90, 551.85185185185185, 125.0)" x1="551.85185185185185" x2="551.85185185185185" y1="117.5" y2="132.5"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="579.62962962962968" cy="125.0" r="7.5"></circle><line transform="rotate(0, 579.62962962962968, 125.0)" x1="579.62962962962968" x2="579.62962962962968" y1="117.5" y2="132.5"></line><line transform="rotate(0, 579.62962962962968, 125.0)" x1="572.12962962962968" x2="587.12962962962968" y1="125.0" y2="125.0"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="607.4074074074075" cy="125.0" r="7.5"></circle><line transform="rotate(-45, 607.4074074074075, 125.0)" x1="607.4074074074075" x2="607.4074074074075" y1="117.5" y2="132.5"></line><line transform="rotate(-45, 607.4074074074075, 125.0)" x1="599.9074074074075" x2="614.9074074074075" y1="125.0" y2="125.0"></line></g><g class="toyplot-Datum" style="fill:rgb(100%,93.3%,73.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0"><circle cx="635.18518518518522" cy="125.0" r="7.5"></circle><line transform="rotate(0, 635.18518518518522, 125.0)" x1="635.18518518518522" x2="635.18518518518522" y1="117.5" y2="132.5"></line><line transform="rotate(60, 635.18518518518522, 125.0)" x1="635.18518518518522" x2="635.18518518518522" y1="117.5" y2="132.5"></line><line transform="rotate(-60, 635.18518518518522, 125.0)" x1="635.18518518518522" x2="635.18518518518522" y1="117.5" y2="132.5"></line></g></g></g><g class="toyplot-mark-Text" id="t7a8cf3afafeb425aaba1adbc0714d7ed" style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-size:16px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(79.629629629629633,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">None</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(107.4074074074074,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">|</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(135.18518518518519,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">/</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(162.96296296296296,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">-</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(190.74074074074073,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">\</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(218.51851851851853,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">+</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(246.2962962962963,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">x</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(274.07407407407408,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">*</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(301.8518518518519,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">^</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(329.62962962962962,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">&gt;</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(357.40740740740745,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">v</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(385.18518518518522,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">&lt;</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(412.96296296296293,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">s</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(440.74074074074076,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">d</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(468.51851851851859,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">o</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(496.29629629629636,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">oo</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(524.07407407407413,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">o|</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(551.85185185185185,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">o-</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(579.62962962962968,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">o+</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(607.4074074074075,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">ox</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:monospace;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(635.18518518518522,75.0)translate(0,4.5)"><tspan style="font-size:16.0px">o*</tspan></text></g></g></g><text style="font-weight:bold;stroke:none;text-anchor:middle" transform="translate(350.0,50.0)translate(0,-10.0625)"><tspan style="font-size:14.0px">Marker Codes and Shapes</tspan></text></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t2aaf666217914257afbdf881a11b4ba6", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#tacffb31c0fbc4bf2b725904fe52bc970 .toyplot-mark-popup");
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

    <div align="center" class="toyplot" id="t422f14956ca84b91a6858516e2da5e74"><svg class="toyplot-canvas-Canvas" height="300.0px" id="te14920206e8a47d3a23c2f327c8d164e" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="ta9efc4a8e18d44ba9130e3262d89c9d8"><clipPath id="t5dbcda0ed8d04fd1991a01f0f8988dff"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t5dbcda0ed8d04fd1991a01f0f8988dff)"><g class="toyplot-mark-Scatterplot" id="tcf61e1a105a3489a8f6bebda09e3802f" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 50.0, 250.0)" x1="50.0" x2="50.0" y1="245.0" y2="255.0"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 60.0, 249.4459833795014)" x1="60.0" x2="60.0" y1="244.4459833795014" y2="254.4459833795014"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 70.0, 247.78393351800551)" x1="70.0" x2="70.0" y1="242.78393351800551" y2="252.78393351800551"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 80.0, 245.01385041551248)" x1="80.0" x2="80.0" y1="240.01385041551248" y2="250.01385041551248"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 90.0, 241.13573407202216)" x1="90.0" x2="90.0" y1="236.13573407202216" y2="246.13573407202216"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 100.0, 236.14958448753461)" x1="100.0" x2="100.0" y1="231.14958448753461" y2="241.14958448753461"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 110.0, 230.05540166204986)" x1="110.0" x2="110.0" y1="225.05540166204986" y2="235.05540166204986"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 120.0, 222.85318559556785)" x1="120.0" x2="120.0" y1="217.85318559556785" y2="227.85318559556785"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 130.0, 214.54293628808864)" x1="130.0" x2="130.0" y1="209.54293628808864" y2="219.54293628808864"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 140.0, 205.1246537396122)" x1="140.0" x2="140.0" y1="200.1246537396122" y2="210.1246537396122"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 150.0, 194.5983379501385)" x1="150.0" x2="150.0" y1="189.5983379501385" y2="199.5983379501385"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 160.0, 182.96398891966757)" x1="160.0" x2="160.0" y1="177.96398891966757" y2="187.96398891966757"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 170.0, 170.22160664819947)" x1="170.0" x2="170.0" y1="165.22160664819947" y2="175.22160664819947"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 180.0, 156.37119113573411)" x1="180.0" x2="180.0" y1="151.37119113573411" y2="161.37119113573411"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 190.0, 141.41274238227149)" x1="190.0" x2="190.0" y1="136.41274238227149" y2="146.41274238227149"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 200.0, 125.34626038781163)" x1="200.0" x2="200.0" y1="120.34626038781163" y2="130.34626038781164"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 210.0, 108.17174515235459)" x1="210.0" x2="210.0" y1="103.17174515235459" y2="113.17174515235459"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 220.0, 89.889196675900322)" x1="220.0" x2="220.0" y1="84.889196675900322" y2="94.889196675900322"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 230.0, 70.498614958448783)" x1="230.0" x2="230.0" y1="65.498614958448783" y2="75.498614958448783"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(-45, 240.0, 50.0)" x1="240.0" x2="240.0" y1="45.0" y2="55.0"></line></g></g></g></g><g class="toyplot-coordinates-Axis" id="t17a0e6f6a7f044eebe1057b083fec8c0" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">10</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">15</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tc72eb073b4fd4846b93b06e5d680a988" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="font-size:10.0px">0.0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="font-size:10.0px">0.5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="font-size:10.0px">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t41c1ed6c7cc346e0a7c9d01e0064c78a"><clipPath id="te92ed4869c1e4dcd97e90cc279643162"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#te92ed4869c1e4dcd97e90cc279643162)"><g class="toyplot-mark-Scatterplot" id="t1407690c797c4f8fb1f16e669281ea60" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="350.0" cy="250.0" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(350.0,250.0)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="360.0" cy="249.4459833795014" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(360.0,249.4459833795014)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="370.0" cy="247.78393351800551" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(370.0,247.78393351800551)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="380.0" cy="245.01385041551248" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(380.0,245.01385041551248)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="390.0" cy="241.13573407202216" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(390.0,241.13573407202216)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="400.0" cy="236.14958448753461" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(400.0,236.14958448753461)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="410.0" cy="230.05540166204986" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(410.0,230.05540166204986)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="420.0" cy="222.85318559556785" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(420.0,222.85318559556785)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="430.0" cy="214.54293628808864" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(430.0,214.54293628808864)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="440.0" cy="205.1246537396122" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(440.0,205.1246537396122)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="450.0" cy="194.5983379501385" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(450.0,194.5983379501385)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="460.0" cy="182.96398891966757" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(460.0,182.96398891966757)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="470.0" cy="170.22160664819947" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(470.0,170.22160664819947)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="480.0" cy="156.37119113573411" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(480.0,156.37119113573411)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="490.0" cy="141.41274238227149" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(490.0,141.41274238227149)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="500.0" cy="125.34626038781163" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(500.0,125.34626038781163)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="510.0" cy="108.17174515235459" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(510.0,108.17174515235459)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="520.0" cy="89.889196675900322" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(520.0,89.889196675900322)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="530.0" cy="70.498614958448783" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(530.0,70.498614958448783)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="540.0" cy="50.0" r="7.5"></circle><text style="fill:rgb(100%,100%,100%);fill-opacity:1.0;stroke:none;text-anchor:middle" transform="translate(540.0,50.0)translate(0,3.1640625)"><tspan style="font-size:11.25px">A</tspan></text></g></g></g></g><g class="toyplot-coordinates-Axis" id="t333532779138438999e153be148c3c10" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="190.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">10</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">15</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t7e9c1426b31e4c5494f90dd88c6311dd" transform="translate(350.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="font-size:10.0px">0.0</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="font-size:10.0px">0.5</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="font-size:10.0px">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tcf61e1a105a3489a8f6bebda09e3802f", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t1407690c797c4f8fb1f16e669281ea60", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t422f14956ca84b91a6858516e2da5e74 .toyplot-mark-popup");
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
    
                var root_id = "t422f14956ca84b91a6858516e2da5e74";
                var axes = {"t17a0e6f6a7f044eebe1057b083fec8c0": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t333532779138438999e153be148c3c10": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t7e9c1426b31e4c5494f90dd88c6311dd": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tc72eb073b4fd4846b93b06e5d680a988": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Using the full marker specification allows you to control the style and
appearance of individual markers, if needed.
