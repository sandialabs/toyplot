
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


.. parsed-literal::

    /Users/tshead/src/toyplot/toyplot/projection.py:21: RuntimeWarning: invalid value encountered in greater_equal
      return numpy.logical_and(left <= x, x <= right)
    /Users/tshead/src/toyplot/toyplot/projection.py:21: RuntimeWarning: invalid value encountered in less_equal
      return numpy.logical_and(left <= x, x <= right)



.. raw:: html

    <div align="center" class="toyplot" id="tc0635015a6814e288ca93c269b68c311"><svg height="300.0px" id="t583761af37374dbd85e87adc874eccda" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t0ca6ff4050934a0cbaefed8493e620ba"><clipPath id="tf9234caad1624600ba75b6bb0e6e0d9f"><rect height="200.0" width="500.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tf9234caad1624600ba75b6bb0e6e0d9f)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-Plot" id="t8e7ccebf2daa4e058b6d64409983d3d9" style="fill:none"><g class="toyplot-Series"><path d="M 60.0 150.0 L 69.795918367346943 138.49105544839446 L 79.591836734693871 127.17108744814433 L 89.387755102040813 116.22596956085634 L 99.183673469387742 105.83542031964561 L 108.97959183673468 96.170052255790551 M 255.91836734693874 100.90185889105058 L 265.71428571428572 110.95046347941975 L 275.51020408163265 121.64026037787411 L 285.30612244897958 132.79572341687648 L 295.10204081632651 144.23368020173581 L 304.89795918367349 155.76631979826411 L 314.69387755102036 167.20427658312349 L 324.48979591836735 178.3597396221258 L 334.28571428571428 189.04953652058023 L 344.08163265306121 199.09814110894936 L 353.87755102040819 208.34055557770094 L 363.67346938775506 216.6250197367784 L 373.46938775510199 223.81550291372602 L 383.26530612244892 229.79393757357002 L 393.0612244897959 234.46215798447844 L 402.85714285714289 237.74351209636413 L 412.65306122448976 239.58412016542783 L 422.44897959183675 239.95375945806191 L 432.24489795918362 238.84636050730055 L 442.0408163265306 236.28010677329945 L 451.83673469387747 232.29713607142313 L 461.63265306122446 226.96284867048118 L 471.42857142857139 220.3648334221227 L 481.22448979591832 212.61142955431384 L 491.0204081632653 203.82994774420948 L 500.81632653061223 194.16457968035448 L 510.61224489795916 183.7740304391437 L 520.40816326530603 172.82891255185575 L 530.20408163265301 161.50894455160562 L 540.0 150.00000000000003" style="fill:none;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="60.0" cy="150.0" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="69.795918367346943" cy="138.49105544839446" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="79.591836734693871" cy="127.17108744814433" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="89.387755102040813" cy="116.22596956085634" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="99.183673469387742" cy="105.83542031964561" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="108.97959183673468" cy="96.170052255790551" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="255.91836734693874" cy="100.90185889105058" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="265.71428571428572" cy="110.95046347941975" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="275.51020408163265" cy="121.64026037787411" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="285.30612244897958" cy="132.79572341687648" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="295.10204081632651" cy="144.23368020173581" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="304.89795918367349" cy="155.76631979826411" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="314.69387755102036" cy="167.20427658312349" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="324.48979591836735" cy="178.3597396221258" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="334.28571428571428" cy="189.04953652058023" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="344.08163265306121" cy="199.09814110894936" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="353.87755102040819" cy="208.34055557770094" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="363.67346938775506" cy="216.6250197367784" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="373.46938775510199" cy="223.81550291372602" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="383.26530612244892" cy="229.79393757357002" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="393.0612244897959" cy="234.46215798447844" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="402.85714285714289" cy="237.74351209636413" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="412.65306122448976" cy="239.58412016542783" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="422.44897959183675" cy="239.95375945806191" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="432.24489795918362" cy="238.84636050730055" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="442.0408163265306" cy="236.28010677329945" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="451.83673469387747" cy="232.29713607142313" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="461.63265306122446" cy="226.96284867048118" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="471.42857142857139" cy="220.3648334221227" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="481.22448979591832" cy="212.61142955431384" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="491.0204081632653" cy="203.82994774420948" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="500.81632653061223" cy="194.16457968035448" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="510.61224489795916" cy="183.7740304391437" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="520.40816326530603" cy="172.82891255185575" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="530.20408163265301" cy="161.50894455160562" r="2.2360679774997898"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="540.0" cy="150.00000000000003" r="2.2360679774997898"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="60.0" x2="540.0" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="212.7887453682195" y="250.0">2</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="365.5774907364391" y="250.0">4</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="518.3662361046586" y="250.0">6</text></g><line style="" x1="50.0" x2="50.0" y1="96.17005225579055" y2="239.9537594580619"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">-1.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 195.0)" x="50.0" y="195.0">-0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0.0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 105.0)" x="50.0" y="105.0">0.5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tc0635015a6814e288ca93c269b68c311 text");
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
          var text = document.querySelectorAll("#tc0635015a6814e288ca93c269b68c311 text");
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
      var data_tables = [{"data": [[0.0, 0.1282282715750936, 0.2564565431501872, 0.38468481472528077, 0.5129130863003744, 0.6411413578754679, 0.7693696294505615, 0.8975979010256552, 1.0258261726007487, 1.1540544441758422, 1.2822827157509358, 1.4105109873260295, 1.538739258901123, 1.6669675304762166, 1.7951958020513104, 1.9234240736264039, 2.0516523452014974, 2.179880616776591, 2.3081088883516845, 2.436337159926778, 2.5645654315018716, 2.6927937030769655, 2.821021974652059, 2.9492502462271526, 3.077478517802246, 3.2057067893773397, 3.333935060952433, 3.4621633325275267, 3.5903916041026207, 3.7186198756777142, 3.8468481472528078, 3.9750764188279013, 4.103304690402995, 4.231532961978089, 4.359761233553182, 4.487989505128276, 4.616217776703369, 4.744446048278463, 4.872674319853556, 5.00090259142865, 5.129130863003743, 5.257359134578837, 5.385587406153931, 5.513815677729024, 5.642043949304118, 5.770272220879211, 5.898500492454305, 6.026728764029398, 6.154957035604492, 6.283185307179586], [0.0, 0.127877161684506, 0.25365458390950735, 0.3752670048793741, 0.49071755200393785, 0.5981105304912159, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 0.545534901210549, 0.43388373911755823, 0.3151082180236208, 0.19115862870137254, 0.06407021998071323, -0.06407021998071254, -0.19115862870137187, -0.3151082180236202, -0.433883739117558, -0.5455349012105485, -0.6482283953077882, -0.7402779970753153, -0.8201722545969556, -0.8865993063730001, -0.9384684220497602, -0.9749279121818235, -0.9953791129491981, -0.9994862162006879, -0.9871817834144503, -0.9586678530366608, -0.9144126230158128, -0.8551427630053465, -0.7818314824680299, -0.6956825506034869, -0.5981105304912162, -0.49071755200393863, -0.3752670048793746, -0.25365458390950835, -0.12787716168450664, -2.4492935982947064e-16]], "title": "Plot Data", "names": ["x", "y0"], "id": "t8e7ccebf2daa4e058b6d64409983d3d9", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#tc0635015a6814e288ca93c269b68c311 .toyplot-mark-popup");
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
      var axes = {"t0ca6ff4050934a0cbaefed8493e620ba": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 6.2831853071795862, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1, "min": -1.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
      function sign(x)
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
    
      function to_domain(projection, range)
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
              return sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
            }
          }
        }
      }
    
      // Compute mouse coordinates relative to a DOM object, with thanks to d3js.org, where this code originated.
      function d3_mousePoint(container, e)
      {
        if (e.changedTouches) e = e.changedTouches[0];
        var svg = container.ownerSVGElement || container;
        if (svg.createSVGPoint) {
          var point = svg.createSVGPoint();
          point.x = e.clientX, point.y = e.clientY;
          point = point.matrixTransform(container.getScreenCTM().inverse());
          return [point.x, point.y];
        }
        var rect = container.getBoundingClientRect();
        return [e.clientX - rect.left - container.clientLeft, e.clientY - rect.top - container.clientTop];
      };
    
      function display_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var data = axes[dom_axes.id];
    
        point = d3_mousePoint(e.target, e);
        var x = Number(to_domain(data["x"], point[0])).toFixed(2);
        var y = Number(to_domain(data["y"], point[1])).toFixed(2);
    
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
        {
          coordinates[i].style.visibility = "visible";
          coordinates[i].querySelector("text").textContent = "x=" + x + " y=" + y;
        }
      }
    
      function clear_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
          coordinates[i].style.visibility = "hidden";
      }
    
      for(var axes_id in axes)
      {
        var event_target = document.querySelector("#" + axes_id + " .toyplot-coordinate-events");
        event_target.onmousemove = display_coordinates;
        event_target.onmouseout = clear_coordinates;
      }
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

    <div align="center" class="toyplot" id="t0c5f5d862ed24c94b021777937fcc34e"><svg height="300.0px" id="t163e6b63201b4abeac2a3ad9c4a6e25d" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t648d7afbcbc6418caaf9611c830bc0e7"><clipPath id="tfd39da2459a2418989b5daab5620a92c"><rect height="200.0" width="500.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tfd39da2459a2418989b5daab5620a92c)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-BarMagnitudes" id="t9a248db34c30478ab8f937b7624a7cfe" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="119.99999999999999" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="60.0" y="120.00000000000001"></rect><rect class="toyplot-Datum" height="180.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="69.504950495049499" y="60.0"></rect><rect class="toyplot-Datum" height="160.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="79.009900990099013" y="80.0"></rect><rect class="toyplot-Datum" height="140.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="88.514851485148512" y="100.0"></rect><rect class="toyplot-Datum" height="140.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="98.019801980198025" y="100.0"></rect><rect class="toyplot-Datum" height="100.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="202.57425742574256" y="140.0"></rect><rect class="toyplot-Datum" height="180.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="212.0792079207921" y="60.0"></rect><rect class="toyplot-Datum" height="100.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="221.58415841584159" y="140.0"></rect><rect class="toyplot-Datum" height="59.999999999999972" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="231.08910891089107" y="180.00000000000003"></rect><rect class="toyplot-Datum" height="59.999999999999972" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="240.59405940594058" y="180.00000000000003"></rect><rect class="toyplot-Datum" height="140.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="250.09900990099013" y="100.0"></rect><rect class="toyplot-Datum" height="160.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="259.60396039603961" y="80.0"></rect><rect class="toyplot-Datum" height="59.999999999999972" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="269.10891089108912" y="180.00000000000003"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="278.61386138613864" y="160.0"></rect><rect class="toyplot-Datum" height="180.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="288.11881188118809" y="60.0"></rect><rect class="toyplot-Datum" height="180.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="297.62376237623761" y="60.0"></rect><rect class="toyplot-Datum" height="100.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="307.12871287128718" y="140.0"></rect><rect class="toyplot-Datum" height="59.999999999999972" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="316.63366336633663" y="180.00000000000003"></rect><rect class="toyplot-Datum" height="119.99999999999999" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="326.13861386138615" y="120.00000000000001"></rect><rect class="toyplot-Datum" height="140.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="335.64356435643566" y="100.0"></rect><rect class="toyplot-Datum" height="160.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="345.14851485148512" y="80.0"></rect><rect class="toyplot-Datum" height="100.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="354.65346534653463" y="140.0"></rect><rect class="toyplot-Datum" height="180.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="364.1584158415842" y="60.0"></rect><rect class="toyplot-Datum" height="100.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="373.66336633663366" y="140.0"></rect><rect class="toyplot-Datum" height="119.99999999999999" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="383.16831683168317" y="120.00000000000001"></rect><rect class="toyplot-Datum" height="119.99999999999999" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="392.67326732673268" y="120.00000000000001"></rect><rect class="toyplot-Datum" height="59.999999999999972" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="402.17821782178214" y="180.00000000000003"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="411.68316831683171" y="160.0"></rect><rect class="toyplot-Datum" height="119.99999999999999" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="421.18811881188117" y="120.00000000000001"></rect><rect class="toyplot-Datum" height="59.999999999999972" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="430.69306930693068" y="180.00000000000003"></rect><rect class="toyplot-Datum" height="119.99999999999999" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="440.19801980198025" y="120.00000000000001"></rect><rect class="toyplot-Datum" height="100.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="449.70297029702971" y="140.0"></rect><rect class="toyplot-Datum" height="119.99999999999999" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="459.20792079207916" y="120.00000000000001"></rect><rect class="toyplot-Datum" height="140.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="468.71287128712873" y="100.0"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="478.21782178217819" y="160.0"></rect><rect class="toyplot-Datum" height="119.99999999999999" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="487.7227722772277" y="120.00000000000001"></rect><rect class="toyplot-Datum" height="119.99999999999999" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="497.22772277227727" y="120.00000000000001"></rect><rect class="toyplot-Datum" height="119.99999999999999" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="506.73267326732673" y="120.00000000000001"></rect><rect class="toyplot-Datum" height="100.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="516.23762376237619" y="140.0"></rect><rect class="toyplot-Datum" height="80.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="525.74257425742564" y="160.0"></rect></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="60.0" x2="535.2475247524752" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="64.75247524752474" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="159.8019801980198" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="254.85148514851485" y="250.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="349.9009900990099" y="250.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="444.950495049505" y="250.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">50</text></g><line style="" x1="50.0" x2="50.0" y1="60.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 180.00000000000003)" x="50.0" y="180.00000000000003">3</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 120.00000000000001)" x="50.0" y="120.00000000000001">6</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">9</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t0c5f5d862ed24c94b021777937fcc34e text");
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
          var text = document.querySelectorAll("#t0c5f5d862ed24c94b021777937fcc34e text");
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
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [6.0, 9.0, 8.0, 7.0, 7.0, null, null, null, null, null, null, null, null, null, null, 5.0, 9.0, 5.0, 3.0, 3.0, 7.0, 8.0, 3.0, 4.0, 9.0, 9.0, 5.0, 3.0, 6.0, 7.0, 8.0, 5.0, 9.0, 5.0, 6.0, 6.0, 3.0, 4.0, 6.0, 3.0, 6.0, 5.0, 6.0, 7.0, 4.0, 6.0, 6.0, 6.0, 5.0, 4.0]], "title": "Bar Data", "names": ["left", "right", "baseline", "magnitude0"], "id": "t9a248db34c30478ab8f937b7624a7cfe", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t0c5f5d862ed24c94b021777937fcc34e .toyplot-mark-popup");
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
      var axes = {"t648d7afbcbc6418caaf9611c830bc0e7": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 9.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
      function sign(x)
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
    
      function to_domain(projection, range)
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
              return sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
            }
          }
        }
      }
    
      // Compute mouse coordinates relative to a DOM object, with thanks to d3js.org, where this code originated.
      function d3_mousePoint(container, e)
      {
        if (e.changedTouches) e = e.changedTouches[0];
        var svg = container.ownerSVGElement || container;
        if (svg.createSVGPoint) {
          var point = svg.createSVGPoint();
          point.x = e.clientX, point.y = e.clientY;
          point = point.matrixTransform(container.getScreenCTM().inverse());
          return [point.x, point.y];
        }
        var rect = container.getBoundingClientRect();
        return [e.clientX - rect.left - container.clientLeft, e.clientY - rect.top - container.clientTop];
      };
    
      function display_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var data = axes[dom_axes.id];
    
        point = d3_mousePoint(e.target, e);
        var x = Number(to_domain(data["x"], point[0])).toFixed(2);
        var y = Number(to_domain(data["y"], point[1])).toFixed(2);
    
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
        {
          coordinates[i].style.visibility = "visible";
          coordinates[i].querySelector("text").textContent = "x=" + x + " y=" + y;
        }
      }
    
      function clear_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
          coordinates[i].style.visibility = "hidden";
      }
    
      for(var axes_id in axes)
      {
        var event_target = document.querySelector("#" + axes_id + " .toyplot-coordinate-events");
        event_target.onmousemove = display_coordinates;
        event_target.onmouseout = clear_coordinates;
      }
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

    <div align="center" class="toyplot" id="td6b111fc5cc84913b941e16d6606ffe0"><svg height="300.0px" id="tc53a2bb82fff498a857b23a7873afbc8" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t02f97a75fc29468aab35e5cea9d7fdc4"><clipPath id="te2887eb72a69456692fa23944632e1b6"><rect height="200.0" width="500.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#te2887eb72a69456692fa23944632e1b6)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-BarMagnitudes" id="t44232c4ccd4b4c92b42e1a7abc4efe2d" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="72.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="60.0" y="168.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="69.504950495049499" y="159.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="79.009900990099013" y="177.0"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="88.514851485148512" y="168.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="98.019801980198025" y="159.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="107.52475247524754" y="240.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="117.02970297029702" y="240.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="126.53465346534654" y="240.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="136.03960396039605" y="240.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="145.54455445544554" y="240.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="155.04950495049508" y="240.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="164.55445544554456" y="240.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="174.05940594059405" y="240.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="183.56435643564359" y="240.0"></rect><rect class="toyplot-Datum" height="0.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="193.06930693069307" y="240.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="202.57425742574256" y="186.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="212.0792079207921" y="195.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="221.58415841584159" y="195.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="231.08910891089107" y="159.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="240.59405940594058" y="195.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="250.09900990099013" y="159.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="259.60396039603961" y="177.0"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="269.10891089108912" y="168.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="278.61386138613864" y="186.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="288.11881188118809" y="177.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="297.62376237623761" y="177.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="307.12871287128718" y="159.0"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="316.63366336633663" y="168.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="326.13861386138615" y="159.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="335.64356435643566" y="177.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="345.14851485148512" y="177.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="354.65346534653463" y="159.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="364.1584158415842" y="159.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="373.66336633663366" y="177.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="383.16831683168317" y="186.0"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="392.67326732673268" y="168.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="402.17821782178214" y="177.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="411.68316831683171" y="186.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="421.18811881188117" y="159.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="430.69306930693068" y="186.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="440.19801980198025" y="195.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="449.70297029702971" y="186.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="459.20792079207916" y="177.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="468.71287128712873" y="186.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="478.21782178217819" y="177.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="487.7227722772277" y="186.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="497.22772277227727" y="177.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="506.73267326732673" y="186.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="516.23762376237619" y="186.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="525.74257425742564" y="159.0"></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="53.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="60.0" y="114.00000000000001"></rect><rect class="toyplot-Datum" height="63.000000000000014" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="69.504950495049499" y="95.999999999999986"></rect><rect class="toyplot-Datum" height="81.000000000000014" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="79.009900990099013" y="95.999999999999986"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="88.514851485148512" y="123.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="98.019801980198025" y="78.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="107.52475247524754" y="186.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="117.02970297029702" y="177.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="126.53465346534654" y="186.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="136.03960396039605" y="186.0"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="145.54455445544554" y="168.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="155.04950495049508" y="159.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="164.55445544554456" y="186.0"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="174.05940594059405" y="168.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="183.56435643564359" y="177.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="193.06930693069307" y="195.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="202.57425742574256" y="105.0"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="212.0792079207921" y="123.0"></rect><rect class="toyplot-Datum" height="80.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="221.58415841584159" y="114.00000000000001"></rect><rect class="toyplot-Datum" height="44.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="231.08910891089107" y="114.00000000000001"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="240.59405940594058" y="150.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="250.09900990099013" y="78.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="259.60396039603961" y="132.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="269.10891089108912" y="87.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="278.61386138613864" y="132.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="288.11881188118809" y="132.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="297.62376237623761" y="123.0"></rect><rect class="toyplot-Datum" height="44.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="307.12871287128718" y="114.00000000000001"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="316.63366336633663" y="105.0"></rect><rect class="toyplot-Datum" height="44.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="326.13861386138615" y="114.00000000000001"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="335.64356435643566" y="105.0"></rect><rect class="toyplot-Datum" height="62.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="345.14851485148512" y="114.00000000000001"></rect><rect class="toyplot-Datum" height="63.000000000000014" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="354.65346534653463" y="95.999999999999986"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="364.1584158415842" y="87.0"></rect><rect class="toyplot-Datum" height="62.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="373.66336633663366" y="114.00000000000001"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="383.16831683168317" y="132.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="392.67326732673268" y="87.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="402.17821782178214" y="132.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="411.68316831683171" y="132.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="421.18811881188117" y="105.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="430.69306930693068" y="123.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="440.19801980198025" y="132.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="449.70297029702971" y="105.0"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="459.20792079207916" y="105.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="468.71287128712873" y="123.0"></rect><rect class="toyplot-Datum" height="81.000000000000014" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="478.21782178217819" y="95.999999999999986"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="487.7227722772277" y="132.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="497.22772277227727" y="132.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="506.73267326732673" y="141.0"></rect><rect class="toyplot-Datum" height="71.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="516.23762376237619" y="114.00000000000001"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="525.74257425742564" y="78.0"></rect></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="60.0" x2="535.2475247524752" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="64.75247524752474" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="159.8019801980198" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="254.85148514851485" y="250.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="349.9009900990099" y="250.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="444.950495049505" y="250.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">50</text></g><line style="" x1="50.0" x2="50.0" y1="78.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 195.0)" x="50.0" y="195.0">5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">10</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 105.0)" x="50.0" y="105.0">15</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">20</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#td6b111fc5cc84913b941e16d6606ffe0 text");
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
          var text = document.querySelectorAll("#td6b111fc5cc84913b941e16d6606ffe0 text");
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
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [8.0, 9.0, 7.0, 8.0, 9.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.0, 5.0, 5.0, 9.0, 5.0, 9.0, 7.0, 8.0, 6.0, 7.0, 7.0, 9.0, 8.0, 9.0, 7.0, 7.0, 9.0, 9.0, 7.0, 6.0, 8.0, 7.0, 6.0, 9.0, 6.0, 5.0, 6.0, 7.0, 6.0, 7.0, 6.0, 7.0, 6.0, 6.0, 9.0], [6.0, 7.0, 9.0, 5.0, 9.0, 6.0, 7.0, 6.0, 6.0, 8.0, 9.0, 6.0, 8.0, 7.0, 5.0, 9.0, 8.0, 9.0, 5.0, 5.0, 9.0, 5.0, 9.0, 6.0, 5.0, 6.0, 5.0, 7.0, 5.0, 8.0, 7.0, 7.0, 8.0, 7.0, 6.0, 9.0, 5.0, 6.0, 6.0, 7.0, 7.0, 9.0, 8.0, 7.0, 9.0, 6.0, 5.0, 5.0, 8.0, 9.0]], "title": "Bar Data", "names": ["left", "right", "baseline", "magnitude0", "magnitude1"], "id": "t44232c4ccd4b4c92b42e1a7abc4efe2d", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#td6b111fc5cc84913b941e16d6606ffe0 .toyplot-mark-popup");
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
      var axes = {"t02f97a75fc29468aab35e5cea9d7fdc4": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
      function sign(x)
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
    
      function to_domain(projection, range)
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
              return sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
            }
          }
        }
      }
    
      // Compute mouse coordinates relative to a DOM object, with thanks to d3js.org, where this code originated.
      function d3_mousePoint(container, e)
      {
        if (e.changedTouches) e = e.changedTouches[0];
        var svg = container.ownerSVGElement || container;
        if (svg.createSVGPoint) {
          var point = svg.createSVGPoint();
          point.x = e.clientX, point.y = e.clientY;
          point = point.matrixTransform(container.getScreenCTM().inverse());
          return [point.x, point.y];
        }
        var rect = container.getBoundingClientRect();
        return [e.clientX - rect.left - container.clientLeft, e.clientY - rect.top - container.clientTop];
      };
    
      function display_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var data = axes[dom_axes.id];
    
        point = d3_mousePoint(e.target, e);
        var x = Number(to_domain(data["x"], point[0])).toFixed(2);
        var y = Number(to_domain(data["y"], point[1])).toFixed(2);
    
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
        {
          coordinates[i].style.visibility = "visible";
          coordinates[i].querySelector("text").textContent = "x=" + x + " y=" + y;
        }
      }
    
      function clear_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
          coordinates[i].style.visibility = "hidden";
      }
    
      for(var axes_id in axes)
      {
        var event_target = document.querySelector("#" + axes_id + " .toyplot-coordinate-events");
        event_target.onmousemove = display_coordinates;
        event_target.onmouseout = clear_coordinates;
      }
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

    <div align="center" class="toyplot" id="t8699b1ce1e1e40eab9ba57297f24504b"><svg height="300.0px" id="tf443d984102e40278e32a73f6a024992" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tba4599258fdd4072aa48a3bd4dea7e84"><clipPath id="te30dfdbcf04d47e7a1dd2fff65b843c1"><rect height="200.0" width="500.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#te30dfdbcf04d47e7a1dd2fff65b843c1)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-BarMagnitudes" id="td5c27df207214979b03f0d5dd8950ed4" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="72.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="60.0" y="168.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="69.504950495049499" y="159.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="79.009900990099013" y="177.0"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="88.514851485148512" y="168.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="98.019801980198025" y="159.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="202.57425742574256" y="186.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="212.0792079207921" y="195.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="221.58415841584159" y="195.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="231.08910891089107" y="159.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="240.59405940594058" y="195.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="250.09900990099013" y="159.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="259.60396039603961" y="177.0"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="269.10891089108912" y="168.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="278.61386138613864" y="186.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="288.11881188118809" y="177.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="297.62376237623761" y="177.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="307.12871287128718" y="159.0"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="316.63366336633663" y="168.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="326.13861386138615" y="159.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="335.64356435643566" y="177.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="345.14851485148512" y="177.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="354.65346534653463" y="159.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="364.1584158415842" y="159.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="373.66336633663366" y="177.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="383.16831683168317" y="186.0"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="392.67326732673268" y="168.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="402.17821782178214" y="177.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="411.68316831683171" y="186.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="421.18811881188117" y="159.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="430.69306930693068" y="186.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="440.19801980198025" y="195.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="449.70297029702971" y="186.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="459.20792079207916" y="177.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="468.71287128712873" y="186.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="478.21782178217819" y="177.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="487.7227722772277" y="186.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="497.22772277227727" y="177.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="506.73267326732673" y="186.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="516.23762376237619" y="186.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="525.74257425742564" y="159.0"></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="53.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="60.0" y="114.00000000000001"></rect><rect class="toyplot-Datum" height="63.000000000000014" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="69.504950495049499" y="95.999999999999986"></rect><rect class="toyplot-Datum" height="81.000000000000014" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="79.009900990099013" y="95.999999999999986"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="88.514851485148512" y="123.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="98.019801980198025" y="78.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="202.57425742574256" y="105.0"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="212.0792079207921" y="123.0"></rect><rect class="toyplot-Datum" height="80.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="221.58415841584159" y="114.00000000000001"></rect><rect class="toyplot-Datum" height="44.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="231.08910891089107" y="114.00000000000001"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="240.59405940594058" y="150.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="250.09900990099013" y="78.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="259.60396039603961" y="132.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="269.10891089108912" y="87.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="278.61386138613864" y="132.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="288.11881188118809" y="132.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="297.62376237623761" y="123.0"></rect><rect class="toyplot-Datum" height="44.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="307.12871287128718" y="114.00000000000001"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="316.63366336633663" y="105.0"></rect><rect class="toyplot-Datum" height="44.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="326.13861386138615" y="114.00000000000001"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="335.64356435643566" y="105.0"></rect><rect class="toyplot-Datum" height="62.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="345.14851485148512" y="114.00000000000001"></rect><rect class="toyplot-Datum" height="63.000000000000014" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="354.65346534653463" y="95.999999999999986"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="364.1584158415842" y="87.0"></rect><rect class="toyplot-Datum" height="62.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="373.66336633663366" y="114.00000000000001"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="383.16831683168317" y="132.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="392.67326732673268" y="87.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="402.17821782178214" y="132.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="411.68316831683171" y="132.0"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="421.18811881188117" y="105.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="430.69306930693068" y="123.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="440.19801980198025" y="132.0"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="449.70297029702971" y="105.0"></rect><rect class="toyplot-Datum" height="72.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="459.20792079207916" y="105.0"></rect><rect class="toyplot-Datum" height="63.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="468.71287128712873" y="123.0"></rect><rect class="toyplot-Datum" height="81.000000000000014" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="478.21782178217819" y="95.999999999999986"></rect><rect class="toyplot-Datum" height="54.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="487.7227722772277" y="132.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="497.22772277227727" y="132.0"></rect><rect class="toyplot-Datum" height="45.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="506.73267326732673" y="141.0"></rect><rect class="toyplot-Datum" height="71.999999999999986" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="516.23762376237619" y="114.00000000000001"></rect><rect class="toyplot-Datum" height="81.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="525.74257425742564" y="78.0"></rect></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="60.0" x2="535.2475247524752" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="64.75247524752474" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="159.8019801980198" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="254.85148514851485" y="250.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="349.9009900990099" y="250.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="444.950495049505" y="250.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">50</text></g><line style="" x1="50.0" x2="50.0" y1="78.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 195.0)" x="50.0" y="195.0">5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">10</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 105.0)" x="50.0" y="105.0">15</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">20</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t8699b1ce1e1e40eab9ba57297f24504b text");
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
          var text = document.querySelectorAll("#t8699b1ce1e1e40eab9ba57297f24504b text");
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
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [8.0, 9.0, 7.0, 8.0, 9.0, null, null, null, null, null, null, null, null, null, null, 6.0, 5.0, 5.0, 9.0, 5.0, 9.0, 7.0, 8.0, 6.0, 7.0, 7.0, 9.0, 8.0, 9.0, 7.0, 7.0, 9.0, 9.0, 7.0, 6.0, 8.0, 7.0, 6.0, 9.0, 6.0, 5.0, 6.0, 7.0, 6.0, 7.0, 6.0, 7.0, 6.0, 6.0, 9.0], [6.0, 7.0, 9.0, 5.0, 9.0, 6.0, 7.0, 6.0, 6.0, 8.0, 9.0, 6.0, 8.0, 7.0, 5.0, 9.0, 8.0, 9.0, 5.0, 5.0, 9.0, 5.0, 9.0, 6.0, 5.0, 6.0, 5.0, 7.0, 5.0, 8.0, 7.0, 7.0, 8.0, 7.0, 6.0, 9.0, 5.0, 6.0, 6.0, 7.0, 7.0, 9.0, 8.0, 7.0, 9.0, 6.0, 5.0, 5.0, 8.0, 9.0]], "title": "Bar Data", "names": ["left", "right", "baseline", "magnitude0", "magnitude1"], "id": "td5c27df207214979b03f0d5dd8950ed4", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t8699b1ce1e1e40eab9ba57297f24504b .toyplot-mark-popup");
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
      var axes = {"tba4599258fdd4072aa48a3bd4dea7e84": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
      function sign(x)
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
    
      function to_domain(projection, range)
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
              return sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
            }
          }
        }
      }
    
      // Compute mouse coordinates relative to a DOM object, with thanks to d3js.org, where this code originated.
      function d3_mousePoint(container, e)
      {
        if (e.changedTouches) e = e.changedTouches[0];
        var svg = container.ownerSVGElement || container;
        if (svg.createSVGPoint) {
          var point = svg.createSVGPoint();
          point.x = e.clientX, point.y = e.clientY;
          point = point.matrixTransform(container.getScreenCTM().inverse());
          return [point.x, point.y];
        }
        var rect = container.getBoundingClientRect();
        return [e.clientX - rect.left - container.clientLeft, e.clientY - rect.top - container.clientTop];
      };
    
      function display_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var data = axes[dom_axes.id];
    
        point = d3_mousePoint(e.target, e);
        var x = Number(to_domain(data["x"], point[0])).toFixed(2);
        var y = Number(to_domain(data["y"], point[1])).toFixed(2);
    
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
        {
          coordinates[i].style.visibility = "visible";
          coordinates[i].querySelector("text").textContent = "x=" + x + " y=" + y;
        }
      }
    
      function clear_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
          coordinates[i].style.visibility = "hidden";
      }
    
      for(var axes_id in axes)
      {
        var event_target = document.querySelector("#" + axes_id + " .toyplot-coordinate-events");
        event_target.onmousemove = display_coordinates;
        event_target.onmouseout = clear_coordinates;
      }
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

    <div align="center" class="toyplot" id="tff4d889cb9184885a202f4589f494cdf"><svg height="300.0px" id="t7098b2d300b2468bb67a13adb5824cb7" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t3e9d59bfbf684cdc97b9eb94b4ca5687"><clipPath id="t0c6dd7bb6f5d4ef98dfab7b96bace775"><rect height="200.0" width="500.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t0c6dd7bb6f5d4ef98dfab7b96bace775)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-BarBoundaries" id="t8ca952fa6cae470c9467db10746f1467" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="37.01239808292982" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="60.0" y="148.68883149561327"></rect><rect class="toyplot-Datum" height="58.397092882238468" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="69.504950495049499" y="149.55882082381882"></rect><rect class="toyplot-Datum" height="56.589272688819165" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="79.009900990099013" y="148.49793351242738"></rect><rect class="toyplot-Datum" height="62.997907018735361" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="88.514851485148512" y="143.94779646002988"></rect><rect class="toyplot-Datum" height="74.251275742938304" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="98.019801980198025" y="149.48556445824244"></rect><rect class="toyplot-Datum" height="42.812132499508863" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="107.52475247524754" y="149.66569842569669"></rect><rect class="toyplot-Datum" height="31.740059480935997" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="117.02970297029702" y="150.11230869311984"></rect><rect class="toyplot-Datum" height="38.563409064276186" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="126.53465346534654" y="156.39433121274632"></rect><rect class="toyplot-Datum" height="37.868434998247636" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="136.03960396039605" y="150.2522088118865"></rect><rect class="toyplot-Datum" height="69.184995309152868" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="145.54455445544554" y="149.63687000503174"></rect><rect class="toyplot-Datum" height="41.694232186004399" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="155.04950495049508" y="146.16251949321315"></rect><rect class="toyplot-Datum" height="47.304995391609509" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="164.55445544554456" y="152.49602620343194"></rect><rect class="toyplot-Datum" height="76.550701352497811" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="174.05940594059405" y="145.03441306048774"></rect><rect class="toyplot-Datum" height="53.015024814554522" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="183.56435643564359" y="157.42612682266892"></rect><rect class="toyplot-Datum" height="56.712724487267963" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="193.06930693069307" y="149.60911627248547"></rect><rect class="toyplot-Datum" height="65.115015414662082" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="202.57425742574256" y="151.77058665127939"></rect><rect class="toyplot-Datum" height="65.70701520845634" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="212.0792079207921" y="152.48192029131008"></rect><rect class="toyplot-Datum" height="50.089585333048092" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="221.58415841584159" y="148.52908620612766"></rect><rect class="toyplot-Datum" height="40.086734252946201" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="231.08910891089107" y="151.28122650571379"></rect><rect class="toyplot-Datum" height="42.079842172979369" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="240.59405940594058" y="149.46786600032812"></rect><rect class="toyplot-Datum" height="88.324556316047023" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="250.09900990099013" y="151.25615102927688"></rect><rect class="toyplot-Datum" height="59.457400956962658" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="259.60396039603961" y="147.63232526291111"></rect><rect class="toyplot-Datum" height="72.997754078949725" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="269.10891089108912" y="154.16872200974092"></rect><rect class="toyplot-Datum" height="42.332886424554971" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="278.61386138613864" y="150.74344749527455"></rect><rect class="toyplot-Datum" height="56.662172664777842" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="288.11881188118809" y="150.35459088159953"></rect><rect class="toyplot-Datum" height="54.868796081854555" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="297.62376237623761" y="146.58627336396066"></rect><rect class="toyplot-Datum" height="39.78338441942725" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="307.12871287128718" y="152.45840459810813"></rect><rect class="toyplot-Datum" height="34.818763247586503" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="316.63366336633663" y="154.79903221687238"></rect><rect class="toyplot-Datum" height="59.240333772269366" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="326.13861386138615" y="145.22286612653915"></rect><rect class="toyplot-Datum" height="48.975446868622186" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="335.64356435643566" y="150.91145368427144"></rect><rect class="toyplot-Datum" height="44.124403117076355" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="345.14851485148512" y="148.72235185286175"></rect><rect class="toyplot-Datum" height="84.178202431728266" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="354.65346534653463" y="146.79097220285956"></rect><rect class="toyplot-Datum" height="46.20368230346395" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="364.1584158415842" y="153.67042861020221"></rect><rect class="toyplot-Datum" height="54.44185121461436" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="373.66336633663366" y="150.21223486128534"></rect><rect class="toyplot-Datum" height="64.975392520010161" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="383.16831683168317" y="144.00622845693846"></rect><rect class="toyplot-Datum" height="46.15228491913993" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="392.67326732673268" y="154.95469600433222"></rect><rect class="toyplot-Datum" height="46.000659030561252" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="402.17821782178214" y="142.924205195627"></rect><rect class="toyplot-Datum" height="32.370474280589519" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="411.68316831683171" y="146.40608415183942"></rect><rect class="toyplot-Datum" height="66.562675700633065" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="421.18811881188117" y="143.70420711313329"></rect><rect class="toyplot-Datum" height="54.156839032544241" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="430.69306930693068" y="152.39100978333553"></rect><rect class="toyplot-Datum" height="43.573631200466309" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="440.19801980198025" y="145.45327125487148"></rect><rect class="toyplot-Datum" height="46.457148056566297" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="449.70297029702971" y="150.10793344869927"></rect><rect class="toyplot-Datum" height="55.009819483664387" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="459.20792079207916" y="152.50723848561142"></rect><rect class="toyplot-Datum" height="52.218920081053881" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="468.71287128712873" y="150.37642274367175"></rect><rect class="toyplot-Datum" height="49.833258589365045" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="478.21782178217819" y="144.66632643740382"></rect><rect class="toyplot-Datum" height="44.741553968106899" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="487.7227722772277" y="152.52932420340301"></rect><rect class="toyplot-Datum" height="61.995704917520641" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="497.22772277227727" y="146.46727704321697"></rect><rect class="toyplot-Datum" height="56.747589232628059" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="506.73267326732673" y="139.97086597759858"></rect><rect class="toyplot-Datum" height="52.237711991438772" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="516.23762376237619" y="153.21024925277365"></rect><rect class="toyplot-Datum" height="48.126536752629988" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="525.74257425742564" y="149.01117843810982"></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="28.2579299204032" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="60.0" y="120.43090157521007"></rect><rect class="toyplot-Datum" height="39.044026310129539" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="69.504950495049499" y="110.51479451368928"></rect><rect class="toyplot-Datum" height="45.020538199717606" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="79.009900990099013" y="103.47739531270977"></rect><rect class="toyplot-Datum" height="51.317540272323129" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="88.514851485148512" y="92.630256187706749"></rect><rect class="toyplot-Datum" height="33.837700924217046" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="98.019801980198025" y="115.64786353402539"></rect><rect class="toyplot-Datum" height="47.360943483410082" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="107.52475247524754" y="102.30475494228661"></rect><rect class="toyplot-Datum" height="38.379200148373684" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="117.02970297029702" y="111.73310854474616"></rect><rect class="toyplot-Datum" height="58.170233049399201" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="126.53465346534654" y="98.224098163347122"></rect><rect class="toyplot-Datum" height="55.151042287050686" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="136.03960396039605" y="95.101166524835818"></rect><rect class="toyplot-Datum" height="51.269185893124273" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="145.54455445544554" y="98.367684111907465"></rect><rect class="toyplot-Datum" height="46.543351092955177" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="155.04950495049508" y="99.619168400257976"></rect><rect class="toyplot-Datum" height="67.868664965232483" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="164.55445544554456" y="84.627361238199455"></rect><rect class="toyplot-Datum" height="43.995151420041623" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="174.05940594059405" y="101.03926164044611"></rect><rect class="toyplot-Datum" height="45.781753772522819" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="183.56435643564359" y="111.6443730501461"></rect><rect class="toyplot-Datum" height="45.483894345443588" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="193.06930693069307" y="104.12522192704188"></rect><rect class="toyplot-Datum" height="78.089571473681389" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="202.57425742574256" y="73.681015177597999"></rect><rect class="toyplot-Datum" height="58.406098815929468" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="212.0792079207921" y="94.075821475380607"></rect><rect class="toyplot-Datum" height="43.718868285247794" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="221.58415841584159" y="104.81021792087986"></rect><rect class="toyplot-Datum" height="45.048978200588635" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="231.08910891089107" y="106.23224830512515"></rect><rect class="toyplot-Datum" height="64.474192537380134" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="240.59405940594058" y="84.993673462947982"></rect><rect class="toyplot-Datum" height="52.620802601524275" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="250.09900990099013" y="98.635348427752604"></rect><rect class="toyplot-Datum" height="55.486212326813316" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="259.60396039603961" y="92.146112936097794"></rect><rect class="toyplot-Datum" height="55.804232768363363" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="269.10891089108912" y="98.364489241377555"></rect><rect class="toyplot-Datum" height="48.518701602429445" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="278.61386138613864" y="102.22474589284511"></rect><rect class="toyplot-Datum" height="70.749596594312607" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="288.11881188118809" y="79.604994287286928"></rect><rect class="toyplot-Datum" height="52.479697730262302" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="297.62376237623761" y="94.106575633698355"></rect><rect class="toyplot-Datum" height="39.121829554293498" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="307.12871287128718" y="113.33657504381463"></rect><rect class="toyplot-Datum" height="56.068273056893744" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="316.63366336633663" y="98.730759159978632"></rect><rect class="toyplot-Datum" height="39.425394179142714" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="326.13861386138615" y="105.79747194739643"></rect><rect class="toyplot-Datum" height="46.945568786855517" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="335.64356435643566" y="103.96588489741592"></rect><rect class="toyplot-Datum" height="29.627985157832398" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="345.14851485148512" y="119.09436669502935"></rect><rect class="toyplot-Datum" height="57.864331402278481" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="354.65346534653463" y="88.926640800581083"></rect><rect class="toyplot-Datum" height="54.166847539875079" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="364.1584158415842" y="99.50358107032713"></rect><rect class="toyplot-Datum" height="49.208665476095348" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="373.66336633663366" y="101.00356938518999"></rect><rect class="toyplot-Datum" height="30.231776182248296" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="383.16831683168317" y="113.77445227469016"></rect><rect class="toyplot-Datum" height="48.279555676755535" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="392.67326732673268" y="106.67514032757668"></rect><rect class="toyplot-Datum" height="54.75428577156427" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="402.17821782178214" y="88.169919424062726"></rect><rect class="toyplot-Datum" height="47.233390427152528" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="411.68316831683171" y="99.172693724686894"></rect><rect class="toyplot-Datum" height="38.45131820995833" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="421.18811881188117" y="105.25288890317496"></rect><rect class="toyplot-Datum" height="54.722293118196887" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="430.69306930693068" y="97.668716665138646"></rect><rect class="toyplot-Datum" height="62.748000019149728" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="440.19801980198025" y="82.705271235721753"></rect><rect class="toyplot-Datum" height="58.205222860642237" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="449.70297029702971" y="91.902710588057033"></rect><rect class="toyplot-Datum" height="56.502306091226671" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="459.20792079207916" y="96.004932394384753"></rect><rect class="toyplot-Datum" height="44.606396179007874" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="468.71287128712873" y="105.77002656466388"></rect><rect class="toyplot-Datum" height="42.010775871180641" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="478.21782178217819" y="102.65555056622318"></rect><rect class="toyplot-Datum" height="49.450802163323601" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="487.7227722772277" y="103.07852204007941"></rect><rect class="toyplot-Datum" height="45.175041999564343" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="497.22772277227727" y="101.29223504365262"></rect><rect class="toyplot-Datum" height="36.941041941335456" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="506.73267326732673" y="103.02982403626312"></rect><rect class="toyplot-Datum" height="58.351713186369579" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="516.23762376237619" y="94.858536066404071"></rect><rect class="toyplot-Datum" height="55.467648405077057" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="525.74257425742564" y="93.543530033032766"></rect></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="60.0" x2="535.2475247524752" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="64.75247524752474" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="159.8019801980198" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="254.85148514851485" y="250.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="349.9009900990099" y="250.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="444.950495049505" y="250.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">50</text></g><line style="" x1="50.0" x2="50.0" y1="73.681015177598" y2="239.5807073453239"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">-4</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 195.0)" x="50.0" y="195.0">-2</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 105.0)" x="50.0" y="105.0">2</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">4</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tff4d889cb9184885a202f4589f494cdf text");
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
          var text = document.querySelectorAll("#tff4d889cb9184885a202f4589f494cdf text");
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
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5], [0.05827415575052086, 0.019607963385830277, 0.0667585105587835, 0.2689868239986718, 0.022863801855891968, 0.014857847746814493, -0.004991497471993052, -0.2841924983442814, -0.01120928052829014, 0.01613911088747882, 0.17055468919052602, -0.11093449793030938, 0.22069275286721116, -0.3300500810075081, 0.01737261011175662, -0.07869274005686182, -0.11030756850266951, 0.06537394639432609, -0.056943400253946556, 0.023650399985416605, -0.05582893463452801, 0.10522998831506175, -0.18527653376626368, -0.03304211090109119, -0.0157595947377568, 0.1517211838239701, -0.10926242658258428, -0.21329032074988336, 0.2123170610427047, -0.04050905263428535, 0.05678436209503326, 0.14262345765068624, -0.16313016045343154, -0.00943266050157094, 0.266389846358291, -0.2202087113036536, 0.31447976908324493, 0.1597295932515817, 0.27981301719407603, -0.10626710148157884, 0.20207683311682245, -0.004797042164411372, -0.1114328215827292, -0.016729899718744508, 0.23705215833760737, -0.11241440904013367, 0.15700990919035693, 0.4457392898845084, -0.1426777445677188, 0.04394762497289654], [1.3141821522128858, 1.75489802161381, 2.0676713194351204, 2.5497663916574775, 1.5267616207099823, 2.1197886692317067, 1.700750731344615, 2.301151192740128, 2.439948154451741, 2.2947695950263345, 2.239148071099645, 2.905450611635579, 2.1760328159801725, 1.7046945311046178, 2.038879025464805, 3.391954880995644, 2.485519045538639, 2.008434759072007, 1.945233408661104, 2.8891700683134234, 2.282873403210996, 2.5712838695067646, 2.2949115892721093, 2.123344626984662, 3.128666920565025, 2.484152194057851, 1.6294855536082387, 2.278632926223172, 1.9645568023379363, 2.0459606712259597, 1.3735837024431405, 2.7143715199741734, 2.2442852857632385, 2.177619138436001, 1.6100243433471038, 1.92554931877437, 2.748003581152767, 2.2589913900139167, 1.9887604931922236, 2.3258348148827266, 2.9908768339679224, 2.58210175164191, 2.3997807824717885, 1.9657765971260497, 2.1041977526123024, 2.0853990204409154, 2.1647895536154382, 2.0875633761660835, 2.4507317303820413, 2.5091764429763215]], "title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "t8ca952fa6cae470c9467db10746f1467", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#tff4d889cb9184885a202f4589f494cdf .toyplot-mark-popup");
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
      var axes = {"t3e9d59bfbf684cdc97b9eb94b4ca5687": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 4.0, "min": -4.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
      function sign(x)
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
    
      function to_domain(projection, range)
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
              return sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
            }
          }
        }
      }
    
      // Compute mouse coordinates relative to a DOM object, with thanks to d3js.org, where this code originated.
      function d3_mousePoint(container, e)
      {
        if (e.changedTouches) e = e.changedTouches[0];
        var svg = container.ownerSVGElement || container;
        if (svg.createSVGPoint) {
          var point = svg.createSVGPoint();
          point.x = e.clientX, point.y = e.clientY;
          point = point.matrixTransform(container.getScreenCTM().inverse());
          return [point.x, point.y];
        }
        var rect = container.getBoundingClientRect();
        return [e.clientX - rect.left - container.clientLeft, e.clientY - rect.top - container.clientTop];
      };
    
      function display_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var data = axes[dom_axes.id];
    
        point = d3_mousePoint(e.target, e);
        var x = Number(to_domain(data["x"], point[0])).toFixed(2);
        var y = Number(to_domain(data["y"], point[1])).toFixed(2);
    
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
        {
          coordinates[i].style.visibility = "visible";
          coordinates[i].querySelector("text").textContent = "x=" + x + " y=" + y;
        }
      }
    
      function clear_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
          coordinates[i].style.visibility = "hidden";
      }
    
      for(var axes_id in axes)
      {
        var event_target = document.querySelector("#" + axes_id + " .toyplot-coordinate-events");
        event_target.onmousemove = display_coordinates;
        event_target.onmouseout = clear_coordinates;
      }
    })();
    </script></div></div>


