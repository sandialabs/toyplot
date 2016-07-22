
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _units:

Units
-----

There are several places in Toyplot where you will need to specify
quantities with real-world units, including canvas dimensions, font
sizes, and target dimensions for document-oriented backends such as
:mod:`toyplot.pdf`. For example, when creating a canvas, whether
explicitly or implicitly through the :ref:`convenience-api`, you could
specify its width and height in inches:

.. code:: python

    import numpy
    x = numpy.linspace(0, 1)
    y = x ** 2

.. code:: python

    import toyplot
    toyplot.plot(x, y, width="3in", height="2in");



.. raw:: html

    <div align="center" class="toyplot" id="t8521d513a1234cd697e7d7e4938b09d7"><svg class="toyplot-canvas-Canvas" height="192.0px" id="t272f93dd89e441018f7edab70e3c5099" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 288.0 192.0" width="288.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t4265108afbb44211a09a813fc29d1ac1"><clipPath id="tb825abe3024740f7a556fa726d58b009"><rect height="112.0" width="208.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tb825abe3024740f7a556fa726d58b009)"><g class="toyplot-mark-Plot" id="t77e1d5d6c5084b8f88b3b8239dfcbfd5" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 142.0 L 53.836734693877546 141.96168263223655 L 57.673469387755098 141.84673052894627 L 61.510204081632651 141.65514369012911 L 65.34693877551021 141.3869221157851 L 69.183673469387756 141.04206580591421 L 73.020408163265301 140.62057476051646 L 76.857142857142861 140.12244897959184 L 80.693877551020407 139.54768846314033 L 84.530612244897952 138.896293211162 L 88.367346938775512 138.16826322365682 L 92.204081632653057 137.36359850062473 L 96.040816326530603 136.48229904206579 L 99.877551020408163 135.52436484798002 L 103.71428571428572 134.48979591836735 L 107.55102040816325 133.37859225322782 L 111.38775510204081 132.19075385256144 L 115.22448979591837 130.92628071636818 L 119.0612244897959 129.58517284464804 L 122.89795918367346 128.16743023740108 L 126.73469387755102 126.67305289462725 L 130.57142857142856 125.10204081632654 L 134.40816326530611 123.45439400249897 L 138.24489795918367 121.73011245314453 L 142.08163265306123 119.92919616826322 L 145.91836734693877 118.05164514785506 L 149.7551020408163 116.09745939192003 L 153.59183673469389 114.06663890045814 L 157.42857142857144 111.9591836734694 L 161.26530612244898 109.77509371095375 L 165.10204081632651 107.5143690129113 L 168.93877551020407 105.17700957934194 L 172.77551020408163 102.76301541024573 L 176.61224489795919 100.27238650562266 L 180.44897959183672 97.705122865472717 L 184.28571428571425 95.061224489795933 L 188.12244897959181 92.340691378592254 L 191.95918367346937 89.543523531861737 L 195.79591836734693 86.66972094960434 L 199.63265306122446 83.71928363182009 L 203.46938775510205 80.692211578508974 L 207.30612244897958 77.588504789670978 L 211.14285714285714 74.408163265306129 L 214.9795918367347 71.151187005414414 L 218.81632653061223 67.817576009995861 L 222.65306122448979 64.407330279050413 L 226.48979591836735 60.920449812578106 L 230.32653061224488 57.356934610578932 L 234.16326530612244 53.716784673052899 L 238.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="tca3e9e7ef23c4b9099606ba4a40ec558" transform="translate(50.0,142.0)translate(0,10.0)"><line style="" x1="0" x2="188.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(94.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(188.0,6)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tb6f8d84797a4426792e72f77190895b0" transform="translate(50.0,142.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="92.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(46.0,-6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(92.0,-6)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Plot Data", "names": ["x", "y0"], "id": "t77e1d5d6c5084b8f88b3b8239dfcbfd5", "columns": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t8521d513a1234cd697e7d7e4938b09d7 .toyplot-mark-popup");
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
    
                var root_id = "t8521d513a1234cd697e7d7e4938b09d7";
                var axes = {"tb6f8d84797a4426792e72f77190895b0": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 92.0, "min": 0.0}, "scale": "linear"}], "tca3e9e7ef23c4b9099606ba4a40ec558": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 188.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


You can also specify the quantity and units separately:

.. code:: python

    toyplot.plot(x, y, width=(3, "in"), height=(2, "in"));



