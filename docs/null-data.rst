
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _null-data:

Null Data
=========

"Never tell a lie" is an integral part of :ref:`ethos` - and Toyplot's
handling of null data is one of the ways that we honor it. Consider the
following data, in which several datums contain floating-point
`NaN <https://en.wikipedia.org/wiki/NaN>`__ values:

.. code:: python

    import numpy
    x = numpy.linspace(0, 2 * numpy.pi)
    y = numpy.sin(x)
    y[6:20] = numpy.nan

When we plot this data, Toyplot carefully takes the NaN values into
account:

.. code:: python

    import toyplot.data
    toyplot.plot(x, y, ymax=1, marker="o", width=600, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="td06636c62a9a48ca8107198fc8aba5ae"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t0b86f3d0ba434fd49121484bee9c73c5" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="td10d9ece000f4e2aa5979a7421089cb5"><clipPath id="td91960e6f7cf493a9872796c61dea8bb"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#td91960e6f7cf493a9872796c61dea8bb)"><g class="toyplot-mark-Plot" id="t55e8d8f06c984afba191889643668508" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 150.0 L 60.204081632653057 137.2122838315494 L 70.408163265306115 124.63454160904925 L 80.612244897959187 112.4732995120626 L 90.816326530612244 100.92824479960623 L 101.0204081632653 90.188946950878403 M 254.08163265306121 95.446509878945093 L 264.28571428571428 106.61162608824417 L 274.48979591836735 118.48917819763791 L 284.69387755102036 130.88413712986275 L 294.89795918367344 143.59297800192866 L 305.10204081632656 156.40702199807123 L 315.30612244897958 169.11586287013719 L 325.51020408163265 181.51082180236202 L 335.71428571428572 193.38837391175579 L 345.91836734693879 204.55349012105484 L 356.12244897959187 214.82283953077882 L 366.32653061224488 224.02779970753153 L 376.5306122448979 232.01722545969557 L 386.73469387755097 238.65993063730002 L 396.93877551020404 243.84684220497604 L 407.14285714285717 247.49279121818236 L 417.34693877551018 249.53791129491984 L 427.55102040816325 249.94862162006879 L 437.75510204081627 248.71817834144503 L 447.9591836734694 245.86678530366606 L 458.16326530612241 241.44126230158125 L 468.36734693877548 235.51427630053465 L 478.57142857142856 228.183148246803 L 488.77551020408157 219.56825506034869 L 498.97959183673464 209.81105304912163 L 509.18367346938771 199.07175520039385 L 519.38775510204073 187.52670048793749 L 529.59183673469374 175.36545839095083 L 539.79591836734687 162.78771616845069 L 550.0 150.00000000000003" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="150.0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="60.204081632653057" cy="137.2122838315494" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="70.408163265306115" cy="124.63454160904925" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.612244897959187" cy="112.4732995120626" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="90.816326530612244" cy="100.92824479960623" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="101.0204081632653" cy="90.188946950878403" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="254.08163265306121" cy="95.446509878945093" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="264.28571428571428" cy="106.61162608824417" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="274.48979591836735" cy="118.48917819763791" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="284.69387755102036" cy="130.88413712986275" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="294.89795918367344" cy="143.59297800192866" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="305.10204081632656" cy="156.40702199807123" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="315.30612244897958" cy="169.11586287013719" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="325.51020408163265" cy="181.51082180236202" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="335.71428571428572" cy="193.38837391175579" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="345.91836734693879" cy="204.55349012105484" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="356.12244897959187" cy="214.82283953077882" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="366.32653061224488" cy="224.02779970753153" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="376.5306122448979" cy="232.01722545969557" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="386.73469387755097" cy="238.65993063730002" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="396.93877551020404" cy="243.84684220497604" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="407.14285714285717" cy="247.49279121818236" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="417.34693877551018" cy="249.53791129491984" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="427.55102040816325" cy="249.94862162006879" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="437.75510204081627" cy="248.71817834144503" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="447.9591836734694" cy="245.86678530366606" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="458.16326530612241" cy="241.44126230158125" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="468.36734693877548" cy="235.51427630053465" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="478.57142857142856" cy="228.183148246803" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="488.77551020408157" cy="219.56825506034869" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="498.97959183673464" cy="209.81105304912163" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="509.18367346938771" cy="199.07175520039385" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="519.38775510204073" cy="187.52670048793749" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="529.59183673469374" cy="175.36545839095083" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="539.79591836734687" cy="162.78771616845069" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="550.0" cy="150.00000000000003" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t4ec802886c83441fad7df97fbed40cab" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(159.15494309189535,6)"><tspan style="dominant-baseline:inherit">2</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(318.3098861837907,6)"><tspan style="dominant-baseline:inherit">4</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(477.464829275686,6)"><tspan style="dominant-baseline:inherit">6</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tf8e106c506f143dc9753812dae51a8f4" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0.05137837993121064" x2="159.8110530491216" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">-1.0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,-6)"><tspan style="dominant-baseline:inherit">-0.5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="dominant-baseline:inherit">0.0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,-6)"><tspan style="dominant-baseline:inherit">0.5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">1.0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Plot Data", "names": ["x", "y0"], "id": "t55e8d8f06c984afba191889643668508", "columns": [[0.0, 0.1282282715750936, 0.2564565431501872, 0.38468481472528077, 0.5129130863003744, 0.6411413578754679, 0.7693696294505615, 0.8975979010256552, 1.0258261726007487, 1.1540544441758422, 1.2822827157509358, 1.4105109873260295, 1.538739258901123, 1.6669675304762166, 1.7951958020513104, 1.9234240736264039, 2.0516523452014974, 2.179880616776591, 2.3081088883516845, 2.436337159926778, 2.5645654315018716, 2.6927937030769655, 2.821021974652059, 2.9492502462271526, 3.077478517802246, 3.2057067893773397, 3.333935060952433, 3.4621633325275267, 3.5903916041026207, 3.7186198756777142, 3.8468481472528078, 3.9750764188279013, 4.103304690402995, 4.231532961978089, 4.359761233553182, 4.487989505128276, 4.616217776703369, 4.744446048278463, 4.872674319853556, 5.00090259142865, 5.129130863003743, 5.257359134578837, 5.385587406153931, 5.513815677729024, 5.642043949304118, 5.770272220879211, 5.898500492454305, 6.026728764029398, 6.154957035604492, 6.283185307179586], [0.0, 0.127877161684506, 0.25365458390950735, 0.3752670048793741, 0.49071755200393785, 0.5981105304912159, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 0.545534901210549, 0.43388373911755823, 0.3151082180236208, 0.19115862870137254, 0.06407021998071323, -0.06407021998071254, -0.19115862870137187, -0.3151082180236202, -0.433883739117558, -0.5455349012105485, -0.6482283953077882, -0.7402779970753153, -0.8201722545969556, -0.8865993063730001, -0.9384684220497602, -0.9749279121818235, -0.9953791129491981, -0.9994862162006879, -0.9871817834144503, -0.9586678530366608, -0.9144126230158128, -0.8551427630053465, -0.7818314824680299, -0.6956825506034869, -0.5981105304912162, -0.49071755200393863, -0.3752670048793746, -0.25365458390950835, -0.12787716168450664, -2.4492935982947064e-16]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#td06636c62a9a48ca8107198fc8aba5ae .toyplot-mark-popup");
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
    
                var root_id = "td06636c62a9a48ca8107198fc8aba5ae";
                var axes = {"t4ec802886c83441fad7df97fbed40cab": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 6.2831853071795862, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "tf8e106c506f143dc9753812dae51a8f4": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": -1.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Note that the Y axis domain reflects the lack of data where there are
NaN values, and there are no markers for the NaN datams. Note too that
the plot has been broken into two segments - drawing a segment through
the NaN region might mislead viewers about the shape of the curve, while
breaking the plot unambiguously communicates the absence of data.

Of course NaN values can only be used with floating-point arrays, so
there must be alternate ways to represent null values for other data
types such as integers. To address this, Toyplot uses `masked
arrays <http://docs.scipy.org/doc/numpy/reference/maskedarray.html>`__
for all its internal data structures, and accepts masked arrays for its
inputs, allowing you to define null values in your data explicitly:

.. code:: python

    numpy.random.seed(1234)
    y = numpy.ma.array(numpy.random.choice(numpy.arange(3, 10), size=50))
    y[5:15] = numpy.ma.masked
    toyplot.bars(y, width=600, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="t0bc9dfa104c74b9887e0cfeaef0be019"><svg class="toyplot-canvas-Canvas" height="300.0px" id="taeaa84840e804c15926dff23d2f911a0" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t04cf213ad6534552a09caf6ae8bcd7b2"><clipPath id="tc83c63ef57bd46eea5bb4051a3ee4bf8"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tc83c63ef57bd46eea5bb4051a3ee4bf8)"><g class="toyplot-mark-BarMagnitudes" id="td0841172cfaa44a38d69ff5bbd9ee967" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="133.33333333333331" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="50.0" y="116.66666666666667"></rect><rect class="toyplot-Datum" height="200.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="59.900990099009903" y="50.0"></rect><rect class="toyplot-Datum" height="177.77777777777777" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="69.801980198019805" y="72.222222222222229"></rect><rect class="toyplot-Datum" height="155.55555555555554" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="79.702970297029694" y="94.444444444444443"></rect><rect class="toyplot-Datum" height="155.55555555555554" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="89.603960396039611" y="94.444444444444443"></rect><rect class="toyplot-Datum" height="111.11111111111111" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="198.51485148514851" y="138.88888888888889"></rect><rect class="toyplot-Datum" height="200.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="208.41584158415844" y="50.0"></rect><rect class="toyplot-Datum" height="111.11111111111111" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="218.31683168316835" y="138.88888888888889"></rect><rect class="toyplot-Datum" height="66.666666666666657" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="228.21782178217819" y="183.33333333333334"></rect><rect class="toyplot-Datum" height="66.666666666666657" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="238.11881188118812" y="183.33333333333334"></rect><rect class="toyplot-Datum" height="155.55555555555554" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="248.01980198019803" y="94.444444444444443"></rect><rect class="toyplot-Datum" height="177.77777777777777" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="257.9207920792079" y="72.222222222222229"></rect><rect class="toyplot-Datum" height="66.666666666666657" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="267.82178217821786" y="183.33333333333334"></rect><rect class="toyplot-Datum" height="88.888888888888886" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="277.72277227722776" y="161.11111111111111"></rect><rect class="toyplot-Datum" height="200.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="287.62376237623761" y="50.0"></rect><rect class="toyplot-Datum" height="200.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="297.52475247524757" y="50.0"></rect><rect class="toyplot-Datum" height="111.11111111111111" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="307.42574257425741" y="138.88888888888889"></rect><rect class="toyplot-Datum" height="66.666666666666657" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="317.32673267326737" y="183.33333333333334"></rect><rect class="toyplot-Datum" height="133.33333333333331" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.900990099009789" x="327.22772277227727" y="116.66666666666667"></rect><rect class="toyplot-Datum" height="155.55555555555554" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="337.12871287128706" y="94.444444444444443"></rect><rect class="toyplot-Datum" height="177.77777777777777" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="347.02970297029702" y="72.222222222222229"></rect><rect class="toyplot-Datum" height="111.11111111111111" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="356.93069306930693" y="138.88888888888889"></rect><rect class="toyplot-Datum" height="200.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="366.83168316831689" y="50.0"></rect><rect class="toyplot-Datum" height="111.11111111111111" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="376.73267326732673" y="138.88888888888889"></rect><rect class="toyplot-Datum" height="133.33333333333331" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="386.63366336633669" y="116.66666666666667"></rect><rect class="toyplot-Datum" height="133.33333333333331" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="396.53465346534654" y="116.66666666666667"></rect><rect class="toyplot-Datum" height="66.666666666666657" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="406.43564356435638" y="183.33333333333334"></rect><rect class="toyplot-Datum" height="88.888888888888886" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="416.33663366336634" y="161.11111111111111"></rect><rect class="toyplot-Datum" height="133.33333333333331" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="426.23762376237624" y="116.66666666666667"></rect><rect class="toyplot-Datum" height="66.666666666666657" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="436.13861386138615" y="183.33333333333334"></rect><rect class="toyplot-Datum" height="133.33333333333331" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="446.03960396039605" y="116.66666666666667"></rect><rect class="toyplot-Datum" height="111.11111111111111" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="455.94059405940595" y="138.88888888888889"></rect><rect class="toyplot-Datum" height="133.33333333333331" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="465.84158415841586" y="116.66666666666667"></rect><rect class="toyplot-Datum" height="155.55555555555554" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="475.7425742574257" y="94.444444444444443"></rect><rect class="toyplot-Datum" height="88.888888888888886" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="485.64356435643566" y="161.11111111111111"></rect><rect class="toyplot-Datum" height="133.33333333333331" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="495.54455445544556" y="116.66666666666667"></rect><rect class="toyplot-Datum" height="133.33333333333331" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="505.44554455445547" y="116.66666666666667"></rect><rect class="toyplot-Datum" height="133.33333333333331" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="515.34653465346537" y="116.66666666666667"></rect><rect class="toyplot-Datum" height="111.11111111111111" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="525.24752475247521" y="138.88888888888889"></rect><rect class="toyplot-Datum" height="88.888888888888886" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="535.14851485148517" y="161.11111111111111"></rect></g></g></g><g class="toyplot-coordinates-Axis" id="t3696182266e44289b16a4730cefbceb0" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="495.049504950495" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(4.9504950495049505,6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(103.96039603960395,6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(202.97029702970298,6)"><tspan style="dominant-baseline:inherit">20</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(301.98019801980195,6)"><tspan style="dominant-baseline:inherit">30</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.99009900990103,6)"><tspan style="dominant-baseline:inherit">40</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,6)"><tspan style="dominant-baseline:inherit">50</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t6bd1716e0c47484cb5e5ad8a8c6d7260" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(66.66666666666666,-6)"><tspan style="dominant-baseline:inherit">3</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(133.33333333333331,-6)"><tspan style="dominant-baseline:inherit">6</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">9</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Bar Data", "names": ["left", "right", "baseline", "magnitude0"], "id": "td0841172cfaa44a38d69ff5bbd9ee967", "columns": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [6.0, 9.0, 8.0, 7.0, 7.0, null, null, null, null, null, null, null, null, null, null, 5.0, 9.0, 5.0, 3.0, 3.0, 7.0, 8.0, 3.0, 4.0, 9.0, 9.0, 5.0, 3.0, 6.0, 7.0, 8.0, 5.0, 9.0, 5.0, 6.0, 6.0, 3.0, 4.0, 6.0, 3.0, 6.0, 5.0, 6.0, 7.0, 4.0, 6.0, 6.0, 6.0, 5.0, 4.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t0bc9dfa104c74b9887e0cfeaef0be019 .toyplot-mark-popup");
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
    
                var root_id = "t0bc9dfa104c74b9887e0cfeaef0be019";
                var axes = {"t3696182266e44289b16a4730cefbceb0": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "t6bd1716e0c47484cb5e5ad8a8c6d7260": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 9.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


You might feel that masking null values in the above example is
needlessly complex, when a special value of "zero" could accomplish the
same thing. But consider what happens if there is more than one series:

.. code:: python

    magnitudes = numpy.ma.column_stack((
            numpy.random.choice(numpy.arange(5, 10), size=50),
            numpy.random.choice(numpy.arange(5, 10), size=50),
        ))
    magnitudes[5:15,0] = 0
    toyplot.bars(magnitudes, width=600, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="tff62dc77b7bb4ec5a460dd81efbeaf3a"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t14b7b61803184b83a5f46470b76e37e9" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t566957ce193a48d198cc632f9c39aa42"><clipPath id="t540d04ff48cb43278da29a328bfe92d6"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t540d04ff48cb43278da29a328bfe92d6)"><g class="toyplot-mark-BarMagnitudes" id="t6929de10fb65435db154f5a24ad44bb5" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="80.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="50.0" y="170.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="59.900990099009903" y="160.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="69.801980198019805" y="180.0"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="79.702970297029694" y="170.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="89.603960396039611" y="160.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="99.504950495049513" y="250.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="109.4059405940594" y="250.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="119.30693069306932" y="250.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="129.20792079207922" y="250.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="139.1089108910891" y="250.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="149.00990099009903" y="250.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="158.91089108910893" y="250.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="168.8118811881188" y="250.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="178.71287128712871" y="250.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="188.61386138613864" y="250.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="198.51485148514851" y="190.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="208.41584158415844" y="200.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="218.31683168316835" y="200.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="228.21782178217819" y="160.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="238.11881188118812" y="200.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="248.01980198019803" y="160.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="257.9207920792079" y="180.0"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="267.82178217821786" y="170.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="277.72277227722776" y="190.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="287.62376237623761" y="180.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="297.52475247524757" y="180.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="307.42574257425741" y="160.0"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="317.32673267326737" y="170.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.900990099009789" x="327.22772277227727" y="160.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="337.12871287128706" y="180.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="347.02970297029702" y="180.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="356.93069306930693" y="160.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="366.83168316831689" y="160.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="376.73267326732673" y="180.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="386.63366336633669" y="190.0"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="396.53465346534654" y="170.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="406.43564356435638" y="180.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="416.33663366336634" y="190.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="426.23762376237624" y="160.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="436.13861386138615" y="190.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="446.03960396039605" y="200.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="455.94059405940595" y="190.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="465.84158415841586" y="180.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="475.7425742574257" y="190.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="485.64356435643566" y="180.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="495.54455445544556" y="190.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="505.44554455445547" y="180.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="515.34653465346537" y="190.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="525.24752475247521" y="190.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="535.14851485148517" y="160.0"></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="59.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="50.0" y="110.00000000000001"></rect><rect class="toyplot-Datum" height="70.000000000000014" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="59.900990099009903" y="89.999999999999986"></rect><rect class="toyplot-Datum" height="90.000000000000014" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="69.801980198019805" y="89.999999999999986"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="79.702970297029694" y="120.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="89.603960396039611" y="70.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="99.504950495049513" y="190.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="109.4059405940594" y="180.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="119.30693069306932" y="190.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="129.20792079207922" y="190.0"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="139.1089108910891" y="170.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="149.00990099009903" y="160.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="158.91089108910893" y="190.0"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="168.8118811881188" y="170.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="178.71287128712871" y="180.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="188.61386138613864" y="200.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="198.51485148514851" y="100.0"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="208.41584158415844" y="120.0"></rect><rect class="toyplot-Datum" height="89.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="218.31683168316835" y="110.00000000000001"></rect><rect class="toyplot-Datum" height="49.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="228.21782178217819" y="110.00000000000001"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="238.11881188118812" y="150.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="248.01980198019803" y="70.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="257.9207920792079" y="130.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="267.82178217821786" y="80.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="277.72277227722776" y="130.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="287.62376237623761" y="130.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="297.52475247524757" y="120.0"></rect><rect class="toyplot-Datum" height="49.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="307.42574257425741" y="110.00000000000001"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="317.32673267326737" y="100.0"></rect><rect class="toyplot-Datum" height="49.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.900990099009789" x="327.22772277227727" y="110.00000000000001"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="337.12871287128706" y="100.0"></rect><rect class="toyplot-Datum" height="69.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="347.02970297029702" y="110.00000000000001"></rect><rect class="toyplot-Datum" height="70.000000000000014" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="356.93069306930693" y="89.999999999999986"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="366.83168316831689" y="80.0"></rect><rect class="toyplot-Datum" height="69.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="376.73267326732673" y="110.00000000000001"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="386.63366336633669" y="130.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="396.53465346534654" y="80.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="406.43564356435638" y="130.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="416.33663366336634" y="130.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="426.23762376237624" y="100.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="436.13861386138615" y="120.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="446.03960396039605" y="130.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="455.94059405940595" y="100.0"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="465.84158415841586" y="100.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="475.7425742574257" y="120.0"></rect><rect class="toyplot-Datum" height="90.000000000000014" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="485.64356435643566" y="89.999999999999986"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="495.54455445544556" y="130.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="505.44554455445547" y="130.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="515.34653465346537" y="140.0"></rect><rect class="toyplot-Datum" height="79.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="525.24752475247521" y="110.00000000000001"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="535.14851485148517" y="70.0"></rect></g></g></g><g class="toyplot-coordinates-Axis" id="ta6d53d1617ad4af8936ed0f47d7fb002" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="495.049504950495" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(4.9504950495049505,6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(103.96039603960395,6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(202.97029702970298,6)"><tspan style="dominant-baseline:inherit">20</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(301.98019801980195,6)"><tspan style="dominant-baseline:inherit">30</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.99009900990103,6)"><tspan style="dominant-baseline:inherit">40</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,6)"><tspan style="dominant-baseline:inherit">50</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tdda3d83ab2ef48f2b7d05c30b185b338" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="180.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,-6)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,-6)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Bar Data", "names": ["left", "right", "baseline", "magnitude0", "magnitude1"], "id": "t6929de10fb65435db154f5a24ad44bb5", "columns": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [8.0, 9.0, 7.0, 8.0, 9.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.0, 5.0, 5.0, 9.0, 5.0, 9.0, 7.0, 8.0, 6.0, 7.0, 7.0, 9.0, 8.0, 9.0, 7.0, 7.0, 9.0, 9.0, 7.0, 6.0, 8.0, 7.0, 6.0, 9.0, 6.0, 5.0, 6.0, 7.0, 6.0, 7.0, 6.0, 7.0, 6.0, 6.0, 9.0], [6.0, 7.0, 9.0, 5.0, 9.0, 6.0, 7.0, 6.0, 6.0, 8.0, 9.0, 6.0, 8.0, 7.0, 5.0, 9.0, 8.0, 9.0, 5.0, 5.0, 9.0, 5.0, 9.0, 6.0, 5.0, 6.0, 5.0, 7.0, 5.0, 8.0, 7.0, 7.0, 8.0, 7.0, 6.0, 9.0, 5.0, 6.0, 6.0, 7.0, 7.0, 9.0, 8.0, 7.0, 9.0, 6.0, 5.0, 5.0, 8.0, 9.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#tff62dc77b7bb4ec5a460dd81efbeaf3a .toyplot-mark-popup");
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
    
                var root_id = "tff62dc77b7bb4ec5a460dd81efbeaf3a";
                var axes = {"ta6d53d1617ad4af8936ed0f47d7fb002": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "tdda3d83ab2ef48f2b7d05c30b185b338": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


The position of the bars in the second series suggest that the null
values in the first series actually have a value of zero, when in
reality we want to communicate that they have no value at all. Contrast
this with what Toyplot produces when you correctly mark the values as
null instead of zero:

.. code:: python

    magnitudes[5:15,0] = numpy.ma.masked
    toyplot.bars(magnitudes, width=600, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="t52317048742148118f51c0b095bb32d3"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t045bb77017f9444e9eeb39c6b8c3f912" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t8f90926876984105be81133510460a87"><clipPath id="t36f4dfc2885d43bf9e05b741533815ff"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t36f4dfc2885d43bf9e05b741533815ff)"><g class="toyplot-mark-BarMagnitudes" id="t27bd38c92fd94cccb77daf9f5e624771" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="80.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="50.0" y="170.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="59.900990099009903" y="160.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="69.801980198019805" y="180.0"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="79.702970297029694" y="170.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="89.603960396039611" y="160.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="198.51485148514851" y="190.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="208.41584158415844" y="200.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="218.31683168316835" y="200.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="228.21782178217819" y="160.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="238.11881188118812" y="200.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="248.01980198019803" y="160.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="257.9207920792079" y="180.0"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="267.82178217821786" y="170.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="277.72277227722776" y="190.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="287.62376237623761" y="180.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="297.52475247524757" y="180.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="307.42574257425741" y="160.0"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="317.32673267326737" y="170.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.900990099009789" x="327.22772277227727" y="160.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="337.12871287128706" y="180.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="347.02970297029702" y="180.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="356.93069306930693" y="160.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="366.83168316831689" y="160.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="376.73267326732673" y="180.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="386.63366336633669" y="190.0"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="396.53465346534654" y="170.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="406.43564356435638" y="180.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="416.33663366336634" y="190.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="426.23762376237624" y="160.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="436.13861386138615" y="190.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="446.03960396039605" y="200.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="455.94059405940595" y="190.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="465.84158415841586" y="180.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="475.7425742574257" y="190.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="485.64356435643566" y="180.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="495.54455445544556" y="190.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="505.44554455445547" y="180.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="515.34653465346537" y="190.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="525.24752475247521" y="190.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="535.14851485148517" y="160.0"></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="59.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="50.0" y="110.00000000000001"></rect><rect class="toyplot-Datum" height="70.000000000000014" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="59.900990099009903" y="89.999999999999986"></rect><rect class="toyplot-Datum" height="90.000000000000014" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="69.801980198019805" y="89.999999999999986"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="79.702970297029694" y="120.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="89.603960396039611" y="70.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="198.51485148514851" y="100.0"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="208.41584158415844" y="120.0"></rect><rect class="toyplot-Datum" height="89.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="218.31683168316835" y="110.00000000000001"></rect><rect class="toyplot-Datum" height="49.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="228.21782178217819" y="110.00000000000001"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="238.11881188118812" y="150.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="248.01980198019803" y="70.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="257.9207920792079" y="130.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="267.82178217821786" y="80.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="277.72277227722776" y="130.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="287.62376237623761" y="130.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="297.52475247524757" y="120.0"></rect><rect class="toyplot-Datum" height="49.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="307.42574257425741" y="110.00000000000001"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="317.32673267326737" y="100.0"></rect><rect class="toyplot-Datum" height="49.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.900990099009789" x="327.22772277227727" y="110.00000000000001"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="337.12871287128706" y="100.0"></rect><rect class="toyplot-Datum" height="69.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="347.02970297029702" y="110.00000000000001"></rect><rect class="toyplot-Datum" height="70.000000000000014" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="356.93069306930693" y="89.999999999999986"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="366.83168316831689" y="80.0"></rect><rect class="toyplot-Datum" height="69.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="376.73267326732673" y="110.00000000000001"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="386.63366336633669" y="130.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="396.53465346534654" y="80.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="406.43564356435638" y="130.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="416.33663366336634" y="130.0"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="426.23762376237624" y="100.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="436.13861386138615" y="120.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="446.03960396039605" y="130.0"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="455.94059405940595" y="100.0"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="465.84158415841586" y="100.0"></rect><rect class="toyplot-Datum" height="70.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="475.7425742574257" y="120.0"></rect><rect class="toyplot-Datum" height="90.000000000000014" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="485.64356435643566" y="89.999999999999986"></rect><rect class="toyplot-Datum" height="60.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="495.54455445544556" y="130.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="505.44554455445547" y="130.0"></rect><rect class="toyplot-Datum" height="50.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="515.34653465346537" y="140.0"></rect><rect class="toyplot-Datum" height="79.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="525.24752475247521" y="110.00000000000001"></rect><rect class="toyplot-Datum" height="90.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="535.14851485148517" y="70.0"></rect></g></g></g><g class="toyplot-coordinates-Axis" id="tb269e8a5d9224d7a8bd35c8e5a44157d" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="495.049504950495" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(4.9504950495049505,6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(103.96039603960395,6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(202.97029702970298,6)"><tspan style="dominant-baseline:inherit">20</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(301.98019801980195,6)"><tspan style="dominant-baseline:inherit">30</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.99009900990103,6)"><tspan style="dominant-baseline:inherit">40</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,6)"><tspan style="dominant-baseline:inherit">50</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tdf3f0c5aded64af0b89d2a81a8f61db0" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="180.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,-6)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,-6)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Bar Data", "names": ["left", "right", "baseline", "magnitude0", "magnitude1"], "id": "t27bd38c92fd94cccb77daf9f5e624771", "columns": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [8.0, 9.0, 7.0, 8.0, 9.0, null, null, null, null, null, null, null, null, null, null, 6.0, 5.0, 5.0, 9.0, 5.0, 9.0, 7.0, 8.0, 6.0, 7.0, 7.0, 9.0, 8.0, 9.0, 7.0, 7.0, 9.0, 9.0, 7.0, 6.0, 8.0, 7.0, 6.0, 9.0, 6.0, 5.0, 6.0, 7.0, 6.0, 7.0, 6.0, 7.0, 6.0, 6.0, 9.0], [6.0, 7.0, 9.0, 5.0, 9.0, 6.0, 7.0, 6.0, 6.0, 8.0, 9.0, 6.0, 8.0, 7.0, 5.0, 9.0, 8.0, 9.0, 5.0, 5.0, 9.0, 5.0, 9.0, 6.0, 5.0, 6.0, 5.0, 7.0, 5.0, 8.0, 7.0, 7.0, 8.0, 7.0, 6.0, 9.0, 5.0, 6.0, 6.0, 7.0, 7.0, 9.0, 8.0, 7.0, 9.0, 6.0, 5.0, 5.0, 8.0, 9.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t52317048742148118f51c0b095bb32d3 .toyplot-mark-popup");
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
    
                var root_id = "t52317048742148118f51c0b095bb32d3";
                var axes = {"tb269e8a5d9224d7a8bd35c8e5a44157d": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "tdf3f0c5aded64af0b89d2a81a8f61db0": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Toyplot now removes entire observations that contain null values. Note
that this behavior is dictated by the structure of the visualization -
because we use stacked bars to represent data where the sum of the
magnitudes is significant, a null anywhere in that sum makes the entire
sum null and void.

This is not the case for all visualizations, of course. Consider what
happens when rendering a set of bar *boundaries*, rather than a set of
bar magnitudes:

.. code:: python

    observations = numpy.random.normal(size=(50, 50))
    boundaries = numpy.ma.column_stack((
        numpy.min(observations, axis=1),
        numpy.median(observations, axis=1),
        numpy.max(observations, axis=1),
        ))
    
    toyplot.bars(boundaries, baseline=None, width=600, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="ta42c4e687cd24873939267b6a7693418"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t67a653d7baaf4c189f3e6bcfade23a2e" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tb3d58dfe14114140a6c08c7e972d732f"><clipPath id="t33c2b83a538b4750b30df4d2faf7acfa"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t33c2b83a538b4750b30df4d2faf7acfa)"><g class="toyplot-mark-BarBoundaries" id="t0b84d92f83fc4f8eab2be436ede97008" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="41.124886758810902" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="50.0" y="148.54314610623697"></rect><rect class="toyplot-Datum" height="64.885658758042752" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="59.900990099009903" y="149.50980091535425"></rect><rect class="toyplot-Datum" height="62.87696965424351" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="69.801980198019805" y="148.3310372360304"></rect><rect class="toyplot-Datum" height="69.997674465261497" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="79.702970297029694" y="143.2753294000332"></rect><rect class="toyplot-Datum" height="82.501417492153649" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="89.603960396039611" y="149.42840495360269"></rect><rect class="toyplot-Datum" height="47.569036110565406" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="99.504950495049513" y="149.62855380632965"></rect><rect class="toyplot-Datum" height="35.266732756595559" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="109.4059405940594" y="150.12478743679981"></rect><rect class="toyplot-Datum" height="42.848232293640223" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="119.30693069306932" y="157.10481245860703"></rect><rect class="toyplot-Datum" height="42.076038886941802" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="129.20792079207922" y="150.28023201320724"></rect><rect class="toyplot-Datum" height="76.872217010169862" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="139.1089108910891" y="149.59652222781304"></rect><rect class="toyplot-Datum" height="46.326924651116002" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="149.00990099009903" y="145.73613277023685"></rect><rect class="toyplot-Datum" height="52.561105990677191" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="158.91089108910893" y="152.77336244825773"></rect><rect class="toyplot-Datum" height="85.056334836108647" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="168.8118811881188" y="144.48268117831972"></rect><rect class="toyplot-Datum" height="58.905583127282796" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="178.71287128712871" y="158.25125202518771"></rect><rect class="toyplot-Datum" height="63.014138319186571" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="188.61386138613864" y="149.56568474720609"></rect><rect class="toyplot-Datum" height="72.35001712740231" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="198.51485148514851" y="151.96731850142154"></rect><rect class="toyplot-Datum" height="73.007794676062616" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="208.41584158415844" y="152.75768921256673"></rect><rect class="toyplot-Datum" height="55.655094814497886" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="218.31683168316835" y="148.36565134014185"></rect><rect class="toyplot-Datum" height="44.540815836606896" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="228.21782178217819" y="151.42358500634865"></rect><rect class="toyplot-Datum" height="46.755380192199283" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="238.11881188118812" y="149.40874000036459"></rect><rect class="toyplot-Datum" height="98.138395906718927" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="248.01980198019803" y="151.3957233658632"></rect><rect class="toyplot-Datum" height="66.06377884106962" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="257.9207920792079" y="147.36925029212347"></rect><rect class="toyplot-Datum" height="81.10861564327746" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="267.82178217821786" y="154.63191334415657"></rect><rect class="toyplot-Datum" height="47.036540471727733" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="277.72277227722776" y="150.82605277252728"></rect><rect class="toyplot-Datum" height="62.957969627530957" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="287.62376237623761" y="150.39398986844392"></rect><rect class="toyplot-Datum" height="60.965328979838375" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="297.52475247524757" y="146.20697040440075"></rect><rect class="toyplot-Datum" height="44.203760466030246" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="307.42574257425741" y="152.7315606645646"></rect><rect class="toyplot-Datum" height="38.687514719540559" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="317.32673267326737" y="155.33225801874707"></rect><rect class="toyplot-Datum" height="65.822593080299271" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.900990099009789" x="327.22772277227727" y="144.6920734739324"></rect><rect class="toyplot-Datum" height="54.417163187357971" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="337.12871287128706" y="151.01272631585715"></rect><rect class="toyplot-Datum" height="49.027114574529321" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="347.02970297029702" y="148.58039094762415"></rect><rect class="toyplot-Datum" height="93.531336035253645" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="356.93069306930693" y="146.43441355873284"></rect><rect class="toyplot-Datum" height="51.337424781626623" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="366.83168316831689" y="154.07825401133579"></rect><rect class="toyplot-Datum" height="60.490945794015943" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="376.73267326732673" y="150.23581651253929"></rect><rect class="toyplot-Datum" height="72.194880577789064" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="386.63366336633669" y="143.34025384104271"></rect><rect class="toyplot-Datum" height="51.280316576822145" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="396.53465346534654" y="155.50521778259136"></rect><rect class="toyplot-Datum" height="51.111843367290277" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="406.43564356435638" y="142.13800577291889"></rect><rect class="toyplot-Datum" height="35.967193645099485" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="416.33663366336634" y="146.00676016871046"></rect><rect class="toyplot-Datum" height="73.958528556259012" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="426.23762376237624" y="143.0046745701481"></rect><rect class="toyplot-Datum" height="60.174265591715852" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="436.13861386138615" y="152.65667753703949"></rect><rect class="toyplot-Datum" height="48.41514577829588" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="446.03960396039605" y="144.94807917207945"></rect><rect class="toyplot-Datum" height="51.619053396184796" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="455.94059405940595" y="150.11992605411029"></rect><rect class="toyplot-Datum" height="61.122021648515982" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="465.84158415841586" y="152.78582053956825"></rect><rect class="toyplot-Datum" height="58.021022312282071" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="475.7425742574257" y="150.41824749296862"></rect><rect class="toyplot-Datum" height="55.370287321516685" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="485.64356435643566" y="144.07369604155983"></rect><rect class="toyplot-Datum" height="49.712837742341037" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="495.54455445544556" y="152.81036022600333"></rect><rect class="toyplot-Datum" height="68.884116575022944" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="505.44554455445547" y="146.07475227024108"></rect><rect class="toyplot-Datum" height="63.0528769251423" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="515.34653465346537" y="138.8565177528873"></rect><rect class="toyplot-Datum" height="58.041902212709687" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="525.24752475247521" y="153.56694361419298"></rect><rect class="toyplot-Datum" height="53.473929725144416" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="535.14851485148517" y="148.90130937567758"></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="31.39769991155913" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="50.0" y="117.14544619467785"></rect><rect class="toyplot-Datum" height="43.382251455699503" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="59.900990099009903" y="106.12754945965474"></rect><rect class="toyplot-Datum" height="50.022820221908418" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="69.801980198019805" y="98.308217014121979"></rect><rect class="toyplot-Datum" height="57.019489191470143" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="79.702970297029694" y="86.255840208563058"></rect><rect class="toyplot-Datum" height="37.597445471352273" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="89.603960396039611" y="111.83095948225042"></rect><rect class="toyplot-Datum" height="52.623270537122309" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="99.504950495049513" y="97.005283269207339"></rect><rect class="toyplot-Datum" height="42.643555720415193" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="109.4059405940594" y="107.48123171638461"></rect><rect class="toyplot-Datum" height="64.633592277110225" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="119.30693069306932" y="92.471220181496804"></rect><rect class="toyplot-Datum" height="61.278935874500775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="129.20792079207922" y="89.001296138706465"></rect><rect class="toyplot-Datum" height="56.965762103471405" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="139.1089108910891" y="92.630760124341634"></rect><rect class="toyplot-Datum" height="51.714834547727989" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="149.00990099009903" y="94.021298222508861"></rect><rect class="toyplot-Datum" height="75.409627739147226" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="158.91089108910893" y="77.363734709110503"></rect><rect class="toyplot-Datum" height="48.883501577824035" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="168.8118811881188" y="95.599179600495688"></rect><rect class="toyplot-Datum" height="50.868615302803164" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="178.71287128712871" y="107.38263672238455"></rect><rect class="toyplot-Datum" height="50.537660383826221" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="188.61386138613864" y="99.02802436337987"></rect><rect class="toyplot-Datum" height="86.766190526312656" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="198.51485148514851" y="65.201127975108889"></rect><rect class="toyplot-Datum" height="64.895665351032719" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="208.41584158415844" y="87.862023861534013"></rect><rect class="toyplot-Datum" height="48.576520316942009" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="218.31683168316835" y="99.789131023199843"></rect><rect class="toyplot-Datum" height="50.054420222876246" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="228.21782178217819" y="101.3691647834724"></rect><rect class="toyplot-Datum" height="71.637991708200175" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="238.11881188118812" y="77.770748292164413"></rect><rect class="toyplot-Datum" height="58.467558446138099" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="248.01980198019803" y="92.928164919725106"></rect><rect class="toyplot-Datum" height="61.651347029792589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="257.9207920792079" y="85.717903262330879"></rect><rect class="toyplot-Datum" height="62.004703075959299" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="267.82178217821786" y="92.627210268197274"></rect><rect class="toyplot-Datum" height="53.909668447143815" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="277.72277227722776" y="96.916384325383461"></rect><rect class="toyplot-Datum" height="78.610662882569557" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="287.62376237623761" y="71.783326985874368"></rect><rect class="toyplot-Datum" height="58.31077525584702" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="297.52475247524757" y="87.89619514855373"></rect><rect class="toyplot-Datum" height="43.468699504770569" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="307.42574257425741" y="109.26286115979403"></rect><rect class="toyplot-Datum" height="62.29808117432637" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="317.32673267326737" y="93.034176844420699"></rect><rect class="toyplot-Datum" height="43.805993532380811" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.900990099009789" x="327.22772277227727" y="100.88607994155159"></rect><rect class="toyplot-Datum" height="52.161743096506129" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="337.12871287128706" y="98.850983219351022"></rect><rect class="toyplot-Datum" height="32.919983508702671" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="347.02970297029702" y="115.66040743892148"></rect><rect class="toyplot-Datum" height="64.293701558087193" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="356.93069306930693" y="82.140712000645649"></rect><rect class="toyplot-Datum" height="60.185386155416751" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="366.83168316831689" y="93.892867855919036"></rect><rect class="toyplot-Datum" height="54.676294973439298" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="376.73267326732673" y="95.55952153909999"></rect><rect class="toyplot-Datum" height="33.590862424720299" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="386.63366336633669" y="109.74939141632241"></rect><rect class="toyplot-Datum" height="53.643950751950598" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="396.53465346534654" y="101.86126703064076"></rect><rect class="toyplot-Datum" height="60.838095301738079" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="406.43564356435638" y="81.299910471180809"></rect><rect class="toyplot-Datum" height="52.481544919058365" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="416.33663366336634" y="93.525215249652092"></rect><rect class="toyplot-Datum" height="42.723686899953691" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="426.23762376237624" y="100.28098767019441"></rect><rect class="toyplot-Datum" height="60.802547909107659" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="436.13861386138615" y="91.854129627931826"></rect><rect class="toyplot-Datum" height="69.7200000212775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="446.03960396039605" y="75.228079150801946"></rect><rect class="toyplot-Datum" height="64.672469845158034" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="455.94059405940595" y="85.447456208952261"></rect><rect class="toyplot-Datum" height="62.780340101362967" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="465.84158415841586" y="90.005480438205282"></rect><rect class="toyplot-Datum" height="49.562662421119867" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="475.7425742574257" y="100.85558507184875"></rect><rect class="toyplot-Datum" height="46.678639856867392" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="485.64356435643566" y="97.395056184692436"></rect><rect class="toyplot-Datum" height="54.945335737026213" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="495.54455445544556" y="97.865024488977113"></rect><rect class="toyplot-Datum" height="50.194491110627041" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="505.44554455445547" y="95.880261159614037"></rect><rect class="toyplot-Datum" height="41.045602157039383" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="515.34653465346537" y="97.810915595847916"></rect><rect class="toyplot-Datum" height="64.835236873744009" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="525.24752475247521" y="88.731706740448971"></rect><rect class="toyplot-Datum" height="61.630720450085619" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="535.14851485148517" y="87.270588925591966"></rect></g></g></g><g class="toyplot-coordinates-Axis" id="t9cecf0dd61204063862ea6a477dda8e5" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="495.049504950495" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(4.9504950495049505,6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(103.96039603960395,6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(202.97029702970298,6)"><tspan style="dominant-baseline:inherit">20</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(301.98019801980195,6)"><tspan style="dominant-baseline:inherit">30</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.99009900990103,6)"><tspan style="dominant-baseline:inherit">40</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,6)"><tspan style="dominant-baseline:inherit">50</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t1c1a80f57f224bd2b348b6cf13f42d9f" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0.4658807274178889" x2="184.79887202489112" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">-4</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,-6)"><tspan style="dominant-baseline:inherit">-2</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,-6)"><tspan style="dominant-baseline:inherit">2</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">4</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "t0b84d92f83fc4f8eab2be436ede97008", "columns": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5], [0.05827415575052086, 0.019607963385830277, 0.0667585105587835, 0.2689868239986718, 0.022863801855891968, 0.014857847746814493, -0.004991497471993052, -0.2841924983442814, -0.01120928052829014, 0.01613911088747882, 0.17055468919052602, -0.11093449793030938, 0.22069275286721116, -0.3300500810075081, 0.01737261011175662, -0.07869274005686182, -0.11030756850266951, 0.06537394639432609, -0.056943400253946556, 0.023650399985416605, -0.05582893463452801, 0.10522998831506175, -0.18527653376626368, -0.03304211090109119, -0.0157595947377568, 0.1517211838239701, -0.10926242658258428, -0.21329032074988336, 0.2123170610427047, -0.04050905263428535, 0.05678436209503326, 0.14262345765068624, -0.16313016045343154, -0.00943266050157094, 0.266389846358291, -0.2202087113036536, 0.31447976908324493, 0.1597295932515817, 0.27981301719407603, -0.10626710148157884, 0.20207683311682245, -0.004797042164411372, -0.1114328215827292, -0.016729899718744508, 0.23705215833760737, -0.11241440904013367, 0.15700990919035693, 0.4457392898845084, -0.1426777445677188, 0.04394762497289654], [1.3141821522128858, 1.75489802161381, 2.0676713194351204, 2.5497663916574775, 1.5267616207099823, 2.1197886692317067, 1.700750731344615, 2.301151192740128, 2.439948154451741, 2.2947695950263345, 2.239148071099645, 2.905450611635579, 2.1760328159801725, 1.7046945311046178, 2.038879025464805, 3.391954880995644, 2.485519045538639, 2.008434759072007, 1.945233408661104, 2.8891700683134234, 2.282873403210996, 2.5712838695067646, 2.2949115892721093, 2.123344626984662, 3.128666920565025, 2.484152194057851, 1.6294855536082387, 2.278632926223172, 1.9645568023379363, 2.0459606712259597, 1.3735837024431405, 2.7143715199741734, 2.2442852857632385, 2.177619138436001, 1.6100243433471038, 1.92554931877437, 2.748003581152767, 2.2589913900139167, 1.9887604931922236, 2.3258348148827266, 2.9908768339679224, 2.58210175164191, 2.3997807824717885, 1.9657765971260497, 2.1041977526123024, 2.0853990204409154, 2.1647895536154382, 2.0875633761660835, 2.4507317303820413, 2.5091764429763215]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#ta42c4e687cd24873939267b6a7693418 .toyplot-mark-popup");
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
    
                var root_id = "ta42c4e687cd24873939267b6a7693418";
                var axes = {"t1c1a80f57f224bd2b348b6cf13f42d9f": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 4.0, "min": -4.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "t9cecf0dd61204063862ea6a477dda8e5": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Now, suppose that some of the lower boundaries in the plot are null:

.. code:: python

    boundaries[5:10, 0] = numpy.ma.masked
    toyplot.bars(boundaries, baseline=None, width=600, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="tb4cae7f473da4254be86ce53473cf4e7"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t8323237a64134ae7898a851edd04b560" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t1b477b395a7d48cca19ce70d75f0ca26"><clipPath id="t48f8b491c50c47aabb564108977fd861"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t48f8b491c50c47aabb564108977fd861)"><g class="toyplot-mark-BarBoundaries" id="t632e562f22bb47199d46f5bdf8415791" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="41.124886758810902" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="50.0" y="148.54314610623697"></rect><rect class="toyplot-Datum" height="64.885658758042752" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="59.900990099009903" y="149.50980091535425"></rect><rect class="toyplot-Datum" height="62.87696965424351" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="69.801980198019805" y="148.3310372360304"></rect><rect class="toyplot-Datum" height="69.997674465261497" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="79.702970297029694" y="143.2753294000332"></rect><rect class="toyplot-Datum" height="82.501417492153649" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="89.603960396039611" y="149.42840495360269"></rect><rect class="toyplot-Datum" height="46.326924651116002" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="149.00990099009903" y="145.73613277023685"></rect><rect class="toyplot-Datum" height="52.561105990677191" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="158.91089108910893" y="152.77336244825773"></rect><rect class="toyplot-Datum" height="85.056334836108647" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="168.8118811881188" y="144.48268117831972"></rect><rect class="toyplot-Datum" height="58.905583127282796" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="178.71287128712871" y="158.25125202518771"></rect><rect class="toyplot-Datum" height="63.014138319186571" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="188.61386138613864" y="149.56568474720609"></rect><rect class="toyplot-Datum" height="72.35001712740231" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="198.51485148514851" y="151.96731850142154"></rect><rect class="toyplot-Datum" height="73.007794676062616" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="208.41584158415844" y="152.75768921256673"></rect><rect class="toyplot-Datum" height="55.655094814497886" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="218.31683168316835" y="148.36565134014185"></rect><rect class="toyplot-Datum" height="44.540815836606896" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="228.21782178217819" y="151.42358500634865"></rect><rect class="toyplot-Datum" height="46.755380192199283" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="238.11881188118812" y="149.40874000036459"></rect><rect class="toyplot-Datum" height="98.138395906718927" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="248.01980198019803" y="151.3957233658632"></rect><rect class="toyplot-Datum" height="66.06377884106962" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="257.9207920792079" y="147.36925029212347"></rect><rect class="toyplot-Datum" height="81.10861564327746" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="267.82178217821786" y="154.63191334415657"></rect><rect class="toyplot-Datum" height="47.036540471727733" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="277.72277227722776" y="150.82605277252728"></rect><rect class="toyplot-Datum" height="62.957969627530957" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="287.62376237623761" y="150.39398986844392"></rect><rect class="toyplot-Datum" height="60.965328979838375" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="297.52475247524757" y="146.20697040440075"></rect><rect class="toyplot-Datum" height="44.203760466030246" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="307.42574257425741" y="152.7315606645646"></rect><rect class="toyplot-Datum" height="38.687514719540559" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="317.32673267326737" y="155.33225801874707"></rect><rect class="toyplot-Datum" height="65.822593080299271" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.900990099009789" x="327.22772277227727" y="144.6920734739324"></rect><rect class="toyplot-Datum" height="54.417163187357971" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="337.12871287128706" y="151.01272631585715"></rect><rect class="toyplot-Datum" height="49.027114574529321" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="347.02970297029702" y="148.58039094762415"></rect><rect class="toyplot-Datum" height="93.531336035253645" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="356.93069306930693" y="146.43441355873284"></rect><rect class="toyplot-Datum" height="51.337424781626623" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="366.83168316831689" y="154.07825401133579"></rect><rect class="toyplot-Datum" height="60.490945794015943" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="376.73267326732673" y="150.23581651253929"></rect><rect class="toyplot-Datum" height="72.194880577789064" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="386.63366336633669" y="143.34025384104271"></rect><rect class="toyplot-Datum" height="51.280316576822145" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="396.53465346534654" y="155.50521778259136"></rect><rect class="toyplot-Datum" height="51.111843367290277" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="406.43564356435638" y="142.13800577291889"></rect><rect class="toyplot-Datum" height="35.967193645099485" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="416.33663366336634" y="146.00676016871046"></rect><rect class="toyplot-Datum" height="73.958528556259012" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="426.23762376237624" y="143.0046745701481"></rect><rect class="toyplot-Datum" height="60.174265591715852" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="436.13861386138615" y="152.65667753703949"></rect><rect class="toyplot-Datum" height="48.41514577829588" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="446.03960396039605" y="144.94807917207945"></rect><rect class="toyplot-Datum" height="51.619053396184796" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="455.94059405940595" y="150.11992605411029"></rect><rect class="toyplot-Datum" height="61.122021648515982" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="465.84158415841586" y="152.78582053956825"></rect><rect class="toyplot-Datum" height="58.021022312282071" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="475.7425742574257" y="150.41824749296862"></rect><rect class="toyplot-Datum" height="55.370287321516685" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="485.64356435643566" y="144.07369604155983"></rect><rect class="toyplot-Datum" height="49.712837742341037" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="495.54455445544556" y="152.81036022600333"></rect><rect class="toyplot-Datum" height="68.884116575022944" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="505.44554455445547" y="146.07475227024108"></rect><rect class="toyplot-Datum" height="63.0528769251423" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="515.34653465346537" y="138.8565177528873"></rect><rect class="toyplot-Datum" height="58.041902212709687" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="525.24752475247521" y="153.56694361419298"></rect><rect class="toyplot-Datum" height="53.473929725144416" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="535.14851485148517" y="148.90130937567758"></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="31.39769991155913" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="50.0" y="117.14544619467785"></rect><rect class="toyplot-Datum" height="43.382251455699503" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="59.900990099009903" y="106.12754945965474"></rect><rect class="toyplot-Datum" height="50.022820221908418" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="69.801980198019805" y="98.308217014121979"></rect><rect class="toyplot-Datum" height="57.019489191470143" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="79.702970297029694" y="86.255840208563058"></rect><rect class="toyplot-Datum" height="37.597445471352273" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="89.603960396039611" y="111.83095948225042"></rect><rect class="toyplot-Datum" height="52.623270537122309" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="99.504950495049513" y="97.005283269207339"></rect><rect class="toyplot-Datum" height="42.643555720415193" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="109.4059405940594" y="107.48123171638461"></rect><rect class="toyplot-Datum" height="64.633592277110225" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="119.30693069306932" y="92.471220181496804"></rect><rect class="toyplot-Datum" height="61.278935874500775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="129.20792079207922" y="89.001296138706465"></rect><rect class="toyplot-Datum" height="56.965762103471405" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="139.1089108910891" y="92.630760124341634"></rect><rect class="toyplot-Datum" height="51.714834547727989" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="149.00990099009903" y="94.021298222508861"></rect><rect class="toyplot-Datum" height="75.409627739147226" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="158.91089108910893" y="77.363734709110503"></rect><rect class="toyplot-Datum" height="48.883501577824035" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="168.8118811881188" y="95.599179600495688"></rect><rect class="toyplot-Datum" height="50.868615302803164" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="178.71287128712871" y="107.38263672238455"></rect><rect class="toyplot-Datum" height="50.537660383826221" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="188.61386138613864" y="99.02802436337987"></rect><rect class="toyplot-Datum" height="86.766190526312656" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="198.51485148514851" y="65.201127975108889"></rect><rect class="toyplot-Datum" height="64.895665351032719" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="208.41584158415844" y="87.862023861534013"></rect><rect class="toyplot-Datum" height="48.576520316942009" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="218.31683168316835" y="99.789131023199843"></rect><rect class="toyplot-Datum" height="50.054420222876246" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="228.21782178217819" y="101.3691647834724"></rect><rect class="toyplot-Datum" height="71.637991708200175" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="238.11881188118812" y="77.770748292164413"></rect><rect class="toyplot-Datum" height="58.467558446138099" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="248.01980198019803" y="92.928164919725106"></rect><rect class="toyplot-Datum" height="61.651347029792589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="257.9207920792079" y="85.717903262330879"></rect><rect class="toyplot-Datum" height="62.004703075959299" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="267.82178217821786" y="92.627210268197274"></rect><rect class="toyplot-Datum" height="53.909668447143815" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="277.72277227722776" y="96.916384325383461"></rect><rect class="toyplot-Datum" height="78.610662882569557" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="287.62376237623761" y="71.783326985874368"></rect><rect class="toyplot-Datum" height="58.31077525584702" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="297.52475247524757" y="87.89619514855373"></rect><rect class="toyplot-Datum" height="43.468699504770569" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="307.42574257425741" y="109.26286115979403"></rect><rect class="toyplot-Datum" height="62.29808117432637" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="317.32673267326737" y="93.034176844420699"></rect><rect class="toyplot-Datum" height="43.805993532380811" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.900990099009789" x="327.22772277227727" y="100.88607994155159"></rect><rect class="toyplot-Datum" height="52.161743096506129" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="337.12871287128706" y="98.850983219351022"></rect><rect class="toyplot-Datum" height="32.919983508702671" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="347.02970297029702" y="115.66040743892148"></rect><rect class="toyplot-Datum" height="64.293701558087193" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="356.93069306930693" y="82.140712000645649"></rect><rect class="toyplot-Datum" height="60.185386155416751" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="366.83168316831689" y="93.892867855919036"></rect><rect class="toyplot-Datum" height="54.676294973439298" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="376.73267326732673" y="95.55952153909999"></rect><rect class="toyplot-Datum" height="33.590862424720299" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="386.63366336633669" y="109.74939141632241"></rect><rect class="toyplot-Datum" height="53.643950751950598" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="396.53465346534654" y="101.86126703064076"></rect><rect class="toyplot-Datum" height="60.838095301738079" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="406.43564356435638" y="81.299910471180809"></rect><rect class="toyplot-Datum" height="52.481544919058365" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="416.33663366336634" y="93.525215249652092"></rect><rect class="toyplot-Datum" height="42.723686899953691" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="426.23762376237624" y="100.28098767019441"></rect><rect class="toyplot-Datum" height="60.802547909107659" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="436.13861386138615" y="91.854129627931826"></rect><rect class="toyplot-Datum" height="69.7200000212775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="446.03960396039605" y="75.228079150801946"></rect><rect class="toyplot-Datum" height="64.672469845158034" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="455.94059405940595" y="85.447456208952261"></rect><rect class="toyplot-Datum" height="62.780340101362967" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="465.84158415841586" y="90.005480438205282"></rect><rect class="toyplot-Datum" height="49.562662421119867" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="475.7425742574257" y="100.85558507184875"></rect><rect class="toyplot-Datum" height="46.678639856867392" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="485.64356435643566" y="97.395056184692436"></rect><rect class="toyplot-Datum" height="54.945335737026213" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="495.54455445544556" y="97.865024488977113"></rect><rect class="toyplot-Datum" height="50.194491110627041" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="505.44554455445547" y="95.880261159614037"></rect><rect class="toyplot-Datum" height="41.045602157039383" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="515.34653465346537" y="97.810915595847916"></rect><rect class="toyplot-Datum" height="64.835236873744009" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="525.24752475247521" y="88.731706740448971"></rect><rect class="toyplot-Datum" height="61.630720450085619" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="535.14851485148517" y="87.270588925591966"></rect></g></g></g><g class="toyplot-coordinates-Axis" id="t17e0699a032b4ea98db38bb9d195603c" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="495.049504950495" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(4.9504950495049505,6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(103.96039603960395,6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(202.97029702970298,6)"><tspan style="dominant-baseline:inherit">20</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(301.98019801980195,6)"><tspan style="dominant-baseline:inherit">30</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.99009900990103,6)"><tspan style="dominant-baseline:inherit">40</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,6)"><tspan style="dominant-baseline:inherit">50</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="td51dca66feab4a41b2e97999f3a2178b" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0.4658807274178889" x2="184.79887202489112" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">-4</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,-6)"><tspan style="dominant-baseline:inherit">-2</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,-6)"><tspan style="dominant-baseline:inherit">2</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">4</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "t632e562f22bb47199d46f5bdf8415791", "columns": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5], [0.05827415575052086, 0.019607963385830277, 0.0667585105587835, 0.2689868239986718, 0.022863801855891968, 0.014857847746814493, -0.004991497471993052, -0.2841924983442814, -0.01120928052829014, 0.01613911088747882, 0.17055468919052602, -0.11093449793030938, 0.22069275286721116, -0.3300500810075081, 0.01737261011175662, -0.07869274005686182, -0.11030756850266951, 0.06537394639432609, -0.056943400253946556, 0.023650399985416605, -0.05582893463452801, 0.10522998831506175, -0.18527653376626368, -0.03304211090109119, -0.0157595947377568, 0.1517211838239701, -0.10926242658258428, -0.21329032074988336, 0.2123170610427047, -0.04050905263428535, 0.05678436209503326, 0.14262345765068624, -0.16313016045343154, -0.00943266050157094, 0.266389846358291, -0.2202087113036536, 0.31447976908324493, 0.1597295932515817, 0.27981301719407603, -0.10626710148157884, 0.20207683311682245, -0.004797042164411372, -0.1114328215827292, -0.016729899718744508, 0.23705215833760737, -0.11241440904013367, 0.15700990919035693, 0.4457392898845084, -0.1426777445677188, 0.04394762497289654], [1.3141821522128858, 1.75489802161381, 2.0676713194351204, 2.5497663916574775, 1.5267616207099823, 2.1197886692317067, 1.700750731344615, 2.301151192740128, 2.439948154451741, 2.2947695950263345, 2.239148071099645, 2.905450611635579, 2.1760328159801725, 1.7046945311046178, 2.038879025464805, 3.391954880995644, 2.485519045538639, 2.008434759072007, 1.945233408661104, 2.8891700683134234, 2.282873403210996, 2.5712838695067646, 2.2949115892721093, 2.123344626984662, 3.128666920565025, 2.484152194057851, 1.6294855536082387, 2.278632926223172, 1.9645568023379363, 2.0459606712259597, 1.3735837024431405, 2.7143715199741734, 2.2442852857632385, 2.177619138436001, 1.6100243433471038, 1.92554931877437, 2.748003581152767, 2.2589913900139167, 1.9887604931922236, 2.3258348148827266, 2.9908768339679224, 2.58210175164191, 2.3997807824717885, 1.9657765971260497, 2.1041977526123024, 2.0853990204409154, 2.1647895536154382, 2.0875633761660835, 2.4507317303820413, 2.5091764429763215]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#tb4cae7f473da4254be86ce53473cf4e7 .toyplot-mark-popup");
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
    
                var root_id = "tb4cae7f473da4254be86ce53473cf4e7";
                var axes = {"t17e0699a032b4ea98db38bb9d195603c": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "td51dca66feab4a41b2e97999f3a2178b": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 4.0, "min": -4.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


In this case, the position of each bar is defined by two boundaries.
Only those bars with missing boundaries are left out - the adjacent bars
are still visible because they are still unambigously well-defined. The
same would be true if some of the top boundary values were null:

.. code:: python

    boundaries[40:45, 2] = numpy.ma.masked
    toyplot.bars(boundaries, baseline=None, width=600, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="tb7179925c3c24780b90ecf6bb0dfada8"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t693e0d9c72a84a5da653dbcafca5f1e3" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t0a56086d5cee41fe8e2dd986ed678dfa"><clipPath id="tbb956476d2db4fafb97a8aefe4ad2143"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tbb956476d2db4fafb97a8aefe4ad2143)"><g class="toyplot-mark-BarBoundaries" id="t5af55280cb814daeab3c39785a0c8116" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="41.124886758810902" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="50.0" y="148.54314610623697"></rect><rect class="toyplot-Datum" height="64.885658758042752" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="59.900990099009903" y="149.50980091535425"></rect><rect class="toyplot-Datum" height="62.87696965424351" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="69.801980198019805" y="148.3310372360304"></rect><rect class="toyplot-Datum" height="69.997674465261497" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="79.702970297029694" y="143.2753294000332"></rect><rect class="toyplot-Datum" height="82.501417492153649" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="89.603960396039611" y="149.42840495360269"></rect><rect class="toyplot-Datum" height="46.326924651116002" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="149.00990099009903" y="145.73613277023685"></rect><rect class="toyplot-Datum" height="52.561105990677191" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="158.91089108910893" y="152.77336244825773"></rect><rect class="toyplot-Datum" height="85.056334836108647" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="168.8118811881188" y="144.48268117831972"></rect><rect class="toyplot-Datum" height="58.905583127282796" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="178.71287128712871" y="158.25125202518771"></rect><rect class="toyplot-Datum" height="63.014138319186571" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="188.61386138613864" y="149.56568474720609"></rect><rect class="toyplot-Datum" height="72.35001712740231" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="198.51485148514851" y="151.96731850142154"></rect><rect class="toyplot-Datum" height="73.007794676062616" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="208.41584158415844" y="152.75768921256673"></rect><rect class="toyplot-Datum" height="55.655094814497886" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="218.31683168316835" y="148.36565134014185"></rect><rect class="toyplot-Datum" height="44.540815836606896" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="228.21782178217819" y="151.42358500634865"></rect><rect class="toyplot-Datum" height="46.755380192199283" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="238.11881188118812" y="149.40874000036459"></rect><rect class="toyplot-Datum" height="98.138395906718927" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="248.01980198019803" y="151.3957233658632"></rect><rect class="toyplot-Datum" height="66.06377884106962" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="257.9207920792079" y="147.36925029212347"></rect><rect class="toyplot-Datum" height="81.10861564327746" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="267.82178217821786" y="154.63191334415657"></rect><rect class="toyplot-Datum" height="47.036540471727733" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="277.72277227722776" y="150.82605277252728"></rect><rect class="toyplot-Datum" height="62.957969627530957" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="287.62376237623761" y="150.39398986844392"></rect><rect class="toyplot-Datum" height="60.965328979838375" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="297.52475247524757" y="146.20697040440075"></rect><rect class="toyplot-Datum" height="44.203760466030246" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="307.42574257425741" y="152.7315606645646"></rect><rect class="toyplot-Datum" height="38.687514719540559" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="317.32673267326737" y="155.33225801874707"></rect><rect class="toyplot-Datum" height="65.822593080299271" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.900990099009789" x="327.22772277227727" y="144.6920734739324"></rect><rect class="toyplot-Datum" height="54.417163187357971" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="337.12871287128706" y="151.01272631585715"></rect><rect class="toyplot-Datum" height="49.027114574529321" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="347.02970297029702" y="148.58039094762415"></rect><rect class="toyplot-Datum" height="93.531336035253645" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="356.93069306930693" y="146.43441355873284"></rect><rect class="toyplot-Datum" height="51.337424781626623" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="366.83168316831689" y="154.07825401133579"></rect><rect class="toyplot-Datum" height="60.490945794015943" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="376.73267326732673" y="150.23581651253929"></rect><rect class="toyplot-Datum" height="72.194880577789064" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="386.63366336633669" y="143.34025384104271"></rect><rect class="toyplot-Datum" height="51.280316576822145" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="396.53465346534654" y="155.50521778259136"></rect><rect class="toyplot-Datum" height="51.111843367290277" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="406.43564356435638" y="142.13800577291889"></rect><rect class="toyplot-Datum" height="35.967193645099485" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="416.33663366336634" y="146.00676016871046"></rect><rect class="toyplot-Datum" height="73.958528556259012" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="426.23762376237624" y="143.0046745701481"></rect><rect class="toyplot-Datum" height="60.174265591715852" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="436.13861386138615" y="152.65667753703949"></rect><rect class="toyplot-Datum" height="48.41514577829588" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="446.03960396039605" y="144.94807917207945"></rect><rect class="toyplot-Datum" height="51.619053396184796" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="455.94059405940595" y="150.11992605411029"></rect><rect class="toyplot-Datum" height="61.122021648515982" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="465.84158415841586" y="152.78582053956825"></rect><rect class="toyplot-Datum" height="58.021022312282071" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="475.7425742574257" y="150.41824749296862"></rect><rect class="toyplot-Datum" height="55.370287321516685" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="485.64356435643566" y="144.07369604155983"></rect><rect class="toyplot-Datum" height="49.712837742341037" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="495.54455445544556" y="152.81036022600333"></rect><rect class="toyplot-Datum" height="68.884116575022944" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="505.44554455445547" y="146.07475227024108"></rect><rect class="toyplot-Datum" height="63.0528769251423" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="515.34653465346537" y="138.8565177528873"></rect><rect class="toyplot-Datum" height="58.041902212709687" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="525.24752475247521" y="153.56694361419298"></rect><rect class="toyplot-Datum" height="53.473929725144416" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="535.14851485148517" y="148.90130937567758"></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="31.39769991155913" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="50.0" y="117.14544619467785"></rect><rect class="toyplot-Datum" height="43.382251455699503" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="59.900990099009903" y="106.12754945965474"></rect><rect class="toyplot-Datum" height="50.022820221908418" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="69.801980198019805" y="98.308217014121979"></rect><rect class="toyplot-Datum" height="57.019489191470143" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="79.702970297029694" y="86.255840208563058"></rect><rect class="toyplot-Datum" height="37.597445471352273" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="89.603960396039611" y="111.83095948225042"></rect><rect class="toyplot-Datum" height="52.623270537122309" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="99.504950495049513" y="97.005283269207339"></rect><rect class="toyplot-Datum" height="42.643555720415193" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="109.4059405940594" y="107.48123171638461"></rect><rect class="toyplot-Datum" height="64.633592277110225" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="119.30693069306932" y="92.471220181496804"></rect><rect class="toyplot-Datum" height="61.278935874500775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="129.20792079207922" y="89.001296138706465"></rect><rect class="toyplot-Datum" height="56.965762103471405" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="139.1089108910891" y="92.630760124341634"></rect><rect class="toyplot-Datum" height="51.714834547727989" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="149.00990099009903" y="94.021298222508861"></rect><rect class="toyplot-Datum" height="75.409627739147226" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="158.91089108910893" y="77.363734709110503"></rect><rect class="toyplot-Datum" height="48.883501577824035" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="168.8118811881188" y="95.599179600495688"></rect><rect class="toyplot-Datum" height="50.868615302803164" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="178.71287128712871" y="107.38263672238455"></rect><rect class="toyplot-Datum" height="50.537660383826221" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="188.61386138613864" y="99.02802436337987"></rect><rect class="toyplot-Datum" height="86.766190526312656" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="198.51485148514851" y="65.201127975108889"></rect><rect class="toyplot-Datum" height="64.895665351032719" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="208.41584158415844" y="87.862023861534013"></rect><rect class="toyplot-Datum" height="48.576520316942009" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="218.31683168316835" y="99.789131023199843"></rect><rect class="toyplot-Datum" height="50.054420222876246" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="228.21782178217819" y="101.3691647834724"></rect><rect class="toyplot-Datum" height="71.637991708200175" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="238.11881188118812" y="77.770748292164413"></rect><rect class="toyplot-Datum" height="58.467558446138099" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="248.01980198019803" y="92.928164919725106"></rect><rect class="toyplot-Datum" height="61.651347029792589" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="257.9207920792079" y="85.717903262330879"></rect><rect class="toyplot-Datum" height="62.004703075959299" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="267.82178217821786" y="92.627210268197274"></rect><rect class="toyplot-Datum" height="53.909668447143815" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="277.72277227722776" y="96.916384325383461"></rect><rect class="toyplot-Datum" height="78.610662882569557" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="287.62376237623761" y="71.783326985874368"></rect><rect class="toyplot-Datum" height="58.31077525584702" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="297.52475247524757" y="87.89619514855373"></rect><rect class="toyplot-Datum" height="43.468699504770569" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="307.42574257425741" y="109.26286115979403"></rect><rect class="toyplot-Datum" height="62.29808117432637" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="317.32673267326737" y="93.034176844420699"></rect><rect class="toyplot-Datum" height="43.805993532380811" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.900990099009789" x="327.22772277227727" y="100.88607994155159"></rect><rect class="toyplot-Datum" height="52.161743096506129" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="337.12871287128706" y="98.850983219351022"></rect><rect class="toyplot-Datum" height="32.919983508702671" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="347.02970297029702" y="115.66040743892148"></rect><rect class="toyplot-Datum" height="64.293701558087193" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="356.93069306930693" y="82.140712000645649"></rect><rect class="toyplot-Datum" height="60.185386155416751" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="366.83168316831689" y="93.892867855919036"></rect><rect class="toyplot-Datum" height="54.676294973439298" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="376.73267326732673" y="95.55952153909999"></rect><rect class="toyplot-Datum" height="33.590862424720299" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="386.63366336633669" y="109.74939141632241"></rect><rect class="toyplot-Datum" height="53.643950751950598" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="396.53465346534654" y="101.86126703064076"></rect><rect class="toyplot-Datum" height="60.838095301738079" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="406.43564356435638" y="81.299910471180809"></rect><rect class="toyplot-Datum" height="52.481544919058365" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="416.33663366336634" y="93.525215249652092"></rect><rect class="toyplot-Datum" height="42.723686899953691" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="426.23762376237624" y="100.28098767019441"></rect><rect class="toyplot-Datum" height="60.802547909107659" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="436.13861386138615" y="91.854129627931826"></rect><rect class="toyplot-Datum" height="54.945335737026213" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="495.54455445544556" y="97.865024488977113"></rect><rect class="toyplot-Datum" height="50.194491110627041" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="505.44554455445547" y="95.880261159614037"></rect><rect class="toyplot-Datum" height="41.045602157039383" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="515.34653465346537" y="97.810915595847916"></rect><rect class="toyplot-Datum" height="64.835236873744009" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="525.24752475247521" y="88.731706740448971"></rect><rect class="toyplot-Datum" height="61.630720450085619" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="535.14851485148517" y="87.270588925591966"></rect></g></g></g><g class="toyplot-coordinates-Axis" id="tb3b24fd167014ae2b86839d537a572e1" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="495.049504950495" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(4.9504950495049505,6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(103.96039603960395,6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(202.97029702970298,6)"><tspan style="dominant-baseline:inherit">20</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(301.98019801980195,6)"><tspan style="dominant-baseline:inherit">30</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.99009900990103,6)"><tspan style="dominant-baseline:inherit">40</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,6)"><tspan style="dominant-baseline:inherit">50</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t7861663641fe4afbb5fc189266d9fc03" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0.4658807274178889" x2="184.79887202489112" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">-4</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,-6)"><tspan style="dominant-baseline:inherit">-2</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,-6)"><tspan style="dominant-baseline:inherit">2</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">4</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "t5af55280cb814daeab3c39785a0c8116", "columns": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5], [0.05827415575052086, 0.019607963385830277, 0.0667585105587835, 0.2689868239986718, 0.022863801855891968, 0.014857847746814493, -0.004991497471993052, -0.2841924983442814, -0.01120928052829014, 0.01613911088747882, 0.17055468919052602, -0.11093449793030938, 0.22069275286721116, -0.3300500810075081, 0.01737261011175662, -0.07869274005686182, -0.11030756850266951, 0.06537394639432609, -0.056943400253946556, 0.023650399985416605, -0.05582893463452801, 0.10522998831506175, -0.18527653376626368, -0.03304211090109119, -0.0157595947377568, 0.1517211838239701, -0.10926242658258428, -0.21329032074988336, 0.2123170610427047, -0.04050905263428535, 0.05678436209503326, 0.14262345765068624, -0.16313016045343154, -0.00943266050157094, 0.266389846358291, -0.2202087113036536, 0.31447976908324493, 0.1597295932515817, 0.27981301719407603, -0.10626710148157884, 0.20207683311682245, -0.004797042164411372, -0.1114328215827292, -0.016729899718744508, 0.23705215833760737, -0.11241440904013367, 0.15700990919035693, 0.4457392898845084, -0.1426777445677188, 0.04394762497289654], [1.3141821522128858, 1.75489802161381, 2.0676713194351204, 2.5497663916574775, 1.5267616207099823, 2.1197886692317067, 1.700750731344615, 2.301151192740128, 2.439948154451741, 2.2947695950263345, 2.239148071099645, 2.905450611635579, 2.1760328159801725, 1.7046945311046178, 2.038879025464805, 3.391954880995644, 2.485519045538639, 2.008434759072007, 1.945233408661104, 2.8891700683134234, 2.282873403210996, 2.5712838695067646, 2.2949115892721093, 2.123344626984662, 3.128666920565025, 2.484152194057851, 1.6294855536082387, 2.278632926223172, 1.9645568023379363, 2.0459606712259597, 1.3735837024431405, 2.7143715199741734, 2.2442852857632385, 2.177619138436001, 1.6100243433471038, 1.92554931877437, 2.748003581152767, 2.2589913900139167, 1.9887604931922236, 2.3258348148827266, null, null, null, null, null, 2.0853990204409154, 2.1647895536154382, 2.0875633761660835, 2.4507317303820413, 2.5091764429763215]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#tb7179925c3c24780b90ecf6bb0dfada8 .toyplot-mark-popup");
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
    
                var root_id = "tb7179925c3c24780b90ecf6bb0dfada8";
                var axes = {"t7861663641fe4afbb5fc189266d9fc03": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 4.0, "min": -4.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}], "tb3b24fd167014ae2b86839d537a572e1": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Finally, as you might imagine, null values in the middle boundary affect
both sets of adjacent bars:

.. code:: python

    boundaries[20:30, 1] = numpy.ma.masked
    toyplot.bars(boundaries, baseline=None, width=600, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="tdef606e17baa4123b1124d4a0995beb4"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t8366e7bc8ce04548a84683e2518a05c2" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t6f80d2a9c8ef4a778f2fbe5e28fd7e4e"><clipPath id="t0621b282fd2b42f7bdcc7085e3de380b"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t0621b282fd2b42f7bdcc7085e3de380b)"><g class="toyplot-mark-BarBoundaries" id="te7f66d0d78484c1e993e008e8042107e" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="41.124886758810902" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="50.0" y="148.54314610623697"></rect><rect class="toyplot-Datum" height="64.885658758042752" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="59.900990099009903" y="149.50980091535425"></rect><rect class="toyplot-Datum" height="62.87696965424351" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="69.801980198019805" y="148.3310372360304"></rect><rect class="toyplot-Datum" height="69.997674465261497" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="79.702970297029694" y="143.2753294000332"></rect><rect class="toyplot-Datum" height="82.501417492153649" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="89.603960396039611" y="149.42840495360269"></rect><rect class="toyplot-Datum" height="46.326924651116002" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="149.00990099009903" y="145.73613277023685"></rect><rect class="toyplot-Datum" height="52.561105990677191" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="158.91089108910893" y="152.77336244825773"></rect><rect class="toyplot-Datum" height="85.056334836108647" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="168.8118811881188" y="144.48268117831972"></rect><rect class="toyplot-Datum" height="58.905583127282796" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="178.71287128712871" y="158.25125202518771"></rect><rect class="toyplot-Datum" height="63.014138319186571" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="188.61386138613864" y="149.56568474720609"></rect><rect class="toyplot-Datum" height="72.35001712740231" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="198.51485148514851" y="151.96731850142154"></rect><rect class="toyplot-Datum" height="73.007794676062616" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="208.41584158415844" y="152.75768921256673"></rect><rect class="toyplot-Datum" height="55.655094814497886" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="218.31683168316835" y="148.36565134014185"></rect><rect class="toyplot-Datum" height="44.540815836606896" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="228.21782178217819" y="151.42358500634865"></rect><rect class="toyplot-Datum" height="46.755380192199283" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="238.11881188118812" y="149.40874000036459"></rect><rect class="toyplot-Datum" height="49.027114574529321" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="347.02970297029702" y="148.58039094762415"></rect><rect class="toyplot-Datum" height="93.531336035253645" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="356.93069306930693" y="146.43441355873284"></rect><rect class="toyplot-Datum" height="51.337424781626623" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="366.83168316831689" y="154.07825401133579"></rect><rect class="toyplot-Datum" height="60.490945794015943" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="376.73267326732673" y="150.23581651253929"></rect><rect class="toyplot-Datum" height="72.194880577789064" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="386.63366336633669" y="143.34025384104271"></rect><rect class="toyplot-Datum" height="51.280316576822145" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="396.53465346534654" y="155.50521778259136"></rect><rect class="toyplot-Datum" height="51.111843367290277" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="406.43564356435638" y="142.13800577291889"></rect><rect class="toyplot-Datum" height="35.967193645099485" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="416.33663366336634" y="146.00676016871046"></rect><rect class="toyplot-Datum" height="73.958528556259012" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="426.23762376237624" y="143.0046745701481"></rect><rect class="toyplot-Datum" height="60.174265591715852" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="436.13861386138615" y="152.65667753703949"></rect><rect class="toyplot-Datum" height="48.41514577829588" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="446.03960396039605" y="144.94807917207945"></rect><rect class="toyplot-Datum" height="51.619053396184796" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="455.94059405940595" y="150.11992605411029"></rect><rect class="toyplot-Datum" height="61.122021648515982" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="465.84158415841586" y="152.78582053956825"></rect><rect class="toyplot-Datum" height="58.021022312282071" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="475.7425742574257" y="150.41824749296862"></rect><rect class="toyplot-Datum" height="55.370287321516685" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="485.64356435643566" y="144.07369604155983"></rect><rect class="toyplot-Datum" height="49.712837742341037" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="495.54455445544556" y="152.81036022600333"></rect><rect class="toyplot-Datum" height="68.884116575022944" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="505.44554455445547" y="146.07475227024108"></rect><rect class="toyplot-Datum" height="63.0528769251423" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="515.34653465346537" y="138.8565177528873"></rect><rect class="toyplot-Datum" height="58.041902212709687" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="525.24752475247521" y="153.56694361419298"></rect><rect class="toyplot-Datum" height="53.473929725144416" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="535.14851485148517" y="148.90130937567758"></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="31.39769991155913" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="50.0" y="117.14544619467785"></rect><rect class="toyplot-Datum" height="43.382251455699503" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="59.900990099009903" y="106.12754945965474"></rect><rect class="toyplot-Datum" height="50.022820221908418" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="69.801980198019805" y="98.308217014121979"></rect><rect class="toyplot-Datum" height="57.019489191470143" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="79.702970297029694" y="86.255840208563058"></rect><rect class="toyplot-Datum" height="37.597445471352273" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="89.603960396039611" y="111.83095948225042"></rect><rect class="toyplot-Datum" height="52.623270537122309" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098885" x="99.504950495049513" y="97.005283269207339"></rect><rect class="toyplot-Datum" height="42.643555720415193" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099169" x="109.4059405940594" y="107.48123171638461"></rect><rect class="toyplot-Datum" height="64.633592277110225" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="119.30693069306932" y="92.471220181496804"></rect><rect class="toyplot-Datum" height="61.278935874500775" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="129.20792079207922" y="89.001296138706465"></rect><rect class="toyplot-Datum" height="56.965762103471405" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="139.1089108910891" y="92.630760124341634"></rect><rect class="toyplot-Datum" height="51.714834547727989" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="149.00990099009903" y="94.021298222508861"></rect><rect class="toyplot-Datum" height="75.409627739147226" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="158.91089108910893" y="77.363734709110503"></rect><rect class="toyplot-Datum" height="48.883501577824035" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="168.8118811881188" y="95.599179600495688"></rect><rect class="toyplot-Datum" height="50.868615302803164" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="178.71287128712871" y="107.38263672238455"></rect><rect class="toyplot-Datum" height="50.537660383826221" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098743" x="188.61386138613864" y="99.02802436337987"></rect><rect class="toyplot-Datum" height="86.766190526312656" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="198.51485148514851" y="65.201127975108889"></rect><rect class="toyplot-Datum" height="64.895665351032719" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="208.41584158415844" y="87.862023861534013"></rect><rect class="toyplot-Datum" height="48.576520316942009" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="218.31683168316835" y="99.789131023199843"></rect><rect class="toyplot-Datum" height="50.054420222876246" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099311" x="228.21782178217819" y="101.3691647834724"></rect><rect class="toyplot-Datum" height="71.637991708200175" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="238.11881188118812" y="77.770748292164413"></rect><rect class="toyplot-Datum" height="32.919983508702671" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="347.02970297029702" y="115.66040743892148"></rect><rect class="toyplot-Datum" height="64.293701558087193" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="356.93069306930693" y="82.140712000645649"></rect><rect class="toyplot-Datum" height="60.185386155416751" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="366.83168316831689" y="93.892867855919036"></rect><rect class="toyplot-Datum" height="54.676294973439298" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="376.73267326732673" y="95.55952153909999"></rect><rect class="toyplot-Datum" height="33.590862424720299" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="386.63366336633669" y="109.74939141632241"></rect><rect class="toyplot-Datum" height="53.643950751950598" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="396.53465346534654" y="101.86126703064076"></rect><rect class="toyplot-Datum" height="60.838095301738079" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="406.43564356435638" y="81.299910471180809"></rect><rect class="toyplot-Datum" height="52.481544919058365" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="416.33663366336634" y="93.525215249652092"></rect><rect class="toyplot-Datum" height="42.723686899953691" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="426.23762376237624" y="100.28098767019441"></rect><rect class="toyplot-Datum" height="60.802547909107659" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="436.13861386138615" y="91.854129627931826"></rect><rect class="toyplot-Datum" height="54.945335737026213" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="495.54455445544556" y="97.865024488977113"></rect><rect class="toyplot-Datum" height="50.194491110627041" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099027" x="505.44554455445547" y="95.880261159614037"></rect><rect class="toyplot-Datum" height="41.045602157039383" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990098458" x="515.34653465346537" y="97.810915595847916"></rect><rect class="toyplot-Datum" height="64.835236873744009" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="525.24752475247521" y="88.731706740448971"></rect><rect class="toyplot-Datum" height="61.630720450085619" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.9009900990099595" x="535.14851485148517" y="87.270588925591966"></rect></g></g></g><g class="toyplot-coordinates-Axis" id="t33c26ff3468a4dc7acc77975a6825612" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="495.049504950495" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(4.9504950495049505,6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(103.96039603960395,6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(202.97029702970298,6)"><tspan style="dominant-baseline:inherit">20</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(301.98019801980195,6)"><tspan style="dominant-baseline:inherit">30</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.99009900990103,6)"><tspan style="dominant-baseline:inherit">40</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,6)"><tspan style="dominant-baseline:inherit">50</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t82c67f04c1b74e638b60d71bc2d10325" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0.4658807274178889" x2="184.79887202489112" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">-4</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,-6)"><tspan style="dominant-baseline:inherit">-2</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,-6)"><tspan style="dominant-baseline:inherit">2</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">4</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "te7f66d0d78484c1e993e008e8042107e", "columns": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5], [0.05827415575052086, 0.019607963385830277, 0.0667585105587835, 0.2689868239986718, 0.022863801855891968, 0.014857847746814493, -0.004991497471993052, -0.2841924983442814, -0.01120928052829014, 0.01613911088747882, 0.17055468919052602, -0.11093449793030938, 0.22069275286721116, -0.3300500810075081, 0.01737261011175662, -0.07869274005686182, -0.11030756850266951, 0.06537394639432609, -0.056943400253946556, 0.023650399985416605, null, null, null, null, null, null, null, null, null, null, 0.05678436209503326, 0.14262345765068624, -0.16313016045343154, -0.00943266050157094, 0.266389846358291, -0.2202087113036536, 0.31447976908324493, 0.1597295932515817, 0.27981301719407603, -0.10626710148157884, 0.20207683311682245, -0.004797042164411372, -0.1114328215827292, -0.016729899718744508, 0.23705215833760737, -0.11241440904013367, 0.15700990919035693, 0.4457392898845084, -0.1426777445677188, 0.04394762497289654], [1.3141821522128858, 1.75489802161381, 2.0676713194351204, 2.5497663916574775, 1.5267616207099823, 2.1197886692317067, 1.700750731344615, 2.301151192740128, 2.439948154451741, 2.2947695950263345, 2.239148071099645, 2.905450611635579, 2.1760328159801725, 1.7046945311046178, 2.038879025464805, 3.391954880995644, 2.485519045538639, 2.008434759072007, 1.945233408661104, 2.8891700683134234, 2.282873403210996, 2.5712838695067646, 2.2949115892721093, 2.123344626984662, 3.128666920565025, 2.484152194057851, 1.6294855536082387, 2.278632926223172, 1.9645568023379363, 2.0459606712259597, 1.3735837024431405, 2.7143715199741734, 2.2442852857632385, 2.177619138436001, 1.6100243433471038, 1.92554931877437, 2.748003581152767, 2.2589913900139167, 1.9887604931922236, 2.3258348148827266, null, null, null, null, null, 2.0853990204409154, 2.1647895536154382, 2.0875633761660835, 2.4507317303820413, 2.5091764429763215]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#tdef606e17baa4123b1124d4a0995beb4 .toyplot-mark-popup");
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
    
                var root_id = "tdef606e17baa4123b1124d4a0995beb4";
                var axes = {"t33c26ff3468a4dc7acc77975a6825612": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "t82c67f04c1b74e638b60d71bc2d10325": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 4.0, "min": -4.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Of course, these behaviors extended to other plot types too:

.. code:: python

    toyplot.fill(magnitudes, baseline="stacked", width=600, height=300);  



.. raw:: html

    <div align="center" class="toyplot" id="t8b0a5c09a3e240bf954ebf1aa60bb59c"><svg class="toyplot-canvas-Canvas" height="300.0px" id="td89641e25ca743dc905a5692844b69be" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t4ed19571b29b41f3927c79b1407cd9e3"><clipPath id="t41d266b7a1484814941e7ceb882a0d6c"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t41d266b7a1484814941e7ceb882a0d6c)"><g class="toyplot-mark-FillMagnitudes" id="t69715ef2186c44888fb32e8397776ef9" style="stroke:none"><polygon points="50.0,250.0 60.0,250.0 70.0,250.0 80.0,250.0 90.0,250.0 90.0,160.0 80.0,170.0 70.0,180.0 60.0,160.0 50.0,170.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon><polygon points="200.0,250.0 210.0,250.0 220.0,250.0 230.0,250.0 240.0,250.0 250.0,250.0 260.0,250.0 270.0,250.0 280.0,250.0 290.0,250.0 300.0,250.0 310.0,250.0 320.0,250.0 330.00000000000006,250.0 340.0,250.0 350.0,250.0 360.0,250.0 370.0,250.0 380.0,250.0 390.0,250.0 400.0,250.0 410.0,250.0 420.0,250.0 430.0,250.0 440.0,250.0 450.0,250.0 460.0,250.0 470.0,250.0 480.0,250.0 490.0,250.0 500.0,250.0 510.0,250.0 520.0,250.0 530.0,250.0 540.0,250.0 540.0,160.0 530.0,190.0 520.0,190.0 510.0,180.0 500.0,190.0 490.0,180.0 480.0,190.0 470.0,180.0 460.0,190.0 450.0,200.0 440.0,190.0 430.0,160.0 420.0,190.0 410.0,180.0 400.0,170.0 390.0,190.0 380.0,180.0 370.0,160.0 360.0,160.0 350.0,180.0 340.0,180.0 330.00000000000006,160.0 320.0,170.0 310.0,160.0 300.0,180.0 290.0,180.0 280.0,190.0 270.0,170.0 260.0,180.0 250.0,160.0 240.0,200.0 230.0,160.0 220.0,200.0 210.0,200.0 200.0,190.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon><polygon points="50.0,170.0 60.0,160.0 70.0,180.0 80.0,170.0 90.0,160.0 90.0,70.0 80.0,120.0 70.0,89.999999999999986 60.0,89.999999999999986 50.0,110.00000000000001" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon><polygon points="200.0,190.0 210.0,200.0 220.0,200.0 230.0,160.0 240.0,200.0 250.0,160.0 260.0,180.0 270.0,170.0 280.0,190.0 290.0,180.0 300.0,180.0 310.0,160.0 320.0,170.0 330.00000000000006,160.0 340.0,180.0 350.0,180.0 360.0,160.0 370.0,160.0 380.0,180.0 390.0,190.0 400.0,170.0 410.0,180.0 420.0,190.0 430.0,160.0 440.0,190.0 450.0,200.0 460.0,190.0 470.0,180.0 480.0,190.0 490.0,180.0 500.0,190.0 510.0,180.0 520.0,190.0 530.0,190.0 540.0,160.0 540.0,70.0 530.0,110.00000000000001 520.0,140.0 510.0,130.0 500.0,130.0 490.0,89.999999999999986 480.0,120.0 470.0,100.0 460.0,100.0 450.0,130.0 440.0,120.0 430.0,100.0 420.0,130.0 410.0,130.0 400.0,80.0 390.0,130.0 380.0,110.00000000000001 370.0,80.0 360.0,89.999999999999986 350.0,110.00000000000001 340.0,100.0 330.00000000000006,110.00000000000001 320.0,100.0 310.0,110.00000000000001 300.0,120.0 290.0,130.0 280.0,130.0 270.0,80.0 260.0,130.0 250.0,70.0 240.0,150.0 230.0,110.00000000000001 220.0,110.00000000000001 210.0,120.0 200.0,100.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon></g></g><g class="toyplot-coordinates-Axis" id="t4a524ce848ea460b94ec46e7afeaa1ac" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="490.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)"><tspan style="dominant-baseline:inherit">20</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(300.0,6)"><tspan style="dominant-baseline:inherit">30</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,6)"><tspan style="dominant-baseline:inherit">40</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,6)"><tspan style="dominant-baseline:inherit">50</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t865e72e76fc1429ba8c3a55708a1b40d" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="180.0" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,-6)"><tspan style="dominant-baseline:inherit">5</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,-6)"><tspan style="dominant-baseline:inherit">15</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">20</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Fill Data", "names": ["x", "y0", "y1"], "id": "t69715ef2186c44888fb32e8397776ef9", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [8.0, 9.0, 7.0, 8.0, 9.0, null, null, null, null, null, null, null, null, null, null, 6.0, 5.0, 5.0, 9.0, 5.0, 9.0, 7.0, 8.0, 6.0, 7.0, 7.0, 9.0, 8.0, 9.0, 7.0, 7.0, 9.0, 9.0, 7.0, 6.0, 8.0, 7.0, 6.0, 9.0, 6.0, 5.0, 6.0, 7.0, 6.0, 7.0, 6.0, 7.0, 6.0, 6.0, 9.0], [6.0, 7.0, 9.0, 5.0, 9.0, 6.0, 7.0, 6.0, 6.0, 8.0, 9.0, 6.0, 8.0, 7.0, 5.0, 9.0, 8.0, 9.0, 5.0, 5.0, 9.0, 5.0, 9.0, 6.0, 5.0, 6.0, 5.0, 7.0, 5.0, 8.0, 7.0, 7.0, 8.0, 7.0, 6.0, 9.0, 5.0, 6.0, 6.0, 7.0, 7.0, 9.0, 8.0, 7.0, 9.0, 6.0, 5.0, 5.0, 8.0, 9.0]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t8b0a5c09a3e240bf954ebf1aa60bb59c .toyplot-mark-popup");
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
    
                var root_id = "t8b0a5c09a3e240bf954ebf1aa60bb59c";
                var axes = {"t4a524ce848ea460b94ec46e7afeaa1ac": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "t865e72e76fc1429ba8c3a55708a1b40d": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


.. code:: python

    toyplot.fill(boundaries, width=600, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="t6f0421c8d7a54be8b57f706c85e2f431"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t33c0f679ba374d5694bc7cf324c39b5a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t31e4b59cca4b40369043ff09004f4eb0"><clipPath id="t25ecc9fb36004ba49b1f60b8dcd83d31"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t25ecc9fb36004ba49b1f60b8dcd83d31)"><g class="toyplot-mark-FillBoundaries" id="t19d68214dc744d66a98863509f93f271" style="stroke:none"><polygon points="50.0,189.66803286504788 60.0,214.395459673397 70.0,211.20800689027391 80.0,213.2730038652947 90.0,231.92982244575634 90.0,149.42840495360269 80.0,143.2753294000332 70.0,148.3310372360304 60.0,149.50980091535425 50.0,148.54314610623697" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon><polygon points="150.0,192.06305742135285 160.0,205.33446843893492 170.0,229.53901601442837 180.0,217.15683515247051 190.00000000000003,212.57982306639266 200.0,224.31733562882386 210.0,225.76548388862935 220.0,204.02074615463974 230.0,195.96440084295554 240.0,196.16412019256387 240.0,149.40874000036459 230.0,151.42358500634865 220.0,148.36565134014185 210.0,152.75768921256673 200.0,151.96731850142154 190.00000000000003,149.56568474720609 180.0,158.25125202518771 170.0,144.48268117831972 160.0,152.77336244825773 150.0,145.73613277023685" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon><polygon points="350.0,197.60750552215347 360.0,239.96574959398649 370.0,205.41567879296241 380.0,210.72676230655523 390.0,215.53513441883177 400.0,206.7855343594135 410.0,193.24984914020916 420.0,181.97395381380994 430.0,216.96320312640711 440.0,212.83094312875534 450.0,193.36322495037533 460.0,201.73897945029509 470.0,213.90784218808423 480.0,208.43926980525069 490.0,199.44398336307651 500.0,202.52319796834436 510.0,214.95886884526402 520.0,201.9093946780296 530.0,211.60884582690267 540.0,202.375239100822 540.0,148.90130937567758 530.0,153.56694361419298 520.0,138.8565177528873 510.0,146.07475227024108 500.0,152.81036022600333 490.0,144.07369604155983 480.0,150.41824749296862 470.0,152.78582053956825 460.0,150.11992605411029 450.0,144.94807917207945 440.0,152.65667753703949 430.0,143.0046745701481 420.0,146.00676016871046 410.0,142.13800577291889 400.0,155.50521778259136 390.0,143.34025384104271 380.0,150.23581651253929 370.0,154.07825401133579 360.0,146.43441355873284 350.0,148.58039094762415" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon><polygon points="50.0,148.54314610623697 60.0,149.50980091535425 70.0,148.3310372360304 80.0,143.2753294000332 90.0,149.42840495360269 100.0,149.62855380632965 110.0,150.12478743679981 120.00000000000001,157.10481245860703 130.0,150.28023201320724 140.0,149.59652222781304 150.0,145.73613277023685 160.0,152.77336244825773 170.0,144.48268117831972 180.0,158.25125202518771 190.00000000000003,149.56568474720609 200.0,151.96731850142154 210.0,152.75768921256673 220.0,148.36565134014185 230.0,151.42358500634865 240.0,149.40874000036459 240.0,77.770748292164413 230.0,101.3691647834724 220.0,99.789131023199843 210.0,87.862023861534013 200.0,65.201127975108889 190.00000000000003,99.02802436337987 180.0,107.38263672238455 170.0,95.599179600495688 160.0,77.363734709110503 150.0,94.021298222508861 140.0,92.630760124341634 130.0,89.001296138706465 120.00000000000001,92.471220181496804 110.0,107.48123171638461 100.0,97.005283269207339 90.0,111.83095948225042 80.0,86.255840208563058 70.0,98.308217014121979 60.0,106.12754945965474 50.0,117.14544619467785" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon><polygon points="350.0,148.58039094762415 360.0,146.43441355873284 370.0,154.07825401133579 380.0,150.23581651253929 390.0,143.34025384104271 400.0,155.50521778259136 410.0,142.13800577291889 420.0,146.00676016871046 430.0,143.0046745701481 440.0,152.65667753703949 440.0,91.854129627931826 430.0,100.28098767019441 420.0,93.525215249652092 410.0,81.299910471180809 400.0,101.86126703064076 390.0,109.74939141632241 380.0,95.55952153909999 370.0,93.892867855919036 360.0,82.140712000645649 350.0,115.66040743892148" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon><polygon points="500.0,152.81036022600333 510.0,146.07475227024108 520.0,138.8565177528873 530.0,153.56694361419298 540.0,148.90130937567758 540.0,87.270588925591966 530.0,88.731706740448971 520.0,97.810915595847916 510.0,95.880261159614037 500.0,97.865024488977113" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon></g></g><g class="toyplot-coordinates-Axis" id="t04f09f0b9d034bf5a573af72fc8e447b" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="490.0" y1="0" y2="0"></line><g><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,6)"><tspan style="dominant-baseline:inherit">10</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,6)"><tspan style="dominant-baseline:inherit">20</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(300.0,6)"><tspan style="dominant-baseline:inherit">30</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(400.0,6)"><tspan style="dominant-baseline:inherit">40</tspan></text><text style="dominant-baseline:hanging;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(500.0,6)"><tspan style="dominant-baseline:inherit">50</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tb597512af83147e59d45c84081aa11e0" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0.4658807274178889" x2="184.79887202489112" y1="0" y2="0"></line><g><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,-6)"><tspan style="dominant-baseline:inherit">-4</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(50.0,-6)"><tspan style="dominant-baseline:inherit">-2</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(100.0,-6)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(150.0,-6)"><tspan style="dominant-baseline:inherit">2</tspan></text><text style="dominant-baseline:alphabetic;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="translate(200.0,-6)"><tspan style="dominant-baseline:inherit">4</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Fill Data", "names": ["x", "y0", "y1", "y2"], "id": "t19d68214dc744d66a98863509f93f271", "columns": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [-1.5867213146019146, -2.5758183869358797, -2.448320275610957, -2.5309201546117883, -3.2771928978302536, null, null, null, null, null, -1.682522296854114, -2.213378737557397, -3.1815606405771346, -2.6862734060988207, -2.5031929226557064, -2.972693425152954, -3.030619355545173, -2.1608298461855897, -1.8385760337182218, -1.846564807702554, -3.9813647709032844, -2.5373211653277234, -3.429621159497361, -1.914503729770202, -2.534078379838995, -2.286891975369565, -1.8774128452237937, -1.7607909095315055, -2.4205866621692667, -2.2171955801286054, -1.904300220886139, -3.598629983759458, -2.2166271517184963, -2.4290704922622086, -2.621405376753271, -2.2714213743765406, -1.729993965608367, -1.2789581525523985, -2.678528125056284, -2.513237725150213, -1.734528998015013, -2.069559178011802, -2.556313687523369, -2.337570792210029, -1.977759334523061, -2.100927918733774, -2.5983547538105602, -2.076375787121184, -2.4643538330761063, -2.0950095640328796], [0.05827415575052086, 0.019607963385830277, 0.0667585105587835, 0.2689868239986718, 0.022863801855891968, 0.014857847746814493, -0.004991497471993052, -0.2841924983442814, -0.01120928052829014, 0.01613911088747882, 0.17055468919052602, -0.11093449793030938, 0.22069275286721116, -0.3300500810075081, 0.01737261011175662, -0.07869274005686182, -0.11030756850266951, 0.06537394639432609, -0.056943400253946556, 0.023650399985416605, null, null, null, null, null, null, null, null, null, null, 0.05678436209503326, 0.14262345765068624, -0.16313016045343154, -0.00943266050157094, 0.266389846358291, -0.2202087113036536, 0.31447976908324493, 0.1597295932515817, 0.27981301719407603, -0.10626710148157884, 0.20207683311682245, -0.004797042164411372, -0.1114328215827292, -0.016729899718744508, 0.23705215833760737, -0.11241440904013367, 0.15700990919035693, 0.4457392898845084, -0.1426777445677188, 0.04394762497289654], [1.3141821522128858, 1.75489802161381, 2.0676713194351204, 2.5497663916574775, 1.5267616207099823, 2.1197886692317067, 1.700750731344615, 2.301151192740128, 2.439948154451741, 2.2947695950263345, 2.239148071099645, 2.905450611635579, 2.1760328159801725, 1.7046945311046178, 2.038879025464805, 3.391954880995644, 2.485519045538639, 2.008434759072007, 1.945233408661104, 2.8891700683134234, 2.282873403210996, 2.5712838695067646, 2.2949115892721093, 2.123344626984662, 3.128666920565025, 2.484152194057851, 1.6294855536082387, 2.278632926223172, 1.9645568023379363, 2.0459606712259597, 1.3735837024431405, 2.7143715199741734, 2.2442852857632385, 2.177619138436001, 1.6100243433471038, 1.92554931877437, 2.748003581152767, 2.2589913900139167, 1.9887604931922236, 2.3258348148827266, null, null, null, null, null, 2.0853990204409154, 2.1647895536154382, 2.0875633761660835, 2.4507317303820413, 2.5091764429763215]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t6f0421c8d7a54be8b57f706c85e2f431 .toyplot-mark-popup");
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
    
                var root_id = "t6f0421c8d7a54be8b57f706c85e2f431";
                var axes = {"t04f09f0b9d034bf5a573af72fc8e447b": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "tb597512af83147e59d45c84081aa11e0": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 4.0, "min": -4.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Finally, a special-case worth mentioning is Toyplot table
visualizations, which *can* make an explicit distinction between null
and NaN values:

.. code:: python

    data = toyplot.data.Table()
    data["a"] = numpy.random.random(11)
    data["b"] = numpy.random.random(11)
    data["a", 3] = numpy.ma.masked
    data["b", 7] = numpy.nan
    toyplot.table(data, width=300, height=350);



.. raw:: html

    <div align="center" class="toyplot" id="tdfaced45208b49dab5d0aed3a1a5c69c"><svg class="toyplot-canvas-Canvas" height="350.0px" id="tc929b02ab07b4f3397b35351282a5336" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 350.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="ta60dc800795c4c76bec7717af460f64d"><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(100.0,60.416666666666664)"><tspan style="dominant-baseline:inherit">a</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(200.0,60.416666666666664)"><tspan style="dominant-baseline:inherit">b</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,81.25)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,81.25)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,81.25)"><tspan style="dominant-baseline:inherit">854699</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,81.25)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,81.25)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,81.25)"><tspan style="dominant-baseline:inherit">703196</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,102.08333333333333)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,102.08333333333333)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,102.08333333333333)"><tspan style="dominant-baseline:inherit">652144</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,102.08333333333333)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,102.08333333333333)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,102.08333333333333)"><tspan style="dominant-baseline:inherit">282864</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,122.91666666666666)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,122.91666666666666)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,122.91666666666666)"><tspan style="dominant-baseline:inherit">351356</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,122.91666666666666)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,122.91666666666666)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,122.91666666666666)"><tspan style="dominant-baseline:inherit">267843</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,143.75)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,143.75)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,143.75)"><tspan style="dominant-baseline:inherit">290331</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,164.58333333333331)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,164.58333333333331)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,164.58333333333331)"><tspan style="dominant-baseline:inherit">525642</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,164.58333333333331)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,164.58333333333331)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,164.58333333333331)"><tspan style="dominant-baseline:inherit">252136</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,185.41666666666666)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,185.41666666666666)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,185.41666666666666)"><tspan style="dominant-baseline:inherit">688357</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,185.41666666666666)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,185.41666666666666)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,185.41666666666666)"><tspan style="dominant-baseline:inherit">554338</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,206.25)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,206.25)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,206.25)"><tspan style="dominant-baseline:inherit">00359724</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,206.25)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,206.25)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,206.25)"><tspan style="dominant-baseline:inherit">24377</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,227.08333333333331)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,227.08333333333331)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,227.08333333333331)"><tspan style="dominant-baseline:inherit">464203</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,227.08333333333331)"><tspan style="dominant-baseline:inherit">nan</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,247.91666666666669)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,247.91666666666669)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,247.91666666666669)"><tspan style="dominant-baseline:inherit">36197</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,247.91666666666669)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,247.91666666666669)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,247.91666666666669)"><tspan style="dominant-baseline:inherit">437727</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,268.75)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,268.75)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,268.75)"><tspan style="dominant-baseline:inherit">768892</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,268.75)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,268.75)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,268.75)"><tspan style="dominant-baseline:inherit">629987</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,289.58333333333337)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,289.58333333333337)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,289.58333333333337)"><tspan style="dominant-baseline:inherit">64803</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,289.58333333333337)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,289.58333333333337)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,289.58333333333337)"><tspan style="dominant-baseline:inherit">0805395</tspan></text><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.0" y1="70.833333333333329" y2="70.833333333333329"></line></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Table Data", "names": ["a", "b"], "id": "ta60dc800795c4c76bec7717af460f64d", "columns": [[0.8546985458000165, 0.6521438665467723, 0.35135558723048876, null, 0.5256423658225312, 0.6883568191104394, 0.0035972436420587117, 0.4642028564132139, 0.36197021830778475, 0.7688923107277068, 0.6480303399869547], [0.7031955820495314, 0.2828638121547319, 0.26784347224046023, 0.29033147812120086, 0.25213599038012935, 0.5543377858633207, 0.2437703411894253, NaN, 0.43772749237222575, 0.6299872032985078, 0.08053945448948319]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#tdfaced45208b49dab5d0aed3a1a5c69c .toyplot-mark-popup");
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