Now, suppose that some of the lower boundaries in the plot are null:

.. code:: python

    boundaries[5:10, 0] = numpy.ma.masked
    toyplot.bars(boundaries, baseline=None, width=600, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="t1d5d76e053674ba59247f96eb95ff803"><svg height="300.0px" id="t7565b332a75e4a83a4702342282c954b" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tec9635080adf4d6db620e8c9dacbb524"><clipPath id="t62bdf3bb5ef04d439a733c889bda3964"><rect height="200.0" width="500.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t62bdf3bb5ef04d439a733c889bda3964)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-BarBoundaries" id="t9a25838504ed4e28afb000560b51ffd5" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="37.01239808292982" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="60.0" y="148.68883149561327"></rect><rect class="toyplot-Datum" height="58.397092882238468" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="69.504950495049499" y="149.55882082381882"></rect><rect class="toyplot-Datum" height="56.589272688819165" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="79.009900990099013" y="148.49793351242738"></rect><rect class="toyplot-Datum" height="62.997907018735361" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="88.514851485148512" y="143.94779646002988"></rect><rect class="toyplot-Datum" height="74.251275742938304" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="98.019801980198025" y="149.48556445824244"></rect><rect class="toyplot-Datum" height="41.694232186004399" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="155.04950495049508" y="146.16251949321315"></rect><rect class="toyplot-Datum" height="47.304995391609509" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="164.55445544554456" y="152.49602620343194"></rect><rect class="toyplot-Datum" height="76.550701352497811" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="174.05940594059405" y="145.03441306048774"></rect><rect class="toyplot-Datum" height="53.015024814554522" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="183.56435643564359" y="157.42612682266892"></rect><rect class="toyplot-Datum" height="56.712724487267963" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="193.06930693069307" y="149.60911627248547"></rect><rect class="toyplot-Datum" height="65.115015414662082" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="202.57425742574256" y="151.77058665127939"></rect><rect class="toyplot-Datum" height="65.70701520845634" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="212.0792079207921" y="152.48192029131008"></rect><rect class="toyplot-Datum" height="50.089585333048092" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="221.58415841584159" y="148.52908620612766"></rect><rect class="toyplot-Datum" height="40.086734252946201" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="231.08910891089107" y="151.28122650571379"></rect><rect class="toyplot-Datum" height="42.079842172979369" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="240.59405940594058" y="149.46786600032812"></rect><rect class="toyplot-Datum" height="88.324556316047023" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="250.09900990099013" y="151.25615102927688"></rect><rect class="toyplot-Datum" height="59.457400956962658" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="259.60396039603961" y="147.63232526291111"></rect><rect class="toyplot-Datum" height="72.997754078949725" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="269.10891089108912" y="154.16872200974092"></rect><rect class="toyplot-Datum" height="42.332886424554971" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="278.61386138613864" y="150.74344749527455"></rect><rect class="toyplot-Datum" height="56.662172664777842" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="288.11881188118809" y="150.35459088159953"></rect><rect class="toyplot-Datum" height="54.868796081854555" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="297.62376237623761" y="146.58627336396066"></rect><rect class="toyplot-Datum" height="39.78338441942725" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="307.12871287128718" y="152.45840459810813"></rect><rect class="toyplot-Datum" height="34.818763247586503" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="316.63366336633663" y="154.79903221687238"></rect><rect class="toyplot-Datum" height="59.240333772269366" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="326.13861386138615" y="145.22286612653915"></rect><rect class="toyplot-Datum" height="48.975446868622186" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="335.64356435643566" y="150.91145368427144"></rect><rect class="toyplot-Datum" height="44.124403117076355" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="345.14851485148512" y="148.72235185286175"></rect><rect class="toyplot-Datum" height="84.178202431728266" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="354.65346534653463" y="146.79097220285956"></rect><rect class="toyplot-Datum" height="46.20368230346395" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="364.1584158415842" y="153.67042861020221"></rect><rect class="toyplot-Datum" height="54.44185121461436" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="373.66336633663366" y="150.21223486128534"></rect><rect class="toyplot-Datum" height="64.975392520010161" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="383.16831683168317" y="144.00622845693846"></rect><rect class="toyplot-Datum" height="46.15228491913993" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="392.67326732673268" y="154.95469600433222"></rect><rect class="toyplot-Datum" height="46.000659030561252" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="402.17821782178214" y="142.924205195627"></rect><rect class="toyplot-Datum" height="32.370474280589519" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="411.68316831683171" y="146.40608415183942"></rect><rect class="toyplot-Datum" height="66.562675700633065" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="421.18811881188117" y="143.70420711313329"></rect><rect class="toyplot-Datum" height="54.156839032544241" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="430.69306930693068" y="152.39100978333553"></rect><rect class="toyplot-Datum" height="43.573631200466309" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="440.19801980198025" y="145.45327125487148"></rect><rect class="toyplot-Datum" height="46.457148056566297" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="449.70297029702971" y="150.10793344869927"></rect><rect class="toyplot-Datum" height="55.009819483664387" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="459.20792079207916" y="152.50723848561142"></rect><rect class="toyplot-Datum" height="52.218920081053881" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="468.71287128712873" y="150.37642274367175"></rect><rect class="toyplot-Datum" height="49.833258589365045" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="478.21782178217819" y="144.66632643740382"></rect><rect class="toyplot-Datum" height="44.741553968106899" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="487.7227722772277" y="152.52932420340301"></rect><rect class="toyplot-Datum" height="61.995704917520641" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="497.22772277227727" y="146.46727704321697"></rect><rect class="toyplot-Datum" height="56.747589232628059" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="506.73267326732673" y="139.97086597759858"></rect><rect class="toyplot-Datum" height="52.237711991438772" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="516.23762376237619" y="153.21024925277365"></rect><rect class="toyplot-Datum" height="48.126536752629988" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="525.74257425742564" y="149.01117843810982"></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="28.2579299204032" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="60.0" y="120.43090157521007"></rect><rect class="toyplot-Datum" height="39.044026310129539" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="69.504950495049499" y="110.51479451368928"></rect><rect class="toyplot-Datum" height="45.020538199717606" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="79.009900990099013" y="103.47739531270977"></rect><rect class="toyplot-Datum" height="51.317540272323129" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="88.514851485148512" y="92.630256187706749"></rect><rect class="toyplot-Datum" height="33.837700924217046" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="98.019801980198025" y="115.64786353402539"></rect><rect class="toyplot-Datum" height="47.360943483410082" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="107.52475247524754" y="102.30475494228661"></rect><rect class="toyplot-Datum" height="38.379200148373684" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="117.02970297029702" y="111.73310854474616"></rect><rect class="toyplot-Datum" height="58.170233049399201" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="126.53465346534654" y="98.224098163347122"></rect><rect class="toyplot-Datum" height="55.151042287050686" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="136.03960396039605" y="95.101166524835818"></rect><rect class="toyplot-Datum" height="51.269185893124273" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="145.54455445544554" y="98.367684111907465"></rect><rect class="toyplot-Datum" height="46.543351092955177" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="155.04950495049508" y="99.619168400257976"></rect><rect class="toyplot-Datum" height="67.868664965232483" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="164.55445544554456" y="84.627361238199455"></rect><rect class="toyplot-Datum" height="43.995151420041623" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="174.05940594059405" y="101.03926164044611"></rect><rect class="toyplot-Datum" height="45.781753772522819" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="183.56435643564359" y="111.6443730501461"></rect><rect class="toyplot-Datum" height="45.483894345443588" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="193.06930693069307" y="104.12522192704188"></rect><rect class="toyplot-Datum" height="78.089571473681389" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="202.57425742574256" y="73.681015177597999"></rect><rect class="toyplot-Datum" height="58.406098815929468" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="212.0792079207921" y="94.075821475380607"></rect><rect class="toyplot-Datum" height="43.718868285247794" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="221.58415841584159" y="104.81021792087986"></rect><rect class="toyplot-Datum" height="45.048978200588635" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="231.08910891089107" y="106.23224830512515"></rect><rect class="toyplot-Datum" height="64.474192537380134" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="240.59405940594058" y="84.993673462947982"></rect><rect class="toyplot-Datum" height="52.620802601524275" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="250.09900990099013" y="98.635348427752604"></rect><rect class="toyplot-Datum" height="55.486212326813316" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="259.60396039603961" y="92.146112936097794"></rect><rect class="toyplot-Datum" height="55.804232768363363" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="269.10891089108912" y="98.364489241377555"></rect><rect class="toyplot-Datum" height="48.518701602429445" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="278.61386138613864" y="102.22474589284511"></rect><rect class="toyplot-Datum" height="70.749596594312607" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="288.11881188118809" y="79.604994287286928"></rect><rect class="toyplot-Datum" height="52.479697730262302" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="297.62376237623761" y="94.106575633698355"></rect><rect class="toyplot-Datum" height="39.121829554293498" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="307.12871287128718" y="113.33657504381463"></rect><rect class="toyplot-Datum" height="56.068273056893744" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="316.63366336633663" y="98.730759159978632"></rect><rect class="toyplot-Datum" height="39.425394179142714" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="326.13861386138615" y="105.79747194739643"></rect><rect class="toyplot-Datum" height="46.945568786855517" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="335.64356435643566" y="103.96588489741592"></rect><rect class="toyplot-Datum" height="29.627985157832398" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="345.14851485148512" y="119.09436669502935"></rect><rect class="toyplot-Datum" height="57.864331402278481" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="354.65346534653463" y="88.926640800581083"></rect><rect class="toyplot-Datum" height="54.166847539875079" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="364.1584158415842" y="99.50358107032713"></rect><rect class="toyplot-Datum" height="49.208665476095348" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="373.66336633663366" y="101.00356938518999"></rect><rect class="toyplot-Datum" height="30.231776182248296" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="383.16831683168317" y="113.77445227469016"></rect><rect class="toyplot-Datum" height="48.279555676755535" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="392.67326732673268" y="106.67514032757668"></rect><rect class="toyplot-Datum" height="54.75428577156427" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="402.17821782178214" y="88.169919424062726"></rect><rect class="toyplot-Datum" height="47.233390427152528" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="411.68316831683171" y="99.172693724686894"></rect><rect class="toyplot-Datum" height="38.45131820995833" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="421.18811881188117" y="105.25288890317496"></rect><rect class="toyplot-Datum" height="54.722293118196887" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="430.69306930693068" y="97.668716665138646"></rect><rect class="toyplot-Datum" height="62.748000019149728" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="440.19801980198025" y="82.705271235721753"></rect><rect class="toyplot-Datum" height="58.205222860642237" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="449.70297029702971" y="91.902710588057033"></rect><rect class="toyplot-Datum" height="56.502306091226671" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="459.20792079207916" y="96.004932394384753"></rect><rect class="toyplot-Datum" height="44.606396179007874" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="468.71287128712873" y="105.77002656466388"></rect><rect class="toyplot-Datum" height="42.010775871180641" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="478.21782178217819" y="102.65555056622318"></rect><rect class="toyplot-Datum" height="49.450802163323601" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="487.7227722772277" y="103.07852204007941"></rect><rect class="toyplot-Datum" height="45.175041999564343" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="497.22772277227727" y="101.29223504365262"></rect><rect class="toyplot-Datum" height="36.941041941335456" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="506.73267326732673" y="103.02982403626312"></rect><rect class="toyplot-Datum" height="58.351713186369579" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="516.23762376237619" y="94.858536066404071"></rect><rect class="toyplot-Datum" height="55.467648405077057" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="525.74257425742564" y="93.543530033032766"></rect></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="60.0" x2="535.2475247524752" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="64.75247524752474" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="159.8019801980198" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="254.85148514851485" y="250.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="349.9009900990099" y="250.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="444.950495049505" y="250.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">50</text></g><line style="" x1="50.0" x2="50.0" y1="73.681015177598" y2="239.5807073453239"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">-4</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 195.0)" x="50.0" y="195.0">-2</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 105.0)" x="50.0" y="105.0">2</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">4</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t1d5d76e053674ba59247f96eb95ff803 text");
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
          var text = document.querySelectorAll("#t1d5d76e053674ba59247f96eb95ff803 text");
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
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5], [0.05827415575052086, 0.019607963385830277, 0.0667585105587835, 0.2689868239986718, 0.022863801855891968, 0.014857847746814493, -0.004991497471993052, -0.2841924983442814, -0.01120928052829014, 0.01613911088747882, 0.17055468919052602, -0.11093449793030938, 0.22069275286721116, -0.3300500810075081, 0.01737261011175662, -0.07869274005686182, -0.11030756850266951, 0.06537394639432609, -0.056943400253946556, 0.023650399985416605, -0.05582893463452801, 0.10522998831506175, -0.18527653376626368, -0.03304211090109119, -0.0157595947377568, 0.1517211838239701, -0.10926242658258428, -0.21329032074988336, 0.2123170610427047, -0.04050905263428535, 0.05678436209503326, 0.14262345765068624, -0.16313016045343154, -0.00943266050157094, 0.266389846358291, -0.2202087113036536, 0.31447976908324493, 0.1597295932515817, 0.27981301719407603, -0.10626710148157884, 0.20207683311682245, -0.004797042164411372, -0.1114328215827292, -0.016729899718744508, 0.23705215833760737, -0.11241440904013367, 0.15700990919035693, 0.4457392898845084, -0.1426777445677188, 0.04394762497289654], [1.3141821522128858, 1.75489802161381, 2.0676713194351204, 2.5497663916574775, 1.5267616207099823, 2.1197886692317067, 1.700750731344615, 2.301151192740128, 2.439948154451741, 2.2947695950263345, 2.239148071099645, 2.905450611635579, 2.1760328159801725, 1.7046945311046178, 2.038879025464805, 3.391954880995644, 2.485519045538639, 2.008434759072007, 1.945233408661104, 2.8891700683134234, 2.282873403210996, 2.5712838695067646, 2.2949115892721093, 2.123344626984662, 3.128666920565025, 2.484152194057851, 1.6294855536082387, 2.278632926223172, 1.9645568023379363, 2.0459606712259597, 1.3735837024431405, 2.7143715199741734, 2.2442852857632385, 2.177619138436001, 1.6100243433471038, 1.92554931877437, 2.748003581152767, 2.2589913900139167, 1.9887604931922236, 2.3258348148827266, 2.9908768339679224, 2.58210175164191, 2.3997807824717885, 1.9657765971260497, 2.1041977526123024, 2.0853990204409154, 2.1647895536154382, 2.0875633761660835, 2.4507317303820413, 2.5091764429763215]], "title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "t9a25838504ed4e28afb000560b51ffd5", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t1d5d76e053674ba59247f96eb95ff803 .toyplot-mark-popup");
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
      var axes = {"tec9635080adf4d6db620e8c9dacbb524": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 4.0, "min": -4.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
      function sign(x)
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
    
      function to_domain(projection, range)
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
              return sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
            }
          }
        }
      }
    
      // Compute mouse coordinates relative to a DOM object, with thanks to d3js.org, where this code originated.
      function d3_mousePoint(container, e)
      {
        if (e.changedTouches) e = e.changedTouches[0];
        var svg = container.ownerSVGElement || container;
        if (svg.createSVGPoint) {
          var point = svg.createSVGPoint();
          point.x = e.clientX, point.y = e.clientY;
          point = point.matrixTransform(container.getScreenCTM().inverse());
          return [point.x, point.y];
        }
        var rect = container.getBoundingClientRect();
        return [e.clientX - rect.left - container.clientLeft, e.clientY - rect.top - container.clientTop];
      };
    
      function display_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var data = axes[dom_axes.id];
    
        point = d3_mousePoint(e.target, e);
        var x = Number(to_domain(data["x"], point[0])).toFixed(2);
        var y = Number(to_domain(data["y"], point[1])).toFixed(2);
    
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
        {
          coordinates[i].style.visibility = "visible";
          coordinates[i].querySelector("text").textContent = "x=" + x + " y=" + y;
        }
      }
    
      function clear_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
          coordinates[i].style.visibility = "hidden";
      }
    
      for(var axes_id in axes)
      {
        var event_target = document.querySelector("#" + axes_id + " .toyplot-coordinate-events");
        event_target.onmousemove = display_coordinates;
        event_target.onmouseout = clear_coordinates;
      }
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

    <div align="center" class="toyplot" id="t1868f5408c1a4da6917044259c6cf149"><svg height="300.0px" id="te824e7f150244be48c00bbaef03e04be" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t15d76fe196144c34aa9187fee73eff56"><clipPath id="t3e029cd182794973a20f2e4624b8bdaa"><rect height="200.0" width="500.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t3e029cd182794973a20f2e4624b8bdaa)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-BarBoundaries" id="tb85e2a3f7d7b4449a98caac707bad86f" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="37.01239808292982" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="60.0" y="148.68883149561327"></rect><rect class="toyplot-Datum" height="58.397092882238468" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="69.504950495049499" y="149.55882082381882"></rect><rect class="toyplot-Datum" height="56.589272688819165" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="79.009900990099013" y="148.49793351242738"></rect><rect class="toyplot-Datum" height="62.997907018735361" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="88.514851485148512" y="143.94779646002988"></rect><rect class="toyplot-Datum" height="74.251275742938304" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="98.019801980198025" y="149.48556445824244"></rect><rect class="toyplot-Datum" height="41.694232186004399" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="155.04950495049508" y="146.16251949321315"></rect><rect class="toyplot-Datum" height="47.304995391609509" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="164.55445544554456" y="152.49602620343194"></rect><rect class="toyplot-Datum" height="76.550701352497811" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="174.05940594059405" y="145.03441306048774"></rect><rect class="toyplot-Datum" height="53.015024814554522" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="183.56435643564359" y="157.42612682266892"></rect><rect class="toyplot-Datum" height="56.712724487267963" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="193.06930693069307" y="149.60911627248547"></rect><rect class="toyplot-Datum" height="65.115015414662082" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="202.57425742574256" y="151.77058665127939"></rect><rect class="toyplot-Datum" height="65.70701520845634" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="212.0792079207921" y="152.48192029131008"></rect><rect class="toyplot-Datum" height="50.089585333048092" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="221.58415841584159" y="148.52908620612766"></rect><rect class="toyplot-Datum" height="40.086734252946201" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="231.08910891089107" y="151.28122650571379"></rect><rect class="toyplot-Datum" height="42.079842172979369" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="240.59405940594058" y="149.46786600032812"></rect><rect class="toyplot-Datum" height="88.324556316047023" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="250.09900990099013" y="151.25615102927688"></rect><rect class="toyplot-Datum" height="59.457400956962658" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="259.60396039603961" y="147.63232526291111"></rect><rect class="toyplot-Datum" height="72.997754078949725" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="269.10891089108912" y="154.16872200974092"></rect><rect class="toyplot-Datum" height="42.332886424554971" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="278.61386138613864" y="150.74344749527455"></rect><rect class="toyplot-Datum" height="56.662172664777842" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="288.11881188118809" y="150.35459088159953"></rect><rect class="toyplot-Datum" height="54.868796081854555" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="297.62376237623761" y="146.58627336396066"></rect><rect class="toyplot-Datum" height="39.78338441942725" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="307.12871287128718" y="152.45840459810813"></rect><rect class="toyplot-Datum" height="34.818763247586503" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="316.63366336633663" y="154.79903221687238"></rect><rect class="toyplot-Datum" height="59.240333772269366" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="326.13861386138615" y="145.22286612653915"></rect><rect class="toyplot-Datum" height="48.975446868622186" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="335.64356435643566" y="150.91145368427144"></rect><rect class="toyplot-Datum" height="44.124403117076355" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="345.14851485148512" y="148.72235185286175"></rect><rect class="toyplot-Datum" height="84.178202431728266" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="354.65346534653463" y="146.79097220285956"></rect><rect class="toyplot-Datum" height="46.20368230346395" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="364.1584158415842" y="153.67042861020221"></rect><rect class="toyplot-Datum" height="54.44185121461436" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="373.66336633663366" y="150.21223486128534"></rect><rect class="toyplot-Datum" height="64.975392520010161" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="383.16831683168317" y="144.00622845693846"></rect><rect class="toyplot-Datum" height="46.15228491913993" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="392.67326732673268" y="154.95469600433222"></rect><rect class="toyplot-Datum" height="46.000659030561252" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="402.17821782178214" y="142.924205195627"></rect><rect class="toyplot-Datum" height="32.370474280589519" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="411.68316831683171" y="146.40608415183942"></rect><rect class="toyplot-Datum" height="66.562675700633065" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="421.18811881188117" y="143.70420711313329"></rect><rect class="toyplot-Datum" height="54.156839032544241" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="430.69306930693068" y="152.39100978333553"></rect><rect class="toyplot-Datum" height="43.573631200466309" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="440.19801980198025" y="145.45327125487148"></rect><rect class="toyplot-Datum" height="46.457148056566297" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="449.70297029702971" y="150.10793344869927"></rect><rect class="toyplot-Datum" height="55.009819483664387" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="459.20792079207916" y="152.50723848561142"></rect><rect class="toyplot-Datum" height="52.218920081053881" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="468.71287128712873" y="150.37642274367175"></rect><rect class="toyplot-Datum" height="49.833258589365045" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="478.21782178217819" y="144.66632643740382"></rect><rect class="toyplot-Datum" height="44.741553968106899" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="487.7227722772277" y="152.52932420340301"></rect><rect class="toyplot-Datum" height="61.995704917520641" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="497.22772277227727" y="146.46727704321697"></rect><rect class="toyplot-Datum" height="56.747589232628059" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="506.73267326732673" y="139.97086597759858"></rect><rect class="toyplot-Datum" height="52.237711991438772" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="516.23762376237619" y="153.21024925277365"></rect><rect class="toyplot-Datum" height="48.126536752629988" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="525.74257425742564" y="149.01117843810982"></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="28.2579299204032" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="60.0" y="120.43090157521007"></rect><rect class="toyplot-Datum" height="39.044026310129539" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="69.504950495049499" y="110.51479451368928"></rect><rect class="toyplot-Datum" height="45.020538199717606" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="79.009900990099013" y="103.47739531270977"></rect><rect class="toyplot-Datum" height="51.317540272323129" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="88.514851485148512" y="92.630256187706749"></rect><rect class="toyplot-Datum" height="33.837700924217046" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="98.019801980198025" y="115.64786353402539"></rect><rect class="toyplot-Datum" height="47.360943483410082" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="107.52475247524754" y="102.30475494228661"></rect><rect class="toyplot-Datum" height="38.379200148373684" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="117.02970297029702" y="111.73310854474616"></rect><rect class="toyplot-Datum" height="58.170233049399201" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="126.53465346534654" y="98.224098163347122"></rect><rect class="toyplot-Datum" height="55.151042287050686" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="136.03960396039605" y="95.101166524835818"></rect><rect class="toyplot-Datum" height="51.269185893124273" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="145.54455445544554" y="98.367684111907465"></rect><rect class="toyplot-Datum" height="46.543351092955177" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="155.04950495049508" y="99.619168400257976"></rect><rect class="toyplot-Datum" height="67.868664965232483" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="164.55445544554456" y="84.627361238199455"></rect><rect class="toyplot-Datum" height="43.995151420041623" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="174.05940594059405" y="101.03926164044611"></rect><rect class="toyplot-Datum" height="45.781753772522819" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="183.56435643564359" y="111.6443730501461"></rect><rect class="toyplot-Datum" height="45.483894345443588" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="193.06930693069307" y="104.12522192704188"></rect><rect class="toyplot-Datum" height="78.089571473681389" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="202.57425742574256" y="73.681015177597999"></rect><rect class="toyplot-Datum" height="58.406098815929468" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="212.0792079207921" y="94.075821475380607"></rect><rect class="toyplot-Datum" height="43.718868285247794" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="221.58415841584159" y="104.81021792087986"></rect><rect class="toyplot-Datum" height="45.048978200588635" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="231.08910891089107" y="106.23224830512515"></rect><rect class="toyplot-Datum" height="64.474192537380134" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="240.59405940594058" y="84.993673462947982"></rect><rect class="toyplot-Datum" height="52.620802601524275" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="250.09900990099013" y="98.635348427752604"></rect><rect class="toyplot-Datum" height="55.486212326813316" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="259.60396039603961" y="92.146112936097794"></rect><rect class="toyplot-Datum" height="55.804232768363363" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="269.10891089108912" y="98.364489241377555"></rect><rect class="toyplot-Datum" height="48.518701602429445" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="278.61386138613864" y="102.22474589284511"></rect><rect class="toyplot-Datum" height="70.749596594312607" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="288.11881188118809" y="79.604994287286928"></rect><rect class="toyplot-Datum" height="52.479697730262302" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="297.62376237623761" y="94.106575633698355"></rect><rect class="toyplot-Datum" height="39.121829554293498" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="307.12871287128718" y="113.33657504381463"></rect><rect class="toyplot-Datum" height="56.068273056893744" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="316.63366336633663" y="98.730759159978632"></rect><rect class="toyplot-Datum" height="39.425394179142714" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="326.13861386138615" y="105.79747194739643"></rect><rect class="toyplot-Datum" height="46.945568786855517" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="335.64356435643566" y="103.96588489741592"></rect><rect class="toyplot-Datum" height="29.627985157832398" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="345.14851485148512" y="119.09436669502935"></rect><rect class="toyplot-Datum" height="57.864331402278481" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="354.65346534653463" y="88.926640800581083"></rect><rect class="toyplot-Datum" height="54.166847539875079" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="364.1584158415842" y="99.50358107032713"></rect><rect class="toyplot-Datum" height="49.208665476095348" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="373.66336633663366" y="101.00356938518999"></rect><rect class="toyplot-Datum" height="30.231776182248296" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="383.16831683168317" y="113.77445227469016"></rect><rect class="toyplot-Datum" height="48.279555676755535" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="392.67326732673268" y="106.67514032757668"></rect><rect class="toyplot-Datum" height="54.75428577156427" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="402.17821782178214" y="88.169919424062726"></rect><rect class="toyplot-Datum" height="47.233390427152528" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="411.68316831683171" y="99.172693724686894"></rect><rect class="toyplot-Datum" height="38.45131820995833" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="421.18811881188117" y="105.25288890317496"></rect><rect class="toyplot-Datum" height="54.722293118196887" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="430.69306930693068" y="97.668716665138646"></rect><rect class="toyplot-Datum" height="49.450802163323601" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="487.7227722772277" y="103.07852204007941"></rect><rect class="toyplot-Datum" height="45.175041999564343" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="497.22772277227727" y="101.29223504365262"></rect><rect class="toyplot-Datum" height="36.941041941335456" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="506.73267326732673" y="103.02982403626312"></rect><rect class="toyplot-Datum" height="58.351713186369579" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="516.23762376237619" y="94.858536066404071"></rect><rect class="toyplot-Datum" height="55.467648405077057" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="525.74257425742564" y="93.543530033032766"></rect></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="60.0" x2="535.2475247524752" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="64.75247524752474" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="159.8019801980198" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="254.85148514851485" y="250.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="349.9009900990099" y="250.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="444.950495049505" y="250.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">50</text></g><line style="" x1="50.0" x2="50.0" y1="73.681015177598" y2="239.5807073453239"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">-4</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 195.0)" x="50.0" y="195.0">-2</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 105.0)" x="50.0" y="105.0">2</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">4</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t1868f5408c1a4da6917044259c6cf149 text");
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
          var text = document.querySelectorAll("#t1868f5408c1a4da6917044259c6cf149 text");
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
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5], [0.05827415575052086, 0.019607963385830277, 0.0667585105587835, 0.2689868239986718, 0.022863801855891968, 0.014857847746814493, -0.004991497471993052, -0.2841924983442814, -0.01120928052829014, 0.01613911088747882, 0.17055468919052602, -0.11093449793030938, 0.22069275286721116, -0.3300500810075081, 0.01737261011175662, -0.07869274005686182, -0.11030756850266951, 0.06537394639432609, -0.056943400253946556, 0.023650399985416605, -0.05582893463452801, 0.10522998831506175, -0.18527653376626368, -0.03304211090109119, -0.0157595947377568, 0.1517211838239701, -0.10926242658258428, -0.21329032074988336, 0.2123170610427047, -0.04050905263428535, 0.05678436209503326, 0.14262345765068624, -0.16313016045343154, -0.00943266050157094, 0.266389846358291, -0.2202087113036536, 0.31447976908324493, 0.1597295932515817, 0.27981301719407603, -0.10626710148157884, 0.20207683311682245, -0.004797042164411372, -0.1114328215827292, -0.016729899718744508, 0.23705215833760737, -0.11241440904013367, 0.15700990919035693, 0.4457392898845084, -0.1426777445677188, 0.04394762497289654], [1.3141821522128858, 1.75489802161381, 2.0676713194351204, 2.5497663916574775, 1.5267616207099823, 2.1197886692317067, 1.700750731344615, 2.301151192740128, 2.439948154451741, 2.2947695950263345, 2.239148071099645, 2.905450611635579, 2.1760328159801725, 1.7046945311046178, 2.038879025464805, 3.391954880995644, 2.485519045538639, 2.008434759072007, 1.945233408661104, 2.8891700683134234, 2.282873403210996, 2.5712838695067646, 2.2949115892721093, 2.123344626984662, 3.128666920565025, 2.484152194057851, 1.6294855536082387, 2.278632926223172, 1.9645568023379363, 2.0459606712259597, 1.3735837024431405, 2.7143715199741734, 2.2442852857632385, 2.177619138436001, 1.6100243433471038, 1.92554931877437, 2.748003581152767, 2.2589913900139167, 1.9887604931922236, 2.3258348148827266, null, null, null, null, null, 2.0853990204409154, 2.1647895536154382, 2.0875633761660835, 2.4507317303820413, 2.5091764429763215]], "title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "tb85e2a3f7d7b4449a98caac707bad86f", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t1868f5408c1a4da6917044259c6cf149 .toyplot-mark-popup");
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
      var axes = {"t15d76fe196144c34aa9187fee73eff56": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 4.0, "min": -4.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
      function sign(x)
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
    
      function to_domain(projection, range)
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
              return sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
            }
          }
        }
      }
    
      // Compute mouse coordinates relative to a DOM object, with thanks to d3js.org, where this code originated.
      function d3_mousePoint(container, e)
      {
        if (e.changedTouches) e = e.changedTouches[0];
        var svg = container.ownerSVGElement || container;
        if (svg.createSVGPoint) {
          var point = svg.createSVGPoint();
          point.x = e.clientX, point.y = e.clientY;
          point = point.matrixTransform(container.getScreenCTM().inverse());
          return [point.x, point.y];
        }
        var rect = container.getBoundingClientRect();
        return [e.clientX - rect.left - container.clientLeft, e.clientY - rect.top - container.clientTop];
      };
    
      function display_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var data = axes[dom_axes.id];
    
        point = d3_mousePoint(e.target, e);
        var x = Number(to_domain(data["x"], point[0])).toFixed(2);
        var y = Number(to_domain(data["y"], point[1])).toFixed(2);
    
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
        {
          coordinates[i].style.visibility = "visible";
          coordinates[i].querySelector("text").textContent = "x=" + x + " y=" + y;
        }
      }
    
      function clear_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
          coordinates[i].style.visibility = "hidden";
      }
    
      for(var axes_id in axes)
      {
        var event_target = document.querySelector("#" + axes_id + " .toyplot-coordinate-events");
        event_target.onmousemove = display_coordinates;
        event_target.onmouseout = clear_coordinates;
      }
    })();
    </script></div></div>