.. raw:: html

    <div align="center" class="toyplot" id="tf12ee894d44f41deb2b4d9e5cbda8e35"><svg class="toyplot-canvas-Canvas" height="192.0px" id="t379aacce3f86416dbf25439f2860750f" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 288.0 192.0" width="288.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t36de432d206c4294bf7074ed17ffeb43"><clipPath id="tb8f039587dc7493598591130c9fd743d"><rect height="112.0" width="208.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tb8f039587dc7493598591130c9fd743d)"><g class="toyplot-mark-Plot" id="tb71b6859d7e84e38853aeddda60604c3" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 142.0 L 53.836734693877546 141.96168263223655 L 57.673469387755098 141.84673052894627 L 61.510204081632651 141.65514369012911 L 65.34693877551021 141.3869221157851 L 69.183673469387756 141.04206580591421 L 73.020408163265301 140.62057476051646 L 76.857142857142861 140.12244897959184 L 80.693877551020407 139.54768846314033 L 84.530612244897952 138.896293211162 L 88.367346938775512 138.16826322365682 L 92.204081632653057 137.36359850062473 L 96.040816326530603 136.48229904206579 L 99.877551020408163 135.52436484798002 L 103.71428571428572 134.48979591836735 L 107.55102040816325 133.37859225322782 L 111.38775510204081 132.19075385256144 L 115.22448979591837 130.92628071636818 L 119.0612244897959 129.58517284464804 L 122.89795918367346 128.16743023740108 L 126.73469387755102 126.67305289462725 L 130.57142857142856 125.10204081632654 L 134.40816326530611 123.45439400249897 L 138.24489795918367 121.73011245314453 L 142.08163265306123 119.92919616826322 L 145.91836734693877 118.05164514785506 L 149.7551020408163 116.09745939192003 L 153.59183673469389 114.06663890045814 L 157.42857142857144 111.9591836734694 L 161.26530612244898 109.77509371095375 L 165.10204081632651 107.5143690129113 L 168.93877551020407 105.17700957934194 L 172.77551020408163 102.76301541024573 L 176.61224489795919 100.27238650562266 L 180.44897959183672 97.705122865472717 L 184.28571428571425 95.061224489795933 L 188.12244897959181 92.340691378592254 L 191.95918367346937 89.543523531861737 L 195.79591836734693 86.66972094960434 L 199.63265306122446 83.71928363182009 L 203.46938775510205 80.692211578508974 L 207.30612244897958 77.588504789670978 L 211.14285714285714 74.408163265306129 L 214.9795918367347 71.151187005414414 L 218.81632653061223 67.817576009995861 L 222.65306122448979 64.407330279050413 L 226.48979591836735 60.920449812578106 L 230.32653061224488 57.356934610578932 L 234.16326530612244 53.716784673052899 L 238.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="t2f644c59c49b48908ef6d053e68e96bc" transform="translate(50.0,142.0)translate(0,10.0)"><line style="" x1="0" x2="188.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(94.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(188.0,6)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="ta88c46137ac04b2b8455a90f1fba7a93" transform="translate(50.0,142.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="92.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(46.0,-6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(92.0,-6)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Plot Data", "names": ["x", "y0"], "id": "tb71b6859d7e84e38853aeddda60604c3", "columns": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#tf12ee894d44f41deb2b4d9e5cbda8e35 .toyplot-mark-popup");
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
    
                var root_id = "tf12ee894d44f41deb2b4d9e5cbda8e35";
                var axes = {"t2f644c59c49b48908ef6d053e68e96bc": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 188.0, "min": 0.0}, "scale": "linear"}], "ta88c46137ac04b2b8455a90f1fba7a93": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 92.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


If you rendered either plot using the PDF backend, the resulting
document size would be 3 inches × 2 inches.

If you don't specify any units, the canvas assumes a default unit of
*CSS pixels*:

.. code:: python

    toyplot.plot(x, y, width=600, height=400);



