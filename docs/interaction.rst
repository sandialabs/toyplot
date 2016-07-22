
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _interaction:

Interaction
-----------

A key goal for the Toyplot team is to explore interactive features for
plots, making them truly useful and embeddable, so that they become a
ubiquitous part of every data graphic user's experience. The following
examples of interaction are just scratching the surface of what we have
planned for Toyplot:

Titles
~~~~~~

Most of the visualization types in Toyplot accept a ``title`` parameter,
allowing you to specify per-series or per-datum titles for a figure.
With Toyplot's preferred embeddable HTML output, those titles are
displayed via a popup when hovering over the data. For example, the
following figure has a global title "Employee Schedule", which you
should see as a popup when you hover the mouse over any of the bars:

.. code:: python

    import numpy
    numpy.random.seed(1234)
    start = numpy.random.normal(loc=8, scale=1, size=20)
    end = numpy.random.normal(loc=16, scale=1, size=20)
    boundaries = numpy.column_stack((start, end))
    title = "Employee Schedule"

.. code:: python

    import toyplot
    toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="t61f270242319467d87beefd9bd53ebb4"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t8a2631669c344d9cb7024f1a8e5f1d32" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t49d91494f37f443cae938d92bf769234"><clipPath id="tcf726f4413df40c08a2bb3f48dc6d4a7"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tcf726f4413df40c08a2bb3f48dc6d4a7)"><g class="toyplot-mark-BarBoundaries" id="t2126a5c21be6416483dd4685b4c25b4c" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="97.678913488510986" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="113.80008467423374" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="112.07959125518579"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="90.14285877392345" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="100.7543816470619"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="118.2145440939794" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.954147853910101"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="133.84987050060198" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="85.757979277598182"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="88.580423666484819" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="109.59073712941199"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="104.21287561873288" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="94.325945531701564"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="90.926617037695365" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="104.01593450275429" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="105.77478053571998"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="150.68872189008744" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="89.213744165717998"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="86.02832062773588" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="108.6378697093332"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="97.939888416950595" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="98.834164618480372"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="107.92339259707052" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="89.365619028097058"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="147.56257434430179" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="89.387489924964484"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="122.63726209990583" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="91.817102777535467"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="105.01053413958454" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="102.92346056264034" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="101.67049394975712"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="98.50817671215556" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="107.63726407477729"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="100.27355361155676" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="92.111003826718104"><title>Employee Schedule</title></rect><rect class="toyplot-Datum" height="159.17154758256362" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="71.45385979382624"><title>Employee Schedule</title></rect></g></g></g><g class="toyplot-coordinates-Axis" id="t94077b4114e34ddc855426101cb93316" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(9.75609756097561,6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(204.8780487804878,6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,6)"><tspan style="dominant-baseline:inherit">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t1ae5c928575e49a9a3561f5c3e0b398c" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,-6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,-6)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Bar Data", "names": ["left", "right", "boundary1"], "id": "t2126a5c21be6416483dd4685b4c25b4c", "columns": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t61f270242319467d87beefd9bd53ebb4 .toyplot-mark-popup");
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
    
                var root_id = "t61f270242319467d87beefd9bd53ebb4";
                var axes = {"t1ae5c928575e49a9a3561f5c3e0b398c": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t94077b4114e34ddc855426101cb93316": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 400.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


If your plot includes multiple series, you can assign a per-series title
instead. Hover the mouse over both series in the following plot to see
"Morning Schedule" and "Afternoon Schedule":

.. code:: python

    lunch = numpy.random.normal(loc=12, scale=0.5, size=20)
    boundaries = numpy.column_stack((start, lunch, end))
    title = ["Morning Schedule", "Afternoon Schedule"]
    
    toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="t289790a81eba484796a67007d9b6ef0c"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t685b05640ea6468c9442ed9cd67ad018" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tbfd56ac7ce414ab08e62b9bca90e0f0a"><clipPath id="td09442fceeda485497d7ec35af78d5cd"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#td09442fceeda485497d7ec35af78d5cd)"><g class="toyplot-mark-BarBoundaries" id="t62efa82b5f864992ba4d9b8d0d0a9a54" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="47.555528402481684" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="156.1586694144184"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="65.436703059653155" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="160.44297286976638"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="34.471519998879188" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="156.42572042210617"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="43.668841276622629" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="170.49985067126687"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="64.593131109857126" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="155.01471866834305"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="35.523448899632172" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="162.64771189626464"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="40.960188928692105" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="157.57863222174234"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="61.942241334559441" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="156.54473872433854"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="58.160141587795181" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="151.63057345067909"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="84.670923262268417" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="155.23154279353702"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="43.606248969945028" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="151.05994136712405"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="30.468652521802227" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="166.30540051362874"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="31.275856415161968" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="166.01315521000561"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="79.610609602940201" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="157.33945466632608"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="54.132748549528912" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="160.32161632791238"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="52.340958415090967" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="157.63079672246255"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="50.287423393725675" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="154.30653111867178"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="49.242020618411942" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="156.90342016852091"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="39.489479478692175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="152.89507795958269"><title>Morning Schedule</title></rect><rect class="toyplot-Datum" height="84.263132740560224" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="146.36227463582964"><title>Morning Schedule</title></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="50.123385086029302" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="48.363381614580589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="112.07959125518579"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="55.671338775044262" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="100.7543816470619"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="74.545702817356769" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.954147853910101"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="69.256739390744869" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="85.757979277598182"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="53.056974766852647" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="109.59073712941199"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="63.252686690040775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="94.325945531701564"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="28.984375703135925" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="45.85579291495911" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="105.77478053571998"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="66.017798627819019" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="89.213744165717998"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="42.422071657790852" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="108.6378697093332"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="67.471235895148368" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="98.834164618480372"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="76.647536181908549" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="89.365619028097058"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="67.951964741361593" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="89.387489924964484"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="68.504513550376913" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="91.817102777535467"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="52.669575724493569" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="52.636037168914669" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="101.67049394975712"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="49.266156093743618" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="107.63726407477729"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="60.784074132864589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="92.111003826718104"><title>Afternoon Schedule</title></rect><rect class="toyplot-Datum" height="74.908414842003396" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="71.45385979382624"><title>Afternoon Schedule</title></rect></g></g></g><g class="toyplot-coordinates-Axis" id="t55c96a16c7224bd2a1e3e7d2c290f59c" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(9.75609756097561,6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(204.8780487804878,6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,6)"><tspan style="dominant-baseline:inherit">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tb8e5e4129bbe4164a75df7786bec1e25" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,-6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,-6)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "t62efa82b5f864992ba4d9b8d0d0a9a54", "columns": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [12.038099793918619, 11.71677703476752, 12.018070968342036, 10.962511199654985, 12.123896099874273, 11.551421607780151, 11.931602583369326, 12.00914459567461, 12.377706991199068, 12.107634290484722, 12.420504397465695, 11.277094961477847, 11.299013359249578, 11.949540900025543, 11.725878775406573, 11.927690245815308, 12.177010166099619, 11.98224348736093, 12.282869153031298, 12.772829402312778], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t289790a81eba484796a67007d9b6ef0c .toyplot-mark-popup");
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
    
                var root_id = "t289790a81eba484796a67007d9b6ef0c";
                var axes = {"t55c96a16c7224bd2a1e3e7d2c290f59c": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 400.0, "min": 0.0}, "scale": "linear"}], "tb8e5e4129bbe4164a75df7786bec1e25": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Finally, you can assign a title for every datum:

.. code:: python

    title = numpy.column_stack((
            ["Employee %s Morning" % i for i in range(20)],
            ["Employee %s Afternoon" % i for i in range(20)]
            ))
    
    toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="t09e80c4dba3944c88e8395843b92bba1"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t986a622319824b238f11ae3a909238bc" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t1441c2c3f5904bb19dc15a29ddb92734"><clipPath id="tbdcb0b3716d24d26a54dec57abb1720d"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tbdcb0b3716d24d26a54dec57abb1720d)"><g class="toyplot-mark-BarBoundaries" id="t7a392d11ec9243debb2704d9249d5662" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="47.555528402481684" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="156.1586694144184"><title>Employee 0 Morning</title></rect><rect class="toyplot-Datum" height="65.436703059653155" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="160.44297286976638"><title>Employee 1 Morning</title></rect><rect class="toyplot-Datum" height="34.471519998879188" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="156.42572042210617"><title>Employee 2 Morning</title></rect><rect class="toyplot-Datum" height="43.668841276622629" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="170.49985067126687"><title>Employee 3 Morning</title></rect><rect class="toyplot-Datum" height="64.593131109857126" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="155.01471866834305"><title>Employee 4 Morning</title></rect><rect class="toyplot-Datum" height="35.523448899632172" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="162.64771189626464"><title>Employee 5 Morning</title></rect><rect class="toyplot-Datum" height="40.960188928692105" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="157.57863222174234"><title>Employee 6 Morning</title></rect><rect class="toyplot-Datum" height="61.942241334559441" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="156.54473872433854"><title>Employee 7 Morning</title></rect><rect class="toyplot-Datum" height="58.160141587795181" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="151.63057345067909"><title>Employee 8 Morning</title></rect><rect class="toyplot-Datum" height="84.670923262268417" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="155.23154279353702"><title>Employee 9 Morning</title></rect><rect class="toyplot-Datum" height="43.606248969945028" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="151.05994136712405"><title>Employee 10 Morning</title></rect><rect class="toyplot-Datum" height="30.468652521802227" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="166.30540051362874"><title>Employee 11 Morning</title></rect><rect class="toyplot-Datum" height="31.275856415161968" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="166.01315521000561"><title>Employee 12 Morning</title></rect><rect class="toyplot-Datum" height="79.610609602940201" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="157.33945466632608"><title>Employee 13 Morning</title></rect><rect class="toyplot-Datum" height="54.132748549528912" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="160.32161632791238"><title>Employee 14 Morning</title></rect><rect class="toyplot-Datum" height="52.340958415090967" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="157.63079672246255"><title>Employee 15 Morning</title></rect><rect class="toyplot-Datum" height="50.287423393725675" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="154.30653111867178"><title>Employee 16 Morning</title></rect><rect class="toyplot-Datum" height="49.242020618411942" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="156.90342016852091"><title>Employee 17 Morning</title></rect><rect class="toyplot-Datum" height="39.489479478692175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="152.89507795958269"><title>Employee 18 Morning</title></rect><rect class="toyplot-Datum" height="84.263132740560224" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="146.36227463582964"><title>Employee 19 Morning</title></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="50.123385086029302" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Employee 0 Afternoon</title></rect><rect class="toyplot-Datum" height="48.363381614580589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="112.07959125518579"><title>Employee 1 Afternoon</title></rect><rect class="toyplot-Datum" height="55.671338775044262" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="100.7543816470619"><title>Employee 2 Afternoon</title></rect><rect class="toyplot-Datum" height="74.545702817356769" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.954147853910101"><title>Employee 3 Afternoon</title></rect><rect class="toyplot-Datum" height="69.256739390744869" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="85.757979277598182"><title>Employee 4 Afternoon</title></rect><rect class="toyplot-Datum" height="53.056974766852647" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="109.59073712941199"><title>Employee 5 Afternoon</title></rect><rect class="toyplot-Datum" height="63.252686690040775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="94.325945531701564"><title>Employee 6 Afternoon</title></rect><rect class="toyplot-Datum" height="28.984375703135925" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Employee 7 Afternoon</title></rect><rect class="toyplot-Datum" height="45.85579291495911" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="105.77478053571998"><title>Employee 8 Afternoon</title></rect><rect class="toyplot-Datum" height="66.017798627819019" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="89.213744165717998"><title>Employee 9 Afternoon</title></rect><rect class="toyplot-Datum" height="42.422071657790852" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="108.6378697093332"><title>Employee 10 Afternoon</title></rect><rect class="toyplot-Datum" height="67.471235895148368" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="98.834164618480372"><title>Employee 11 Afternoon</title></rect><rect class="toyplot-Datum" height="76.647536181908549" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="89.365619028097058"><title>Employee 12 Afternoon</title></rect><rect class="toyplot-Datum" height="67.951964741361593" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="89.387489924964484"><title>Employee 13 Afternoon</title></rect><rect class="toyplot-Datum" height="68.504513550376913" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="91.817102777535467"><title>Employee 14 Afternoon</title></rect><rect class="toyplot-Datum" height="52.669575724493569" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Employee 15 Afternoon</title></rect><rect class="toyplot-Datum" height="52.636037168914669" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="101.67049394975712"><title>Employee 16 Afternoon</title></rect><rect class="toyplot-Datum" height="49.266156093743618" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="107.63726407477729"><title>Employee 17 Afternoon</title></rect><rect class="toyplot-Datum" height="60.784074132864589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="92.111003826718104"><title>Employee 18 Afternoon</title></rect><rect class="toyplot-Datum" height="74.908414842003396" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="71.45385979382624"><title>Employee 19 Afternoon</title></rect></g></g></g><g class="toyplot-coordinates-Axis" id="ta165bd25a039425db414335be62895df" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(9.75609756097561,6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(204.8780487804878,6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,6)"><tspan style="dominant-baseline:inherit">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t20c6dd1ca17747cca3d14b178940dab9" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,-6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,-6)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "t7a392d11ec9243debb2704d9249d5662", "columns": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [12.038099793918619, 11.71677703476752, 12.018070968342036, 10.962511199654985, 12.123896099874273, 11.551421607780151, 11.931602583369326, 12.00914459567461, 12.377706991199068, 12.107634290484722, 12.420504397465695, 11.277094961477847, 11.299013359249578, 11.949540900025543, 11.725878775406573, 11.927690245815308, 12.177010166099619, 11.98224348736093, 12.282869153031298, 12.772829402312778], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t09e80c4dba3944c88e8395843b92bba1 .toyplot-mark-popup");
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
    
                var root_id = "t09e80c4dba3944c88e8395843b92bba1";
                var axes = {"t20c6dd1ca17747cca3d14b178940dab9": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "ta165bd25a039425db414335be62895df": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 400.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Of course, the title attribute works with all types of visualizations.

Coordinates
~~~~~~~~~~~

When you click or tap the above figures, you should also see the domain
values for the point you chose displayed along each of the axes. If you
wish to disable display of either or both of the values, you can do so
using the individual axes:

.. code:: python

    canvas, axes, mark = toyplot.bars(boundaries, baseline=None, title=title, width=500, height=300)
    axes.x.interactive.coordinates.show = False
    axes.y.interactive.coordinates.show = False



.. raw:: html

    <div align="center" class="toyplot" id="t07d5e74dea354d0f997a20b08f9db9c7"><svg class="toyplot-canvas-Canvas" height="300.0px" id="td48b55f65c7543f6b6e8a15a495519a7" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t5c224013a5404b0a9451dda3b2c60da8"><clipPath id="t9ba5a0a8808846548abf08e25d1473f0"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t9ba5a0a8808846548abf08e25d1473f0)"><g class="toyplot-mark-BarBoundaries" id="t1fa1c0d6ee274076bda86e7c6c253a4a" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="47.555528402481684" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="156.1586694144184"><title>Employee 0 Morning</title></rect><rect class="toyplot-Datum" height="65.436703059653155" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="160.44297286976638"><title>Employee 1 Morning</title></rect><rect class="toyplot-Datum" height="34.471519998879188" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="156.42572042210617"><title>Employee 2 Morning</title></rect><rect class="toyplot-Datum" height="43.668841276622629" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="170.49985067126687"><title>Employee 3 Morning</title></rect><rect class="toyplot-Datum" height="64.593131109857126" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="155.01471866834305"><title>Employee 4 Morning</title></rect><rect class="toyplot-Datum" height="35.523448899632172" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="162.64771189626464"><title>Employee 5 Morning</title></rect><rect class="toyplot-Datum" height="40.960188928692105" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="157.57863222174234"><title>Employee 6 Morning</title></rect><rect class="toyplot-Datum" height="61.942241334559441" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="156.54473872433854"><title>Employee 7 Morning</title></rect><rect class="toyplot-Datum" height="58.160141587795181" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="151.63057345067909"><title>Employee 8 Morning</title></rect><rect class="toyplot-Datum" height="84.670923262268417" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="155.23154279353702"><title>Employee 9 Morning</title></rect><rect class="toyplot-Datum" height="43.606248969945028" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="151.05994136712405"><title>Employee 10 Morning</title></rect><rect class="toyplot-Datum" height="30.468652521802227" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="166.30540051362874"><title>Employee 11 Morning</title></rect><rect class="toyplot-Datum" height="31.275856415161968" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="166.01315521000561"><title>Employee 12 Morning</title></rect><rect class="toyplot-Datum" height="79.610609602940201" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="157.33945466632608"><title>Employee 13 Morning</title></rect><rect class="toyplot-Datum" height="54.132748549528912" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="160.32161632791238"><title>Employee 14 Morning</title></rect><rect class="toyplot-Datum" height="52.340958415090967" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="157.63079672246255"><title>Employee 15 Morning</title></rect><rect class="toyplot-Datum" height="50.287423393725675" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="154.30653111867178"><title>Employee 16 Morning</title></rect><rect class="toyplot-Datum" height="49.242020618411942" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="156.90342016852091"><title>Employee 17 Morning</title></rect><rect class="toyplot-Datum" height="39.489479478692175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="152.89507795958269"><title>Employee 18 Morning</title></rect><rect class="toyplot-Datum" height="84.263132740560224" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="146.36227463582964"><title>Employee 19 Morning</title></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="50.123385086029302" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Employee 0 Afternoon</title></rect><rect class="toyplot-Datum" height="48.363381614580589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="112.07959125518579"><title>Employee 1 Afternoon</title></rect><rect class="toyplot-Datum" height="55.671338775044262" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="100.7543816470619"><title>Employee 2 Afternoon</title></rect><rect class="toyplot-Datum" height="74.545702817356769" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.954147853910101"><title>Employee 3 Afternoon</title></rect><rect class="toyplot-Datum" height="69.256739390744869" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="85.757979277598182"><title>Employee 4 Afternoon</title></rect><rect class="toyplot-Datum" height="53.056974766852647" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="109.59073712941199"><title>Employee 5 Afternoon</title></rect><rect class="toyplot-Datum" height="63.252686690040775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="94.325945531701564"><title>Employee 6 Afternoon</title></rect><rect class="toyplot-Datum" height="28.984375703135925" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Employee 7 Afternoon</title></rect><rect class="toyplot-Datum" height="45.85579291495911" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="105.77478053571998"><title>Employee 8 Afternoon</title></rect><rect class="toyplot-Datum" height="66.017798627819019" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="89.213744165717998"><title>Employee 9 Afternoon</title></rect><rect class="toyplot-Datum" height="42.422071657790852" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="108.6378697093332"><title>Employee 10 Afternoon</title></rect><rect class="toyplot-Datum" height="67.471235895148368" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="98.834164618480372"><title>Employee 11 Afternoon</title></rect><rect class="toyplot-Datum" height="76.647536181908549" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="89.365619028097058"><title>Employee 12 Afternoon</title></rect><rect class="toyplot-Datum" height="67.951964741361593" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="89.387489924964484"><title>Employee 13 Afternoon</title></rect><rect class="toyplot-Datum" height="68.504513550376913" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="91.817102777535467"><title>Employee 14 Afternoon</title></rect><rect class="toyplot-Datum" height="52.669575724493569" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Employee 15 Afternoon</title></rect><rect class="toyplot-Datum" height="52.636037168914669" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="101.67049394975712"><title>Employee 16 Afternoon</title></rect><rect class="toyplot-Datum" height="49.266156093743618" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="107.63726407477729"><title>Employee 17 Afternoon</title></rect><rect class="toyplot-Datum" height="60.784074132864589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="92.111003826718104"><title>Employee 18 Afternoon</title></rect><rect class="toyplot-Datum" height="74.908414842003396" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="71.45385979382624"><title>Employee 19 Afternoon</title></rect></g></g></g><g class="toyplot-coordinates-Axis" id="tf933ea11799545c9a65f2186aaedb665" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(9.75609756097561,6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(204.8780487804878,6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,6)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g><g class="toyplot-coordinates-Axis" id="t5f11c0ad0f9b4974aa43f0c823bd9e95" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,-6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,-6)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">20</tspan></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "t1fa1c0d6ee274076bda86e7c6c253a4a", "columns": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [12.038099793918619, 11.71677703476752, 12.018070968342036, 10.962511199654985, 12.123896099874273, 11.551421607780151, 11.931602583369326, 12.00914459567461, 12.377706991199068, 12.107634290484722, 12.420504397465695, 11.277094961477847, 11.299013359249578, 11.949540900025543, 11.725878775406573, 11.927690245815308, 12.177010166099619, 11.98224348736093, 12.282869153031298, 12.772829402312778], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t07d5e74dea354d0f997a20b08f9db9c7 .toyplot-mark-popup");
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
    
                var root_id = "t07d5e74dea354d0f997a20b08f9db9c7";
                var axes = {"t5f11c0ad0f9b4974aa43f0c823bd9e95": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tf933ea11799545c9a65f2186aaedb665": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 400.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Now when you click or tap, nothing happens.

Data Export
~~~~~~~~~~~

If you right-click the mouse over any of the above plots, a small popup
menu will appear, giving you the option to "Save as .csv". If you choose
that option, the raw data from the plot will be extracted in CSV format
and you can save it.

Note that different browsers, browser versions, and platforms will
behave differently when extracting the file:

-  Safari on OSX will open the file in a separate tab, which you can
   save to disk using ``File > Save As``.
-  Chrome on OSX will immediately open a file dialog, prompting you to
   save the file.
-  Firefox on OSX will prompt you to open the file with Microsoft Excel
   (if installed), or save it to disk.

Note that, on the browsers that support it, the default filename for the
saved data is ``toyplot.csv``. You can override this default on a
per-data-table basis by specifying the filename when you create your
figure. For example, when exporting data from the following figure
(again, for browsers that support setting a default filename), the
filename will default to ``employee-schedules.csv``:

.. code:: python

    toyplot.bars(boundaries, baseline=None, filename="employee-schedules", title=title, width=500, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="t09914dc8aed94e80b0a6bb245925ddc0"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t5e2a1e4f4128431a837bfc7a8ece4881" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 500.0 300.0" width="500.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t48b02e641dc54b11af19869a9fc343c0"><clipPath id="t17f3067111804169b8b7d724e58be095"><rect height="220.0" width="420.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t17f3067111804169b8b7d724e58be095)"><g class="toyplot-mark-BarBoundaries" id="t3bcb171c5edc4d53913de8c834dbc5cd" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="47.555528402481684" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="156.1586694144184"><title>Employee 0 Morning</title></rect><rect class="toyplot-Datum" height="65.436703059653155" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="160.44297286976638"><title>Employee 1 Morning</title></rect><rect class="toyplot-Datum" height="34.471519998879188" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="156.42572042210617"><title>Employee 2 Morning</title></rect><rect class="toyplot-Datum" height="43.668841276622629" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="170.49985067126687"><title>Employee 3 Morning</title></rect><rect class="toyplot-Datum" height="64.593131109857126" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="155.01471866834305"><title>Employee 4 Morning</title></rect><rect class="toyplot-Datum" height="35.523448899632172" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="162.64771189626464"><title>Employee 5 Morning</title></rect><rect class="toyplot-Datum" height="40.960188928692105" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="157.57863222174234"><title>Employee 6 Morning</title></rect><rect class="toyplot-Datum" height="61.942241334559441" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="156.54473872433854"><title>Employee 7 Morning</title></rect><rect class="toyplot-Datum" height="58.160141587795181" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="151.63057345067909"><title>Employee 8 Morning</title></rect><rect class="toyplot-Datum" height="84.670923262268417" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="155.23154279353702"><title>Employee 9 Morning</title></rect><rect class="toyplot-Datum" height="43.606248969945028" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="151.05994136712405"><title>Employee 10 Morning</title></rect><rect class="toyplot-Datum" height="30.468652521802227" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="166.30540051362874"><title>Employee 11 Morning</title></rect><rect class="toyplot-Datum" height="31.275856415161968" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="166.01315521000561"><title>Employee 12 Morning</title></rect><rect class="toyplot-Datum" height="79.610609602940201" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="157.33945466632608"><title>Employee 13 Morning</title></rect><rect class="toyplot-Datum" height="54.132748549528912" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="160.32161632791238"><title>Employee 14 Morning</title></rect><rect class="toyplot-Datum" height="52.340958415090967" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="157.63079672246255"><title>Employee 15 Morning</title></rect><rect class="toyplot-Datum" height="50.287423393725675" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="154.30653111867178"><title>Employee 16 Morning</title></rect><rect class="toyplot-Datum" height="49.242020618411942" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="156.90342016852091"><title>Employee 17 Morning</title></rect><rect class="toyplot-Datum" height="39.489479478692175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="152.89507795958269"><title>Employee 18 Morning</title></rect><rect class="toyplot-Datum" height="84.263132740560224" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="146.36227463582964"><title>Employee 19 Morning</title></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="50.123385086029302" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="50.0" y="106.0352843283891"><title>Employee 0 Afternoon</title></rect><rect class="toyplot-Datum" height="48.363381614580589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951223" x="69.512195121951223" y="112.07959125518579"><title>Employee 1 Afternoon</title></rect><rect class="toyplot-Datum" height="55.671338775044262" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="89.024390243902445" y="100.7543816470619"><title>Employee 2 Afternoon</title></rect><rect class="toyplot-Datum" height="74.545702817356769" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951237" x="108.53658536585365" y="95.954147853910101"><title>Employee 3 Afternoon</title></rect><rect class="toyplot-Datum" height="69.256739390744869" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="128.04878048780489" y="85.757979277598182"><title>Employee 4 Afternoon</title></rect><rect class="toyplot-Datum" height="53.056974766852647" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="147.5609756097561" y="109.59073712941199"><title>Employee 5 Afternoon</title></rect><rect class="toyplot-Datum" height="63.252686690040775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="167.07317073170731" y="94.325945531701564"><title>Employee 6 Afternoon</title></rect><rect class="toyplot-Datum" height="28.984375703135925" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="186.58536585365852" y="127.56036302120262"><title>Employee 7 Afternoon</title></rect><rect class="toyplot-Datum" height="45.85579291495911" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="206.09756097560978" y="105.77478053571998"><title>Employee 8 Afternoon</title></rect><rect class="toyplot-Datum" height="66.017798627819019" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="225.60975609756099" y="89.213744165717998"><title>Employee 9 Afternoon</title></rect><rect class="toyplot-Datum" height="42.422071657790852" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="245.1219512195122" y="108.6378697093332"><title>Employee 10 Afternoon</title></rect><rect class="toyplot-Datum" height="67.471235895148368" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="264.63414634146341" y="98.834164618480372"><title>Employee 11 Afternoon</title></rect><rect class="toyplot-Datum" height="76.647536181908549" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="284.14634146341461" y="89.365619028097058"><title>Employee 12 Afternoon</title></rect><rect class="toyplot-Datum" height="67.951964741361593" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="303.65853658536588" y="89.387489924964484"><title>Employee 13 Afternoon</title></rect><rect class="toyplot-Datum" height="68.504513550376913" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="323.17073170731709" y="91.817102777535467"><title>Employee 14 Afternoon</title></rect><rect class="toyplot-Datum" height="52.669575724493569" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="342.6829268292683" y="104.96122099796898"><title>Employee 15 Afternoon</title></rect><rect class="toyplot-Datum" height="52.636037168914669" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951152" x="362.19512195121956" y="101.67049394975712"><title>Employee 16 Afternoon</title></rect><rect class="toyplot-Datum" height="49.266156093743618" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951265" x="381.70731707317071" y="107.63726407477729"><title>Employee 17 Afternoon</title></rect><rect class="toyplot-Datum" height="60.784074132864589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="401.21951219512198" y="92.111003826718104"><title>Employee 18 Afternoon</title></rect><rect class="toyplot-Datum" height="74.908414842003396" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="19.512195121951208" x="420.73170731707319" y="71.45385979382624"><title>Employee 19 Afternoon</title></rect></g></g></g><g class="toyplot-coordinates-Axis" id="tfa7b8c0fa6564c77aa1cac40fb426294" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="390.2439024390244" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(9.75609756097561,6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(204.8780487804878,6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,6)"><tspan style="dominant-baseline:inherit">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t6d23eebe80004db09f1a9c33058caab2" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="10.097533944194598" x2="178.54614020617376" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,-6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,-6)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "t3bcb171c5edc4d53913de8c834dbc5cd", "columns": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5], [12.038099793918619, 11.71677703476752, 12.018070968342036, 10.962511199654985, 12.123896099874273, 11.551421607780151, 11.931602583369326, 12.00914459567461, 12.377706991199068, 12.107634290484722, 12.420504397465695, 11.277094961477847, 11.299013359249578, 11.949540900025543, 11.725878775406573, 11.927690245815308, 12.177010166099619, 11.98224348736093, 12.282869153031298, 12.772829402312778], [15.797353675370818, 15.344030655861067, 16.193421376470358, 16.553438910956743, 17.318151554180137, 15.5306947152941, 16.675554085122382, 14.182972773409803, 15.816891459821, 17.05896918757115, 15.60215977180001, 16.33743765361397, 17.04757857289272, 17.045938255627664, 16.86371729168484, 15.877908425152325, 16.124712953768217, 15.677205194391703, 16.84167471299614, 18.390960515463032]], "filename": "employee-schedules"}];
    
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
                  var popup = document.querySelector("#t09914dc8aed94e80b0a6bb245925ddc0 .toyplot-mark-popup");
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
    
                var root_id = "t09914dc8aed94e80b0a6bb245925ddc0";
                var axes = {"t6d23eebe80004db09f1a9c33058caab2": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 5.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tfa7b8c0fa6564c77aa1cac40fb426294": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 400.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Note that the filename you specify should not include a file extension,
as the file extension is added for you (and other file formats may
become available in the future).