Finally, as you might imagine, null values in the middle boundary affect
both sets of adjacent bars:

.. code:: python

    boundaries[20:30, 1] = numpy.ma.masked
    toyplot.bars(boundaries, baseline=None, width=600, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="t0f2fc3698d514503badd8356b67969df"><svg height="300.0px" id="tf613aeabd585414c8fa41211d0ac50f3" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="te91c0de2df3b461996ca14778bd660dc"><clipPath id="t51c8d298dbbd431da731a23a815ffa56"><rect height="200.0" width="500.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t51c8d298dbbd431da731a23a815ffa56)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-BarBoundaries" id="te8e06f8c564e49c892dcfc211c4203e9" style="stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0"><g class="toyplot-Series"><rect class="toyplot-Datum" height="37.01239808292982" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="60.0" y="148.68883149561327"></rect><rect class="toyplot-Datum" height="58.397092882238468" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="69.504950495049499" y="149.55882082381882"></rect><rect class="toyplot-Datum" height="56.589272688819165" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="79.009900990099013" y="148.49793351242738"></rect><rect class="toyplot-Datum" height="62.997907018735361" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="88.514851485148512" y="143.94779646002988"></rect><rect class="toyplot-Datum" height="74.251275742938304" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="98.019801980198025" y="149.48556445824244"></rect><rect class="toyplot-Datum" height="41.694232186004399" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="155.04950495049508" y="146.16251949321315"></rect><rect class="toyplot-Datum" height="47.304995391609509" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="164.55445544554456" y="152.49602620343194"></rect><rect class="toyplot-Datum" height="76.550701352497811" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="174.05940594059405" y="145.03441306048774"></rect><rect class="toyplot-Datum" height="53.015024814554522" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="183.56435643564359" y="157.42612682266892"></rect><rect class="toyplot-Datum" height="56.712724487267963" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="193.06930693069307" y="149.60911627248547"></rect><rect class="toyplot-Datum" height="65.115015414662082" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="202.57425742574256" y="151.77058665127939"></rect><rect class="toyplot-Datum" height="65.70701520845634" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="212.0792079207921" y="152.48192029131008"></rect><rect class="toyplot-Datum" height="50.089585333048092" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="221.58415841584159" y="148.52908620612766"></rect><rect class="toyplot-Datum" height="40.086734252946201" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="231.08910891089107" y="151.28122650571379"></rect><rect class="toyplot-Datum" height="42.079842172979369" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="240.59405940594058" y="149.46786600032812"></rect><rect class="toyplot-Datum" height="44.124403117076355" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="345.14851485148512" y="148.72235185286175"></rect><rect class="toyplot-Datum" height="84.178202431728266" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="354.65346534653463" y="146.79097220285956"></rect><rect class="toyplot-Datum" height="46.20368230346395" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="364.1584158415842" y="153.67042861020221"></rect><rect class="toyplot-Datum" height="54.44185121461436" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="373.66336633663366" y="150.21223486128534"></rect><rect class="toyplot-Datum" height="64.975392520010161" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="383.16831683168317" y="144.00622845693846"></rect><rect class="toyplot-Datum" height="46.15228491913993" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="392.67326732673268" y="154.95469600433222"></rect><rect class="toyplot-Datum" height="46.000659030561252" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="402.17821782178214" y="142.924205195627"></rect><rect class="toyplot-Datum" height="32.370474280589519" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="411.68316831683171" y="146.40608415183942"></rect><rect class="toyplot-Datum" height="66.562675700633065" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="421.18811881188117" y="143.70420711313329"></rect><rect class="toyplot-Datum" height="54.156839032544241" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="430.69306930693068" y="152.39100978333553"></rect><rect class="toyplot-Datum" height="43.573631200466309" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="440.19801980198025" y="145.45327125487148"></rect><rect class="toyplot-Datum" height="46.457148056566297" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="449.70297029702971" y="150.10793344869927"></rect><rect class="toyplot-Datum" height="55.009819483664387" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="459.20792079207916" y="152.50723848561142"></rect><rect class="toyplot-Datum" height="52.218920081053881" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="468.71287128712873" y="150.37642274367175"></rect><rect class="toyplot-Datum" height="49.833258589365045" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="478.21782178217819" y="144.66632643740382"></rect><rect class="toyplot-Datum" height="44.741553968106899" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="487.7227722772277" y="152.52932420340301"></rect><rect class="toyplot-Datum" height="61.995704917520641" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="497.22772277227727" y="146.46727704321697"></rect><rect class="toyplot-Datum" height="56.747589232628059" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="506.73267326732673" y="139.97086597759858"></rect><rect class="toyplot-Datum" height="52.237711991438772" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="516.23762376237619" y="153.21024925277365"></rect><rect class="toyplot-Datum" height="48.126536752629988" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="525.74257425742564" y="149.01117843810982"></rect></g><g class="toyplot-Series"><rect class="toyplot-Datum" height="28.2579299204032" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="60.0" y="120.43090157521007"></rect><rect class="toyplot-Datum" height="39.044026310129539" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="69.504950495049499" y="110.51479451368928"></rect><rect class="toyplot-Datum" height="45.020538199717606" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494992" x="79.009900990099013" y="103.47739531270977"></rect><rect class="toyplot-Datum" height="51.317540272323129" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="88.514851485148512" y="92.630256187706749"></rect><rect class="toyplot-Datum" height="33.837700924217046" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="98.019801980198025" y="115.64786353402539"></rect><rect class="toyplot-Datum" height="47.360943483410082" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="107.52475247524754" y="102.30475494228661"></rect><rect class="toyplot-Datum" height="38.379200148373684" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="117.02970297029702" y="111.73310854474616"></rect><rect class="toyplot-Datum" height="58.170233049399201" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="126.53465346534654" y="98.224098163347122"></rect><rect class="toyplot-Datum" height="55.151042287050686" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="136.03960396039605" y="95.101166524835818"></rect><rect class="toyplot-Datum" height="51.269185893124273" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="145.54455445544554" y="98.367684111907465"></rect><rect class="toyplot-Datum" height="46.543351092955177" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="155.04950495049508" y="99.619168400257976"></rect><rect class="toyplot-Datum" height="67.868664965232483" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="164.55445544554456" y="84.627361238199455"></rect><rect class="toyplot-Datum" height="43.995151420041623" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="174.05940594059405" y="101.03926164044611"></rect><rect class="toyplot-Datum" height="45.781753772522819" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="183.56435643564359" y="111.6443730501461"></rect><rect class="toyplot-Datum" height="45.483894345443588" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="193.06930693069307" y="104.12522192704188"></rect><rect class="toyplot-Datum" height="78.089571473681389" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="202.57425742574256" y="73.681015177597999"></rect><rect class="toyplot-Datum" height="58.406098815929468" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="212.0792079207921" y="94.075821475380607"></rect><rect class="toyplot-Datum" height="43.718868285247794" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.504950495049485" x="221.58415841584159" y="104.81021792087986"></rect><rect class="toyplot-Datum" height="45.048978200588635" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="231.08910891089107" y="106.23224830512515"></rect><rect class="toyplot-Datum" height="64.474192537380134" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495418" x="240.59405940594058" y="84.993673462947982"></rect><rect class="toyplot-Datum" height="29.627985157832398" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="345.14851485148512" y="119.09436669502935"></rect><rect class="toyplot-Datum" height="57.864331402278481" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="354.65346534653463" y="88.926640800581083"></rect><rect class="toyplot-Datum" height="54.166847539875079" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="364.1584158415842" y="99.50358107032713"></rect><rect class="toyplot-Datum" height="49.208665476095348" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="373.66336633663366" y="101.00356938518999"></rect><rect class="toyplot-Datum" height="30.231776182248296" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="383.16831683168317" y="113.77445227469016"></rect><rect class="toyplot-Datum" height="48.279555676755535" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="392.67326732673268" y="106.67514032757668"></rect><rect class="toyplot-Datum" height="54.75428577156427" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="402.17821782178214" y="88.169919424062726"></rect><rect class="toyplot-Datum" height="47.233390427152528" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="411.68316831683171" y="99.172693724686894"></rect><rect class="toyplot-Datum" height="38.45131820995833" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495134" x="421.18811881188117" y="105.25288890317496"></rect><rect class="toyplot-Datum" height="54.722293118196887" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="430.69306930693068" y="97.668716665138646"></rect><rect class="toyplot-Datum" height="49.450802163323601" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="487.7227722772277" y="103.07852204007941"></rect><rect class="toyplot-Datum" height="45.175041999564343" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="497.22772277227727" y="101.29223504365262"></rect><rect class="toyplot-Datum" height="36.941041941335456" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="506.73267326732673" y="103.02982403626312"></rect><rect class="toyplot-Datum" height="58.351713186369579" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950494565" x="516.23762376237619" y="94.858536066404071"></rect><rect class="toyplot-Datum" height="55.467648405077057" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,100%,100%);stroke-opacity:1.0;stroke-width:1.0" width="9.5049504950495702" x="525.74257425742564" y="93.543530033032766"></rect></g></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="60.0" x2="535.2475247524752" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="64.75247524752474" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="159.8019801980198" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="254.85148514851485" y="250.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="349.9009900990099" y="250.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="444.950495049505" y="250.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">50</text></g><line style="" x1="50.0" x2="50.0" y1="73.681015177598" y2="239.5807073453239"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">-4</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 195.0)" x="50.0" y="195.0">-2</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 105.0)" x="50.0" y="105.0">2</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">4</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t0f2fc3698d514503badd8356b67969df text");
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
          var text = document.querySelectorAll("#t0f2fc3698d514503badd8356b67969df text");
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
      var data_tables = [{"data": [[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5], [0.05827415575052086, 0.019607963385830277, 0.0667585105587835, 0.2689868239986718, 0.022863801855891968, 0.014857847746814493, -0.004991497471993052, -0.2841924983442814, -0.01120928052829014, 0.01613911088747882, 0.17055468919052602, -0.11093449793030938, 0.22069275286721116, -0.3300500810075081, 0.01737261011175662, -0.07869274005686182, -0.11030756850266951, 0.06537394639432609, -0.056943400253946556, 0.023650399985416605, null, null, null, null, null, null, null, null, null, null, 0.05678436209503326, 0.14262345765068624, -0.16313016045343154, -0.00943266050157094, 0.266389846358291, -0.2202087113036536, 0.31447976908324493, 0.1597295932515817, 0.27981301719407603, -0.10626710148157884, 0.20207683311682245, -0.004797042164411372, -0.1114328215827292, -0.016729899718744508, 0.23705215833760737, -0.11241440904013367, 0.15700990919035693, 0.4457392898845084, -0.1426777445677188, 0.04394762497289654], [1.3141821522128858, 1.75489802161381, 2.0676713194351204, 2.5497663916574775, 1.5267616207099823, 2.1197886692317067, 1.700750731344615, 2.301151192740128, 2.439948154451741, 2.2947695950263345, 2.239148071099645, 2.905450611635579, 2.1760328159801725, 1.7046945311046178, 2.038879025464805, 3.391954880995644, 2.485519045538639, 2.008434759072007, 1.945233408661104, 2.8891700683134234, 2.282873403210996, 2.5712838695067646, 2.2949115892721093, 2.123344626984662, 3.128666920565025, 2.484152194057851, 1.6294855536082387, 2.278632926223172, 1.9645568023379363, 2.0459606712259597, 1.3735837024431405, 2.7143715199741734, 2.2442852857632385, 2.177619138436001, 1.6100243433471038, 1.92554931877437, 2.748003581152767, 2.2589913900139167, 1.9887604931922236, 2.3258348148827266, null, null, null, null, null, 2.0853990204409154, 2.1647895536154382, 2.0875633761660835, 2.4507317303820413, 2.5091764429763215]], "title": "Bar Data", "names": ["left", "right", "boundary1", "boundary2"], "id": "te8e06f8c564e49c892dcfc211c4203e9", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t0f2fc3698d514503badd8356b67969df .toyplot-mark-popup");
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
      var axes = {"te91c0de2df3b461996ca14778bd660dc": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": -0.5}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 4.0, "min": -4.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
      function sign(x)
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
    
      function to_domain(projection, range)
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
              return sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
            }
          }
        }
      }
    
      // Compute mouse coordinates relative to a DOM object, with thanks to d3js.org, where this code originated.
      function d3_mousePoint(container, e)
      {
        if (e.changedTouches) e = e.changedTouches[0];
        var svg = container.ownerSVGElement || container;
        if (svg.createSVGPoint) {
          var point = svg.createSVGPoint();
          point.x = e.clientX, point.y = e.clientY;
          point = point.matrixTransform(container.getScreenCTM().inverse());
          return [point.x, point.y];
        }
        var rect = container.getBoundingClientRect();
        return [e.clientX - rect.left - container.clientLeft, e.clientY - rect.top - container.clientTop];
      };
    
      function display_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var data = axes[dom_axes.id];
    
        point = d3_mousePoint(e.target, e);
        var x = Number(to_domain(data["x"], point[0])).toFixed(2);
        var y = Number(to_domain(data["y"], point[1])).toFixed(2);
    
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
        {
          coordinates[i].style.visibility = "visible";
          coordinates[i].querySelector("text").textContent = "x=" + x + " y=" + y;
        }
      }
    
      function clear_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
          coordinates[i].style.visibility = "hidden";
      }
    
      for(var axes_id in axes)
      {
        var event_target = document.querySelector("#" + axes_id + " .toyplot-coordinate-events");
        event_target.onmousemove = display_coordinates;
        event_target.onmouseout = clear_coordinates;
      }
    })();
    </script></div></div>