.. raw:: html

    <div align="center" class="toyplot" id="tac54077d0e3544e087f5887608548172"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t83a0a837279e4916ac974949c7b6c0a1" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 400.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t76286a7cade945e883c63af55570318f"><clipPath id="t0bf0e5569dae4d3484b9d55e72aaa3b7"><rect height="320.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t0bf0e5569dae4d3484b9d55e72aaa3b7)"><g class="toyplot-mark-Plot" id="ta2c84a29c6be485e882467c3c4a6448a" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 350.0 L 60.204081632653057 349.87505206164099 L 70.408163265306115 349.50020824656394 L 80.612244897959187 348.87546855476882 L 90.816326530612244 348.00083298625572 L 101.0204081632653 346.87630154102459 L 111.22448979591836 345.50187421907538 L 121.42857142857143 343.87755102040813 L 131.63265306122449 342.00333194502286 L 141.83673469387753 339.87921699291962 L 152.0408163265306 337.50520616409835 L 162.24489795918365 334.88129945855894 L 172.44897959183672 332.0074968763015 L 182.65306122448979 328.88379841732615 L 192.85714285714286 325.51020408163265 L 203.0612244897959 321.88671386922118 L 213.26530612244898 318.01332778009169 L 223.46938775510202 313.89004581424405 L 233.67346938775509 309.51686797167849 L 243.87755102040816 304.89379425239485 L 254.08163265306121 300.02082465639319 L 264.28571428571428 294.89795918367349 L 274.48979591836729 289.52519783423577 L 284.69387755102036 283.90254060807996 L 294.89795918367344 278.02998750520618 L 305.10204081632656 271.90753852561431 L 315.30612244897958 265.53519366930448 L 325.51020408163265 258.91295293627661 L 335.71428571428572 252.04081632653066 L 345.91836734693879 244.91878384006662 L 356.12244897959181 237.54685547688467 L 366.32653061224488 229.92503123698458 L 376.5306122448979 222.05331112036652 L 386.73469387755097 213.93169512703039 L 396.93877551020404 205.56018325697625 L 407.14285714285711 196.93877551020412 L 417.34693877551018 188.06747188671392 L 427.55102040816325 178.94627238650563 L 437.75510204081633 169.57517700957936 L 447.95918367346934 159.9541857559351 L 458.16326530612241 150.08329862557272 L 468.36734693877548 139.96251561849232 L 478.57142857142856 129.59183673469391 L 488.77551020408163 118.97126197417745 L 498.97959183673458 108.10079133694299 L 509.18367346938771 96.980424822990472 L 519.38775510204073 85.610162432319896 L 529.59183673469386 73.990004164931293 L 539.79591836734687 62.119950020824668 L 550.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="t998fc66ba66f4f23a7028078a0c201e7" transform="translate(50.0,350.0)translate(0,10.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(250.0,6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,6)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tca5525393fc149ed82c444bf57824672" transform="translate(50.0,350.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="300.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,-6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(300.0,-6)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Plot Data", "names": ["x", "y0"], "id": "ta2c84a29c6be485e882467c3c4a6448a", "columns": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#tac54077d0e3544e087f5887608548172 .toyplot-mark-popup");
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
    
                var root_id = "tac54077d0e3544e087f5887608548172";
                var axes = {"t998fc66ba66f4f23a7028078a0c201e7": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "tca5525393fc149ed82c444bf57824672": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 300.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Note: You're probably used to treating pixels as dimensionless; however
*CSS Pixels* are always 1/96th of an inch. Thus, the above example would
produce a PDF document that is 6.25 inches × 4.16 inches.

If you rendered the same canvas using the PNG, MP4, or WebM backends, it
would produce 600 × 400 pixel images / movies. Put another way, the
backends that produce raster images always assume 96 DPI, unless
overridden by the caller.

Allowed Units
~~~~~~~~~~~~~

The units and abbreviations currently understood by Toyplot are as
follows:

-  centimeters - "cm", "centimeter", "centimeters"
-  decimeters - "dm", "decimeter", "decimeters"
-  inches - "in", "inch", "inches"
-  meters - "m", "meter", "meters"
-  millimeters - "mm", "millimeter", "millimeters"
-  picas (1/6th of an inch) - "pc", "pica", "picas"
-  pixels (1/96th of an inch) - "px", "pixel", "pixels"
-  points (1/72nd of an inch) - "pt", "point", "points"

Functions that accept quantities with units as parameters will always
accept them in either of two forms:

-  A string that combines the value and unit abbreviations: "5in",
   "12px", "25.4mm".
-  A 2-tuple containing a number and string unit abbreviation: (5,
   "in"), (12, "px"), (25.4, "mm").

In addition, some functions will also accept a single numeric value,
with a documented default unit of measure (such as the canvas width and
height discussed above).

Further, some functions may accept quantities with "%" as the units. In
this case, the quantity will be relative to some other documented value.

Style Units
~~~~~~~~~~~

Toyplot style parameters always explicitly follow the CSS standard. As
such, they support a subset of unit abbreviations including "cm", "in",
"mm", "pc", "px", and "pt". Although CSS provides additional units for
relative dimensioning, they assume that the caller understands their
relationship to the underlying Document Object Model (DOM). Because
Toyplot does not expose the DOM to callers and may change it at any
time, these units are not supported.