If you would rather not make this distinction, you can specify a table
formatter object that will treat NaN and null values the same:

.. code:: python

    canvas, table = toyplot.table(data, width=300, height=350)
    table.column(1).format = toyplot.format.FloatFormatter(nanshow=False)


.. parsed-literal::

    WARNING:toyplot:table.column is deprecated, use table.cells.column instead.
    WARNING:toyplot:column() is deprecated, use column[] instead.



.. raw:: html

    <div align="center" class="toyplot" id="t28846ebb14984a93845c3986ee6bec59"><svg class="toyplot-canvas-Canvas" height="350.0px" id="t49eba45b27ee47fa9c080876f830846b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 350.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Table" id="t697412a3946448b5a7f8f89610365dfc"><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(100.0,60.416666666666664)"><tspan style="dominant-baseline:inherit">a</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="translate(200.0,60.416666666666664)"><tspan style="dominant-baseline:inherit">b</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,81.25)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,81.25)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,81.25)"><tspan style="dominant-baseline:inherit">854699</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,81.25)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,81.25)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,81.25)"><tspan style="dominant-baseline:inherit">703196</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,102.08333333333333)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,102.08333333333333)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,102.08333333333333)"><tspan style="dominant-baseline:inherit">652144</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,102.08333333333333)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,102.08333333333333)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,102.08333333333333)"><tspan style="dominant-baseline:inherit">282864</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,122.91666666666666)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,122.91666666666666)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,122.91666666666666)"><tspan style="dominant-baseline:inherit">351356</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,122.91666666666666)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,122.91666666666666)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,122.91666666666666)"><tspan style="dominant-baseline:inherit">267843</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,143.75)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,143.75)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,143.75)"><tspan style="dominant-baseline:inherit">290331</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,164.58333333333331)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,164.58333333333331)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,164.58333333333331)"><tspan style="dominant-baseline:inherit">525642</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,164.58333333333331)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,164.58333333333331)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,164.58333333333331)"><tspan style="dominant-baseline:inherit">252136</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,185.41666666666666)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,185.41666666666666)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,185.41666666666666)"><tspan style="dominant-baseline:inherit">688357</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,185.41666666666666)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,185.41666666666666)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,185.41666666666666)"><tspan style="dominant-baseline:inherit">554338</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,206.25)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,206.25)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,206.25)"><tspan style="dominant-baseline:inherit">00359724</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,206.25)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,206.25)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,206.25)"><tspan style="dominant-baseline:inherit">24377</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,227.08333333333331)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,227.08333333333331)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,227.08333333333331)"><tspan style="dominant-baseline:inherit">464203</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,247.91666666666669)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,247.91666666666669)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,247.91666666666669)"><tspan style="dominant-baseline:inherit">36197</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,247.91666666666669)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,247.91666666666669)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,247.91666666666669)"><tspan style="dominant-baseline:inherit">437727</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,268.75)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,268.75)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,268.75)"><tspan style="dominant-baseline:inherit">768892</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,268.75)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,268.75)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,268.75)"><tspan style="dominant-baseline:inherit">629987</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(98.0,289.58333333333337)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(100.0,289.58333333333337)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(102.0,289.58333333333337)"><tspan style="dominant-baseline:inherit">64803</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" transform="translate(198.0,289.58333333333337)"><tspan style="dominant-baseline:inherit">0</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" transform="translate(200.0,289.58333333333337)"><tspan style="dominant-baseline:inherit">.</tspan></text><text style="dominant-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" transform="translate(202.0,289.58333333333337)"><tspan style="dominant-baseline:inherit">0805395</tspan></text><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.0" y1="70.833333333333329" y2="70.833333333333329"></line></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Table Data", "names": ["a", "b"], "id": "t697412a3946448b5a7f8f89610365dfc", "columns": [[0.8546985458000165, 0.6521438665467723, 0.35135558723048876, null, 0.5256423658225312, 0.6883568191104394, 0.0035972436420587117, 0.4642028564132139, 0.36197021830778475, 0.7688923107277068, 0.6480303399869547], [0.7031955820495314, 0.2828638121547319, 0.26784347224046023, 0.29033147812120086, 0.25213599038012935, 0.5543377858633207, 0.2437703411894253, NaN, 0.43772749237222575, 0.6299872032985078, 0.08053945448948319]], "filename": "toyplot"}];
    
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
                  var popup = document.querySelector("#t28846ebb14984a93845c3986ee6bec59 .toyplot-mark-popup");
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