Of course, these behaviors extended to other plot types too:

.. code:: python

    toyplot.fill(magnitudes, baseline="stacked", width=600, height=300);  



.. raw:: html

    <div align="center" class="toyplot" id="t023eb9e099e8442287a4523fc77c720a"><svg height="300.0px" id="te3770b8d9c724dc28237603d1d0d1fe2" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="t4a8ac8423c0c40bfb4802a3f8ea890fd"><clipPath id="t98bcd6c5d82749afaaf6fae7049a6ab2"><rect height="200.0" width="500.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t98bcd6c5d82749afaaf6fae7049a6ab2)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-FillMagnitudes" id="tf1d5b1201c1c43149c79fa0d77a79803" style="stroke:none"><polygon points="60.0,240.0 69.599999999999994,240.0 79.199999999999989,240.0 88.799999999999997,240.0 98.400000000000006,240.0 98.400000000000006,159.0 88.799999999999997,168.0 79.199999999999989,177.0 69.599999999999994,159.0 60.0,168.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon><polygon points="204.0,240.0 213.60000000000002,240.0 223.20000000000002,240.0 232.80000000000001,240.0 242.39999999999998,240.0 252.0,240.0 261.59999999999997,240.0 271.19999999999999,240.0 280.80000000000001,240.0 290.39999999999998,240.0 300.0,240.0 309.60000000000002,240.0 319.20000000000005,240.0 328.80000000000001,240.0 338.39999999999998,240.0 348.0,240.0 357.60000000000002,240.0 367.20000000000005,240.0 376.80000000000001,240.0 386.40000000000003,240.0 396.0,240.0 405.60000000000002,240.0 415.20000000000005,240.0 424.79999999999995,240.0 434.39999999999998,240.0 444.0,240.0 453.59999999999997,240.0 463.19999999999999,240.0 472.79999999999995,240.0 482.39999999999998,240.0 492.0,240.0 501.60000000000002,240.0 511.19999999999999,240.0 520.79999999999995,240.0 530.40000000000009,240.0 530.40000000000009,159.0 520.79999999999995,186.0 511.19999999999999,186.0 501.60000000000002,177.0 492.0,186.0 482.39999999999998,177.0 472.79999999999995,186.0 463.19999999999999,177.0 453.59999999999997,186.0 444.0,195.0 434.39999999999998,186.0 424.79999999999995,159.0 415.20000000000005,186.0 405.60000000000002,177.0 396.0,168.0 386.40000000000003,186.0 376.80000000000001,177.0 367.20000000000005,159.0 357.60000000000002,159.0 348.0,177.0 338.39999999999998,177.0 328.80000000000001,159.0 319.20000000000005,168.0 309.60000000000002,159.0 300.0,177.0 290.39999999999998,177.0 280.80000000000001,186.0 271.19999999999999,168.0 261.59999999999997,177.0 252.0,159.0 242.39999999999998,195.0 232.80000000000001,159.0 223.20000000000002,195.0 213.60000000000002,195.0 204.0,186.0" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon><polygon points="60.0,168.0 69.599999999999994,159.0 79.199999999999989,177.0 88.799999999999997,168.0 98.400000000000006,159.0 98.400000000000006,78.0 88.799999999999997,123.0 79.199999999999989,95.999999999999986 69.599999999999994,95.999999999999986 60.0,114.00000000000001" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon><polygon points="204.0,186.0 213.60000000000002,195.0 223.20000000000002,195.0 232.80000000000001,159.0 242.39999999999998,195.0 252.0,159.0 261.59999999999997,177.0 271.19999999999999,168.0 280.80000000000001,186.0 290.39999999999998,177.0 300.0,177.0 309.60000000000002,159.0 319.20000000000005,168.0 328.80000000000001,159.0 338.39999999999998,177.0 348.0,177.0 357.60000000000002,159.0 367.20000000000005,159.0 376.80000000000001,177.0 386.40000000000003,186.0 396.0,168.0 405.60000000000002,177.0 415.20000000000005,186.0 424.79999999999995,159.0 434.39999999999998,186.0 444.0,195.0 453.59999999999997,186.0 463.19999999999999,177.0 472.79999999999995,186.0 482.39999999999998,177.0 492.0,186.0 501.60000000000002,177.0 511.19999999999999,186.0 520.79999999999995,186.0 530.40000000000009,159.0 530.40000000000009,78.0 520.79999999999995,114.00000000000001 511.19999999999999,141.0 501.60000000000002,132.0 492.0,132.0 482.39999999999998,95.999999999999986 472.79999999999995,123.0 463.19999999999999,105.0 453.59999999999997,105.0 444.0,132.0 434.39999999999998,123.0 424.79999999999995,105.0 415.20000000000005,132.0 405.60000000000002,132.0 396.0,87.0 386.40000000000003,132.0 376.80000000000001,114.00000000000001 367.20000000000005,87.0 357.60000000000002,95.999999999999986 348.0,114.00000000000001 338.39999999999998,105.0 328.80000000000001,114.00000000000001 319.20000000000005,105.0 309.60000000000002,114.00000000000001 300.0,123.0 290.39999999999998,132.0 280.80000000000001,132.0 271.19999999999999,87.0 261.59999999999997,132.0 252.0,78.0 242.39999999999998,150.0 232.80000000000001,114.00000000000001 223.20000000000002,114.00000000000001 213.60000000000002,123.0 204.0,105.0" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="60.0" x2="530.4000000000001" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="156.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="252.0" y="250.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="348.0" y="250.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="444.0" y="250.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">50</text></g><line style="" x1="50.0" x2="50.0" y1="78.0" y2="240.0"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 195.0)" x="50.0" y="195.0">5</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">10</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 105.0)" x="50.0" y="105.0">15</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">20</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t023eb9e099e8442287a4523fc77c720a text");
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
          var text = document.querySelectorAll("#t023eb9e099e8442287a4523fc77c720a text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [8.0, 9.0, 7.0, 8.0, 9.0, null, null, null, null, null, null, null, null, null, null, 6.0, 5.0, 5.0, 9.0, 5.0, 9.0, 7.0, 8.0, 6.0, 7.0, 7.0, 9.0, 8.0, 9.0, 7.0, 7.0, 9.0, 9.0, 7.0, 6.0, 8.0, 7.0, 6.0, 9.0, 6.0, 5.0, 6.0, 7.0, 6.0, 7.0, 6.0, 7.0, 6.0, 6.0, 9.0], [6.0, 7.0, 9.0, 5.0, 9.0, 6.0, 7.0, 6.0, 6.0, 8.0, 9.0, 6.0, 8.0, 7.0, 5.0, 9.0, 8.0, 9.0, 5.0, 5.0, 9.0, 5.0, 9.0, 6.0, 5.0, 6.0, 5.0, 7.0, 5.0, 8.0, 7.0, 7.0, 8.0, 7.0, 6.0, 9.0, 5.0, 6.0, 6.0, 7.0, 7.0, 9.0, 8.0, 7.0, 9.0, 6.0, 5.0, 5.0, 8.0, 9.0]], "title": "Fill Data", "names": ["x", "y0", "y1"], "id": "tf1d5b1201c1c43149c79fa0d77a79803", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#t023eb9e099e8442287a4523fc77c720a .toyplot-mark-popup");
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
      var axes = {"t4a8ac8423c0c40bfb4802a3f8ea890fd": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 20.0, "min": 0.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
      function sign(x)
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
    
      function to_domain(projection, range)
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
              return sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
            }
          }
        }
      }
    
      // Compute mouse coordinates relative to a DOM object, with thanks to d3js.org, where this code originated.
      function d3_mousePoint(container, e)
      {
        if (e.changedTouches) e = e.changedTouches[0];
        var svg = container.ownerSVGElement || container;
        if (svg.createSVGPoint) {
          var point = svg.createSVGPoint();
          point.x = e.clientX, point.y = e.clientY;
          point = point.matrixTransform(container.getScreenCTM().inverse());
          return [point.x, point.y];
        }
        var rect = container.getBoundingClientRect();
        return [e.clientX - rect.left - container.clientLeft, e.clientY - rect.top - container.clientTop];
      };
    
      function display_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var data = axes[dom_axes.id];
    
        point = d3_mousePoint(e.target, e);
        var x = Number(to_domain(data["x"], point[0])).toFixed(2);
        var y = Number(to_domain(data["y"], point[1])).toFixed(2);
    
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
        {
          coordinates[i].style.visibility = "visible";
          coordinates[i].querySelector("text").textContent = "x=" + x + " y=" + y;
        }
      }
    
      function clear_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
          coordinates[i].style.visibility = "hidden";
      }
    
      for(var axes_id in axes)
      {
        var event_target = document.querySelector("#" + axes_id + " .toyplot-coordinate-events");
        event_target.onmousemove = display_coordinates;
        event_target.onmouseout = clear_coordinates;
      }
    })();
    </script></div></div>


.. code:: python

    toyplot.fill(boundaries, width=600, height=300);



.. raw:: html

    <div align="center" class="toyplot" id="tc5e0013899b940729e089968a2e2514c"><svg height="300.0px" id="t1fbfbd69a1b94db0b502ee30de13854f" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Cartesian" id="tc3c82ad5abe44f5fa2ad8086d8ba0205"><clipPath id="t5ef188137d5c49fb8ef3fa79fc69cec6"><rect height="200.0" width="500.0" x="50.0" y="50.0"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t5ef188137d5c49fb8ef3fa79fc69cec6)" style="cursor:crosshair"><rect height="200.0" style="pointer-events:all;visibility:hidden" width="500.0" x="50.0" y="50.0"></rect><g class="toyplot-mark-FillBoundaries" id="tb340cd5763d14c9c8977a2faef0662f3" style="stroke:none"><polygon points="60.0,185.70122957854309 69.599999999999994,207.95591370605729 79.199999999999989,205.08720620124654 88.799999999999997,206.94570347876524 98.400000000000006,223.73684020118074 98.400000000000006,149.48556445824244 88.799999999999997,143.94779646002988 79.199999999999989,148.49793351242738 69.599999999999994,149.55882082381882 60.0,148.68883149561327" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon><polygon points="156.0,187.85675167921755 165.59999999999999,199.80102159504145 175.19999999999999,221.58511441298555 184.80000000000001,210.44115163722344 194.40000000000001,206.32184075975343 204.0,216.88560206594147 213.60000000000002,218.18893549976642 223.20000000000002,198.61867153917575 232.80000000000001,191.36796075865999 242.39999999999998,191.54770817330748 242.39999999999998,149.46786600032812 232.80000000000001,151.28122650571379 223.20000000000002,148.52908620612766 213.60000000000002,152.48192029131008 204.0,151.77058665127939 194.40000000000001,149.60911627248547 184.80000000000001,157.42612682266892 175.19999999999999,145.03441306048774 165.59999999999999,152.49602620343194 156.0,146.16251949321315" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon><polygon points="348.0,192.8467549699381 357.60000000000002,230.96917463458783 367.20000000000005,199.87411091366616 376.80000000000001,204.6540860758997 386.40000000000003,208.98162097694862 396.0,201.10698092347215 405.60000000000002,188.92486422618825 415.20000000000005,178.77655843242894 424.79999999999995,210.26688281376636 434.39999999999998,206.54784881587977 444.0,189.02690245533779 453.59999999999997,196.56508150526557 463.19999999999999,207.51705796927581 472.79999999999995,202.59534282472563 482.39999999999998,194.49958502676887 492.0,197.27087817150991 501.60000000000002,208.46298196073761 511.19999999999999,196.71845521022664 520.79999999999995,205.44796124421242 530.40000000000009,197.13771519073981 530.40000000000009,149.01117843810982 520.79999999999995,153.21024925277365 511.19999999999999,139.97086597759858 501.60000000000002,146.46727704321697 492.0,152.52932420340301 482.39999999999998,144.66632643740382 472.79999999999995,150.37642274367175 463.19999999999999,152.50723848561142 453.59999999999997,150.10793344869927 444.0,145.45327125487148 434.39999999999998,152.39100978333553 424.79999999999995,143.70420711313329 415.20000000000005,146.40608415183942 405.60000000000002,142.924205195627 396.0,154.95469600433222 386.40000000000003,144.00622845693846 376.80000000000001,150.21223486128534 367.20000000000005,153.67042861020221 357.60000000000002,146.79097220285956 348.0,148.72235185286175" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon><polygon points="60.0,148.68883149561327 69.599999999999994,149.55882082381882 79.199999999999989,148.49793351242738 88.799999999999997,143.94779646002988 98.400000000000006,149.48556445824244 108.0,149.66569842569669 117.59999999999999,150.11230869311984 127.20000000000002,156.39433121274632 136.80000000000001,150.2522088118865 146.40000000000001,149.63687000503174 156.0,146.16251949321315 165.59999999999999,152.49602620343194 175.19999999999999,145.03441306048774 184.80000000000001,157.42612682266892 194.40000000000001,149.60911627248547 204.0,151.77058665127939 213.60000000000002,152.48192029131008 223.20000000000002,148.52908620612766 232.80000000000001,151.28122650571379 242.39999999999998,149.46786600032812 242.39999999999998,84.993673462947982 232.80000000000001,106.23224830512515 223.20000000000002,104.81021792087986 213.60000000000002,94.075821475380607 204.0,73.681015177597999 194.40000000000001,104.12522192704188 184.80000000000001,111.6443730501461 175.19999999999999,101.03926164044611 165.59999999999999,84.627361238199455 156.0,99.619168400257976 146.40000000000001,98.367684111907465 136.80000000000001,95.101166524835818 127.20000000000002,98.224098163347122 117.59999999999999,111.73310854474616 108.0,102.30475494228661 98.400000000000006,115.64786353402539 88.799999999999997,92.630256187706749 79.199999999999989,103.47739531270977 69.599999999999994,110.51479451368928 60.0,120.43090157521007" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon><polygon points="348.0,148.72235185286175 357.60000000000002,146.79097220285956 367.20000000000005,153.67042861020221 376.80000000000001,150.21223486128534 386.40000000000003,144.00622845693846 396.0,154.95469600433222 405.60000000000002,142.924205195627 415.20000000000005,146.40608415183942 424.79999999999995,143.70420711313329 434.39999999999998,152.39100978333553 434.39999999999998,97.668716665138646 424.79999999999995,105.25288890317496 415.20000000000005,99.172693724686894 405.60000000000002,88.169919424062726 396.0,106.67514032757668 386.40000000000003,113.77445227469016 376.80000000000001,101.00356938518999 367.20000000000005,99.50358107032713 357.60000000000002,88.926640800581083 348.0,119.09436669502935" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon><polygon points="492.0,152.52932420340301 501.60000000000002,146.46727704321697 511.19999999999999,139.97086597759858 520.79999999999995,153.21024925277365 530.40000000000009,149.01117843810982 530.40000000000009,93.543530033032766 520.79999999999995,94.858536066404071 511.19999999999999,103.02982403626312 501.60000000000002,101.29223504365262 492.0,103.07852204007941" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:none"></polygon></g></g><g class="toyplot-coordinates" style="visibility:hidden"><rect height="14.0" style="fill:rgb(100%,100%,100%);fill-opacity:1.0;opacity:0.75;stroke:none" width="90.0" x="450.0" y="60.0"></rect><text style="alignment-baseline:middle;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="495.0" y="67.0"></text></g><line style="" x1="60.0" x2="530.4000000000001" y1="250.0" y2="250.0"></line><g><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="60.0" y="250.0">0</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="156.0" y="250.0">10</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="252.0" y="250.0">20</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="348.0" y="250.0">30</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="444.0" y="250.0">40</text><text style="alignment-baseline:middle;baseline-shift:-80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="540.0" y="250.0">50</text></g><line style="" x1="50.0" x2="50.0" y1="73.681015177598" y2="239.5807073453239"></line><g><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 240.0)" x="50.0" y="240.0">-4</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 195.0)" x="50.0" y="195.0">-2</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 150.0)" x="50.0" y="150.0">0</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 105.0)" x="50.0" y="105.0">2</text><text style="alignment-baseline:middle;baseline-shift:80%;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" transform="rotate(-90, 50.0, 60.0)" x="50.0" y="60.0">4</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#tc5e0013899b940729e089968a2e2514c text");
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
          var text = document.querySelectorAll("#tc5e0013899b940729e089968a2e2514c text");
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
      var data_tables = [{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [-1.5867213146019146, -2.5758183869358797, -2.448320275610957, -2.5309201546117883, -3.2771928978302536, null, null, null, null, null, -1.682522296854114, -2.213378737557397, -3.1815606405771346, -2.6862734060988207, -2.5031929226557064, -2.972693425152954, -3.030619355545173, -2.1608298461855897, -1.8385760337182218, -1.846564807702554, -3.9813647709032844, -2.5373211653277234, -3.429621159497361, -1.914503729770202, -2.534078379838995, -2.286891975369565, -1.8774128452237937, -1.7607909095315055, -2.4205866621692667, -2.2171955801286054, -1.904300220886139, -3.598629983759458, -2.2166271517184963, -2.4290704922622086, -2.621405376753271, -2.2714213743765406, -1.729993965608367, -1.2789581525523985, -2.678528125056284, -2.513237725150213, -1.734528998015013, -2.069559178011802, -2.556313687523369, -2.337570792210029, -1.977759334523061, -2.100927918733774, -2.5983547538105602, -2.076375787121184, -2.4643538330761063, -2.0950095640328796], [0.05827415575052086, 0.019607963385830277, 0.0667585105587835, 0.2689868239986718, 0.022863801855891968, 0.014857847746814493, -0.004991497471993052, -0.2841924983442814, -0.01120928052829014, 0.01613911088747882, 0.17055468919052602, -0.11093449793030938, 0.22069275286721116, -0.3300500810075081, 0.01737261011175662, -0.07869274005686182, -0.11030756850266951, 0.06537394639432609, -0.056943400253946556, 0.023650399985416605, null, null, null, null, null, null, null, null, null, null, 0.05678436209503326, 0.14262345765068624, -0.16313016045343154, -0.00943266050157094, 0.266389846358291, -0.2202087113036536, 0.31447976908324493, 0.1597295932515817, 0.27981301719407603, -0.10626710148157884, 0.20207683311682245, -0.004797042164411372, -0.1114328215827292, -0.016729899718744508, 0.23705215833760737, -0.11241440904013367, 0.15700990919035693, 0.4457392898845084, -0.1426777445677188, 0.04394762497289654], [1.3141821522128858, 1.75489802161381, 2.0676713194351204, 2.5497663916574775, 1.5267616207099823, 2.1197886692317067, 1.700750731344615, 2.301151192740128, 2.439948154451741, 2.2947695950263345, 2.239148071099645, 2.905450611635579, 2.1760328159801725, 1.7046945311046178, 2.038879025464805, 3.391954880995644, 2.485519045538639, 2.008434759072007, 1.945233408661104, 2.8891700683134234, 2.282873403210996, 2.5712838695067646, 2.2949115892721093, 2.123344626984662, 3.128666920565025, 2.484152194057851, 1.6294855536082387, 2.278632926223172, 1.9645568023379363, 2.0459606712259597, 1.3735837024431405, 2.7143715199741734, 2.2442852857632385, 2.177619138436001, 1.6100243433471038, 1.92554931877437, 2.748003581152767, 2.2589913900139167, 1.9887604931922236, 2.3258348148827266, null, null, null, null, null, 2.0853990204409154, 2.1647895536154382, 2.0875633761660835, 2.4507317303820413, 2.5091764429763215]], "title": "Fill Data", "names": ["x", "y0", "y1", "y2"], "id": "tb340cd5763d14c9c8977a2faef0662f3", "filename": "toyplot"}];
    
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
          var popup = document.querySelector("#tc5e0013899b940729e089968a2e2514c .toyplot-mark-popup");
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
      var axes = {"tc3c82ad5abe44f5fa2ad8086d8ba0205": {"x": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 60.0}, "scale": "linear"}], "y": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 4.0, "min": -4.0}, "range": {"bounds": {"max": -Infinity, "min": Infinity}, "max": 60.0, "min": 240.0}, "scale": "linear"}]}};
    
      function sign(x)
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
    
      function to_domain(projection, range)
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
              return sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
            }
          }
        }
      }
    
      // Compute mouse coordinates relative to a DOM object, with thanks to d3js.org, where this code originated.
      function d3_mousePoint(container, e)
      {
        if (e.changedTouches) e = e.changedTouches[0];
        var svg = container.ownerSVGElement || container;
        if (svg.createSVGPoint) {
          var point = svg.createSVGPoint();
          point.x = e.clientX, point.y = e.clientY;
          point = point.matrixTransform(container.getScreenCTM().inverse());
          return [point.x, point.y];
        }
        var rect = container.getBoundingClientRect();
        return [e.clientX - rect.left - container.clientLeft, e.clientY - rect.top - container.clientTop];
      };
    
      function display_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var data = axes[dom_axes.id];
    
        point = d3_mousePoint(e.target, e);
        var x = Number(to_domain(data["x"], point[0])).toFixed(2);
        var y = Number(to_domain(data["y"], point[1])).toFixed(2);
    
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
        {
          coordinates[i].style.visibility = "visible";
          coordinates[i].querySelector("text").textContent = "x=" + x + " y=" + y;
        }
      }
    
      function clear_coordinates(e)
      {
        var dom_axes = e.currentTarget.parentElement;
        var coordinates = dom_axes.querySelectorAll(".toyplot-coordinates");
        for(var i = 0; i != coordinates.length; ++i)
          coordinates[i].style.visibility = "hidden";
      }
    
      for(var axes_id in axes)
      {
        var event_target = document.querySelector("#" + axes_id + " .toyplot-coordinate-events");
        event_target.onmousemove = display_coordinates;
        event_target.onmouseout = clear_coordinates;
      }
    })();
    </script></div></div>


Finally, a special-case worth mentioning is Toyplot table
visualizations, which will make an explicit distinction between null and
NaN values:

.. code:: python

    data = toyplot.data.Table()
    data["a"] = numpy.random.random(11)
    data["b"] = numpy.random.random(11)
    data["a"][3] = numpy.ma.masked
    data["b"][7] = numpy.nan
    toyplot.table(data, width=300, height=350);



.. raw:: html

    <div align="center" class="toyplot" id="t58575ee7f15546ee86b8a454887d0589"><svg height="350.0px" id="t21df44160b9648d0aeb05ccebacea9f5" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 350.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Table" id="t58b7e5f6edf94449989daeb8d3d92163"><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="rotate(0,100.0,60.416666666666664)" x="100.0" y="60.416666666666664">a</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="rotate(0,200.0,60.416666666666664)" x="200.0" y="60.416666666666664">b</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="81.25">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="81.25">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="81.25">854699</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="81.25">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="81.25">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="81.25">703196</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="102.08333333333331">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="102.08333333333331">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="102.08333333333331">652144</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="102.08333333333331">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="102.08333333333331">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="102.08333333333331">282864</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="122.91666666666666">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="122.91666666666666">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="122.91666666666666">351356</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="122.91666666666666">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="122.91666666666666">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="122.91666666666666">267843</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="143.75">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="143.75">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="143.75">290331</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="164.58333333333331">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="164.58333333333331">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="164.58333333333331">525642</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="164.58333333333331">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="164.58333333333331">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="164.58333333333331">252136</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="185.41666666666669">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="185.41666666666669">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="185.41666666666669">688357</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="185.41666666666669">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="185.41666666666669">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="185.41666666666669">554338</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="206.25">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="206.25">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="206.25">00359724</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="206.25">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="206.25">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="206.25">24377</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="227.08333333333337">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="227.08333333333337">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="227.08333333333337">464203</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="227.08333333333337">nan</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="227.08333333333337"></text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="227.08333333333337"></text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="247.91666666666669">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="247.91666666666669">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="247.91666666666669">36197</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="247.91666666666669">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="247.91666666666669">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="247.91666666666669">437727</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="268.75">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="268.75">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="268.75">768892</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="268.75">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="268.75">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="268.75">629987</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="289.58333333333337">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="289.58333333333337">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="289.58333333333337">64803</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="289.58333333333337">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="289.58333333333337">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="289.58333333333337">0805395</text><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.0" y1="70.833333333333329" y2="70.833333333333329"></line></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t58575ee7f15546ee86b8a454887d0589 text");
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
          var text = document.querySelectorAll("#t58575ee7f15546ee86b8a454887d0589 text");
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


Note that in this case the table explicitly displays the NaN value,
since there is no ambiguity about the fact that it is unlike the other
floating-point values. If you prefer, you can modify your data to mask
it explicitly:

.. code:: python

    data["b"] = numpy.ma.masked_invalid(data["b"])
    toyplot.table(data, width=300, height=350);



.. raw:: html

    <div align="center" class="toyplot" id="t7a96895bcdc4428386a2c4a1e428ba60"><svg height="350.0px" id="tda49c527b91249b4bcdc198a59b1dc18" preserveAspectRatio="xMidyMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 350.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-axes-Table" id="t1ea51c14afdf43b0b2672607c62fc988"><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="rotate(0,100.0,60.416666666666664)" x="100.0" y="60.416666666666664">a</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;font-weight:bold;stroke:none;text-anchor:middle" transform="rotate(0,200.0,60.416666666666664)" x="200.0" y="60.416666666666664">b</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="81.25">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="81.25">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="81.25">854699</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="81.25">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="81.25">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="81.25">703196</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="102.08333333333331">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="102.08333333333331">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="102.08333333333331">652144</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="102.08333333333331">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="102.08333333333331">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="102.08333333333331">282864</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="122.91666666666666">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="122.91666666666666">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="122.91666666666666">351356</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="122.91666666666666">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="122.91666666666666">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="122.91666666666666">267843</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="143.75">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="143.75">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="143.75">290331</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="164.58333333333331">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="164.58333333333331">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="164.58333333333331">525642</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="164.58333333333331">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="164.58333333333331">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="164.58333333333331">252136</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="185.41666666666669">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="185.41666666666669">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="185.41666666666669">688357</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="185.41666666666669">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="185.41666666666669">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="185.41666666666669">554338</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="206.25">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="206.25">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="206.25">00359724</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="206.25">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="206.25">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="206.25">24377</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="227.08333333333337">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="227.08333333333337">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="227.08333333333337">464203</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="247.91666666666669">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="247.91666666666669">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="247.91666666666669">36197</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="247.91666666666669">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="247.91666666666669">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="247.91666666666669">437727</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="268.75">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="268.75">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="268.75">768892</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="268.75">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="268.75">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="268.75">629987</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="98.0" y="289.58333333333337">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="100.0" y="289.58333333333337">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="102.0" y="289.58333333333337">64803</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:end" x="198.0" y="289.58333333333337">0</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:middle" x="200.0" y="289.58333333333337">.</text><text style="alignment-baseline:middle;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-size:12px;stroke:none;text-anchor:begin" x="202.0" y="289.58333333333337">0805395</text><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.0" y1="70.833333333333329" y2="70.833333333333329"></line></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
    (function()
    {
      if(window.CSS !== undefined && window.CSS.supports !== undefined)
      {
        if(!window.CSS.supports("alignment-baseline", "middle"))
        {
          var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
          var text = document.querySelectorAll("#t7a96895bcdc4428386a2c4a1e428ba60 text");
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
          var text = document.querySelectorAll("#t7a96895bcdc4428386a2c4a1e428ba60 text");
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


