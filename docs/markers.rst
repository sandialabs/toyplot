
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
Markers
=======

In Toyplot, markers are used to show the individual datums in
scatterplots:

.. code:: python

    import numpy
    numpy.random.seed(1234)
    x = numpy.random.normal(size=100)
    y = numpy.random.normal(size=100)
.. code:: python

    import toyplot
    toyplot.scatterplot(x, y, width=300);


.. raw:: html

    <div align="center" class="toyplot" id="tae49d9d52f6b49a7af4c4ca0b392da6e"><svg height="300px" id="t53ea2ff61926471e97c7818893f5f7db" style="opacity:1.0;font-size:12px;font-family:helvetica;stroke-opacity:1.0;fill-opacity:1.0;stroke:#343434;stroke-width:1.0;background-color:transparent;fill:#343434;" width="300px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-Axes2D" id="ta24fc82ea6e1414a9165ef08d0993030"><toyplot:axes>{"y": [{"range": {"max": 240, "min": 60}, "scale": "linear", "domain": {"max": 2.3657686288400388, "min": -2.1478550376436099}}], "x": [{"range": {"max": 240, "min": 60}, "scale": "linear", "domain": {"max": 2.3909605154630329, "min": -4.0}}]}</toyplot:axes><clipPath id="tef3c394788c840b09fa5081d8681a7a5"><rect height="200" width="200" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tef3c394788c840b09fa5081d8681a7a5)" style="cursor:crosshair;"><rect height="200" style="pointer-events:all;visibility:hidden;" width="200" x="50" y="50"></rect><g class="toyplot-PlotMark" id="te976c55e9eb8439d86f8d78564150a63" style="stroke:none;fill:none;"><toyplot:data-table title="Plot Data">{"data": [[0.47143516373249306, -1.1909756947064645, 1.4327069684260973, -0.3126518960917129, -0.7205887333650116, 0.8871629403077386, 0.8595884137174165, -0.6365235044173491, 0.015696372114428918, -2.2426849541854055, 1.150035724719818, 0.9919460223426778, 0.9533241281124304, -2.0212548201949705, -0.334077365808097, 0.002118364683486495, 0.405453411570191, 0.2890919409800353, 1.3211581921293856, -1.5469055532292402, -0.2026463246291819, -0.6559693441389339, 0.19342137647035826, 0.5534389109567419, 1.3181515541801367, -0.4693052847058996, 0.6755540851223808, -1.8170272265901968, -0.1831085401789987, 1.0589691875711504, -0.3978402281999914, 0.3374376536139724, 1.0475785728927218, 1.0459382556276653, 0.8637172916848387, -0.12209157484767426, 0.12471295376821585, -0.32279480560829565, 0.8416747129961416, 2.390960515463033, 0.07619958783723642, -0.5664459304649568, 0.036141936684072715, -2.0749776006900293, 0.24779219974854666, -0.8971567844396987, -0.1367948332613474, 0.018289191349219306, 0.7554139823981354, 0.2152685809694434, 0.841008794931391, -1.4458100770443063, -1.4019732815008439, -0.10091819994891389, -0.5482424491868549, -0.14461950836938436, 0.3540203321992379, -0.0355130252781402, 0.5657383060625951, 1.5456588046255575, -0.9742363337673154, -0.07034487710410242, 0.30796885521603423, -0.20849876310587975, 1.0338007325554992, -2.4004536338122957, 2.0306036208387996, -1.1426312890227635, 0.21188338677770105, 0.7047206243171088, -0.785435211763197, 0.4620597371620487, 0.7042282254621743, 0.5235079678938094, -0.9262543135302259, 2.0078429507780005, 0.2269625418708953, -1.1526591092509524, 0.6319794458091295, 0.0395126866933667, 0.46439232505089606, -3.5635166606247353, 1.3211056154702059, 0.15263055220453448, 0.16452954293239852, -0.4300956908764876, 0.7673687357524115, 0.9849198419098969, 0.270835848826804, 1.3919861934464073, 0.07984231300862901, -0.3999645806965225, -1.0278505586819058, -0.5847182112607883, 0.8165939265478418, -0.08194705182666534, -0.3447660142546443, 0.5282881452973941, -1.0689887834801322, -0.5118813091268151], [0.2912053597430635, 0.5665336963535724, 0.503591759111203, 0.2852956847818571, 0.48428811274975, 1.3634815124261457, -0.781105283625392, -0.4680176663374855, 1.2245743551261743, -1.2811082751440426, 0.8754755042743244, -1.710715324029529, -0.4507651031362744, 0.7491638059190651, -0.20393286610125122, -0.18217541166573417, 0.6806560043814565, -1.8184989903916142, 0.047071635325711084, 0.3948442093272043, -0.24843205438084665, -0.6177066479970167, -0.682883996449334, 0.4362576043409168, -1.703012774113238, 0.3937105991386652, -0.47932400357549726, -0.2990162929660804, 0.6941032876787643, 0.6786296737098565, 0.2395559950038969, 0.15122662929444983, 0.8161272333600409, 1.8935344675962007, 0.6396327631937027, -0.9620288319051914, -2.0852656421201097, 1.9302467674655757, -1.7353488744703927, 1.2103837049045143, 0.7974354194278735, -0.379810784047379, 0.7025622240016004, -0.850346271655115, 1.1768124501049289, -0.524336102632456, 0.7009077309156047, 0.9841880707224154, -0.12172840866682022, 2.365768628840039, 0.4961429262475947, 0.7965948666649523, -0.4740208901256851, -0.05669571649092953, 1.3577972581070583, -0.8048337241667037, -2.12362024909293, -0.33350244043324745, -0.886719352485378, 0.33419793089900884, 0.5367838249027502, -0.7438303679362013, -0.3202038822408791, -0.9161988612665409, -0.8596682999817407, 0.22598548673375538, 0.6287758265382943, 0.18649434877307466, 0.9524783451091219, 0.9881375825933089, -0.07260831396267549, -0.5506029235634193, -0.9381526140931042, -1.2390715625947926, 0.13968327403129469, -0.22301898188247601, 2.123691888593553, 0.12227343425882888, -1.4094317399227687, 1.4229859527722433, -2.14785503764361, -1.347532513457755, 0.3635645568066484, -0.014752111804594866, 1.2723950785462097, -1.4495666088633876, -1.1955237416669708, -0.591862973147249, -0.4145048435321895, -1.4257947334380214, 0.2093947875359238, -0.5928860038389254, -1.4731164134656474, -0.896580615301871, 1.1043515698603126, -0.43154951551604476, -0.16113690824405888, 0.8891574940728737, 0.2883768477152654, -1.0515389375700381]], "names": ["position", "series0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="185.936989835" cy="142.732060985" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="139.115552933" cy="131.75216894" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="213.0109992" cy="134.262247214" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="163.853349915" cy="142.967734486" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="152.363898442" cy="135.032062467" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="197.645871403" cy="99.970474786" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="196.869240915" cy="185.495022647" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="154.731577161" cy="173.009318194" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="173.101206811" cy="105.509990298" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="109.494392507" cy="205.434775077" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="205.049625672" cy="119.431796322" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="200.597063907" cy="222.567188967" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="199.509286734" cy="172.321298632" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="115.730923623" cy="124.469014173" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="163.249906263" cy="162.477810129" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="172.718785212" cy="161.610138811" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="184.078628269" cy="127.201055031" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="180.801332993" cy="226.865522497" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="209.869252402" cy="152.467934784" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="129.0908666" cy="138.599019707" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="166.951632687" cy="164.252405107" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="154.183889354" cy="178.97880495" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="178.106792545" cy="181.578029783" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="188.246607374" cy="136.947483901" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="209.784571104" cy="222.260016928" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="159.441241612" cy="138.64422725" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="191.685954449" cy="173.460206627" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="121.482948966" cy="166.269667426" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="167.501910097" cy="126.66478724" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="202.484756643" cy="127.281863612" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="161.454039241" cy="144.791799753" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="182.162979377" cy="148.314310047" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="202.163942481" cy="121.79856182" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="202.117743306" cy="78.832351854" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="196.985529857" cy="128.83703179" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="169.220439532" cy="192.710121001" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="176.171634902" cy="237.503980831" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="163.567677095" cy="77.3682922725" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="196.364705467" cy="223.549556884" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="240.0" cy="106.075903016" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="174.8052666" cy="122.543977645" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="156.705296648" cy="169.491692449" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="173.677051649" cy="126.327451066" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="114.217833303" cy="188.256302444" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="179.638134848" cy="107.414700025" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="147.390898043" cy="175.25525611" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="168.806325486" cy="126.393431037" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="173.174232996" cy="115.096418939" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="193.935190925" cy="159.199556683" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="178.722114264" cy="60.0" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="196.34595003" cy="134.559301203" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="131.938198495" cy="122.577498272" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="133.172852218" cy="173.248722354" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="169.816782988" cy="156.606100636" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="157.217993703" cy="100.197158677" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="168.585945229" cy="186.441295445" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="182.630026879" cy="239.033534415" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="171.658905375" cy="167.644949684" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="188.593017138" cy="189.70683422" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="216.192262872" cy="141.017548792" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="145.219969456" cy="132.938571984" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="170.677873914" cy="184.008526359" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="181.332997139" cy="167.114612941" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="166.786800042" cy="190.8824554" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="201.775892633" cy="188.628058094" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="105.050872278" cy="145.332981666" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="229.850627167" cy="129.269998457" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="140.477162507" cy="146.907859272" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="178.626771013" cy="116.36097953" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="192.507423622" cy="114.938915303" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="150.537511612" cy="157.240683348" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="185.672933004" cy="176.302757656" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="192.493555317" cy="191.757954954" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="187.403608933" cy="203.758381824" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="146.571372523" cy="148.774650585" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="229.209577891" cy="163.238950423" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="179.051472106" cy="69.65384278" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="140.194731151" cy="149.468942221" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="190.458684298" cy="210.552220696" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="173.771988083" cy="97.5974813657" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="185.73862983" cy="240.0" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="72.2934574384" cy="208.083724963" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="209.867771592" cy="139.846429299" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="176.957927934" cy="154.933420457" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="177.293060396" cy="103.602934935" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="160.545571215" cy="212.152769821" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="194.271893929" cy="202.021726679" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="200.399173078" cy="177.948178159" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="180.287154165" cy="170.875266085" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="211.864107511" cy="211.204764872" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="174.907863155" cy="145.994606577" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="161.394207319" cy="177.988975872" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="143.70993658" cy="213.091918749" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="156.190661871" cy="190.100094145" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="195.658310622" cy="110.304386762" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="170.35110121" cy="171.554995097" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="162.948862826" cy="160.771138731" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="187.538241581" cy="118.886168608" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="142.551287509" cy="142.844859969" r="2.2360679775"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="158.242097231" cy="196.279718338" r="2.2360679775"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden;"><rect height="14" style="opacity:0.75;stroke:none;fill:white;" width="90" x="150" y="60"></rect><text style="font-size:10px;font-weight:normal;stroke:none;text-anchor:middle;alignment-baseline:middle;" x="195.0" y="67.0"></text></g><line style="" x1="72.2934574384" x2="240.0" y1="250" y2="250"></line><g><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="60.0" y="250">-4</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="116.329560968" y="250">-2</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="172.659121936" y="250">0</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="228.988682904" y="250">2</text></g><line style="" x1="50" x2="50" y1="60.0" y2="240.0"></line><g><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 234.103649586)" x="50" y="234.103649586">-2</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 194.224383324)" x="50" y="194.224383324">-1</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 154.345117063)" x="50" y="154.345117063">0</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 114.465850801)" x="50" y="114.465850801">1</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 74.5865845396)" x="50" y="74.5865845396">2</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="border-radius:6px;padding:5px;color:white;border:0;list-style:none;visibility:hidden;cursor:default;background:rgba(0%,0%,0%,0.75);position:fixed;margin:0;"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#tae49d9d52f6b49a7af4c4ca0b392da6e text");
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
              var text = document.querySelectorAll("#tae49d9d52f6b49a7af4c4ca0b392da6e text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="tae49d9d52f6b49a7af4c4ca0b392da6e";
    
          function save_csv(dataset)
          {
            uri = "data:text/csv;charset=utf-8,";
            data = JSON.parse(dataset.textContent);
            uri += data.names.join(",") + "\n";
            for(var i = 0; i != data.data[0].length; ++i)
            {
              for(var j = 0; j != data.data.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data.data[j][i];
              }
              uri += "\n";
            }
    
            uri = encodeURI(uri);
            window.open(uri);
          }
    
          function open_popup(dataset)
          {
            return function(e)
            {
              var popup = document.querySelector("#" + root_id + " .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }
    
          }
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="tae49d9d52f6b49a7af4c4ca0b392da6e";
    
          function sign(x)
          {
            if(x < 0)
              return -1;
            if(x > 0)
              return 1;
            return 0;
          }
    
          function log_n(x, base)
          {
            return Math.log(x) / Math.log(base);
          }
    
          function mix(a, b, amount)
          {
            return ((1.0 - amount) * a) + (amount * b);
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
            var x = null;
            var y = null;
    
            var axes = e.currentTarget.parentElement;
            var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
            point = d3_mousePoint(e.target, e);
    
            for(var i = 0; i != data["x"].length; ++i)
            {
              var segment = data["x"][i];
              if(segment.range.min <= point[0] && point[0] < segment.range.max)
              {
                var normalized = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  x = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            for(var i = 0; i != data["y"].length; ++i)
            {
              var segment = data["y"][i];
              if(segment.range.min <= point[1] && point[1] < segment.range.max)
              {
                var normalized = (segment.range.max - point[1]) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  y = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            if(x !== null && y !== null)
              text = "x=" + x + " y=" + y;
            else if(x !== null)
              text = "x=" + x;
            else if(y !== null)
              text = "y=" + y;
            else
              text = null;
    
            if(text !== null)
            {
              var coordinates = axes.querySelectorAll(".toyplot-coordinates");
              for(var i = 0; i != coordinates.length; ++i)
              {
                coordinates[i].style.visibility = "visible";
                coordinates[i].querySelector("text").textContent = text;
              }
            }
          }
    
          function clear_coordinates(e)
          {
            var axes = e.currentTarget.parentElement;
            var coordinates = axes.querySelectorAll(".toyplot-coordinates");
            for(var i = 0; i != coordinates.length; ++i)
              coordinates[i].style.visibility = "hidden";
          }
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-Axes2D .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
          }
        })();
        </script></div></div>


By default, the markers are small circles, but there are many
alternatives:

.. code:: python

    toyplot.scatterplot(x, y, marker="^", size=40, width=300);


.. raw:: html

    <div align="center" class="toyplot" id="t98a947c55b63430ba8c0429c4b676eb0"><svg height="300px" id="tccbe7ca29d8f4e10b60e5c0ea360070b" style="opacity:1.0;font-size:12px;font-family:helvetica;stroke-opacity:1.0;fill-opacity:1.0;stroke:#343434;stroke-width:1.0;background-color:transparent;fill:#343434;" width="300px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-Axes2D" id="tbb9a96b1e9d14fdd8a3cdb7b33997d65"><toyplot:axes>{"y": [{"range": {"max": 240, "min": 60}, "scale": "linear", "domain": {"max": 2.3657686288400388, "min": -2.1478550376436099}}], "x": [{"range": {"max": 240, "min": 60}, "scale": "linear", "domain": {"max": 2.3909605154630329, "min": -4.0}}]}</toyplot:axes><clipPath id="tb404d46d9009459daa4e018027797b10"><rect height="200" width="200" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tb404d46d9009459daa4e018027797b10)" style="cursor:crosshair;"><rect height="200" style="pointer-events:all;visibility:hidden;" width="200" x="50" y="50"></rect><g class="toyplot-PlotMark" id="td7cbe353e7884b0aad2ef7a47c2662f4" style="stroke:none;fill:none;"><toyplot:data-table title="Plot Data">{"data": [[0.47143516373249306, -1.1909756947064645, 1.4327069684260973, -0.3126518960917129, -0.7205887333650116, 0.8871629403077386, 0.8595884137174165, -0.6365235044173491, 0.015696372114428918, -2.2426849541854055, 1.150035724719818, 0.9919460223426778, 0.9533241281124304, -2.0212548201949705, -0.334077365808097, 0.002118364683486495, 0.405453411570191, 0.2890919409800353, 1.3211581921293856, -1.5469055532292402, -0.2026463246291819, -0.6559693441389339, 0.19342137647035826, 0.5534389109567419, 1.3181515541801367, -0.4693052847058996, 0.6755540851223808, -1.8170272265901968, -0.1831085401789987, 1.0589691875711504, -0.3978402281999914, 0.3374376536139724, 1.0475785728927218, 1.0459382556276653, 0.8637172916848387, -0.12209157484767426, 0.12471295376821585, -0.32279480560829565, 0.8416747129961416, 2.390960515463033, 0.07619958783723642, -0.5664459304649568, 0.036141936684072715, -2.0749776006900293, 0.24779219974854666, -0.8971567844396987, -0.1367948332613474, 0.018289191349219306, 0.7554139823981354, 0.2152685809694434, 0.841008794931391, -1.4458100770443063, -1.4019732815008439, -0.10091819994891389, -0.5482424491868549, -0.14461950836938436, 0.3540203321992379, -0.0355130252781402, 0.5657383060625951, 1.5456588046255575, -0.9742363337673154, -0.07034487710410242, 0.30796885521603423, -0.20849876310587975, 1.0338007325554992, -2.4004536338122957, 2.0306036208387996, -1.1426312890227635, 0.21188338677770105, 0.7047206243171088, -0.785435211763197, 0.4620597371620487, 0.7042282254621743, 0.5235079678938094, -0.9262543135302259, 2.0078429507780005, 0.2269625418708953, -1.1526591092509524, 0.6319794458091295, 0.0395126866933667, 0.46439232505089606, -3.5635166606247353, 1.3211056154702059, 0.15263055220453448, 0.16452954293239852, -0.4300956908764876, 0.7673687357524115, 0.9849198419098969, 0.270835848826804, 1.3919861934464073, 0.07984231300862901, -0.3999645806965225, -1.0278505586819058, -0.5847182112607883, 0.8165939265478418, -0.08194705182666534, -0.3447660142546443, 0.5282881452973941, -1.0689887834801322, -0.5118813091268151], [0.2912053597430635, 0.5665336963535724, 0.503591759111203, 0.2852956847818571, 0.48428811274975, 1.3634815124261457, -0.781105283625392, -0.4680176663374855, 1.2245743551261743, -1.2811082751440426, 0.8754755042743244, -1.710715324029529, -0.4507651031362744, 0.7491638059190651, -0.20393286610125122, -0.18217541166573417, 0.6806560043814565, -1.8184989903916142, 0.047071635325711084, 0.3948442093272043, -0.24843205438084665, -0.6177066479970167, -0.682883996449334, 0.4362576043409168, -1.703012774113238, 0.3937105991386652, -0.47932400357549726, -0.2990162929660804, 0.6941032876787643, 0.6786296737098565, 0.2395559950038969, 0.15122662929444983, 0.8161272333600409, 1.8935344675962007, 0.6396327631937027, -0.9620288319051914, -2.0852656421201097, 1.9302467674655757, -1.7353488744703927, 1.2103837049045143, 0.7974354194278735, -0.379810784047379, 0.7025622240016004, -0.850346271655115, 1.1768124501049289, -0.524336102632456, 0.7009077309156047, 0.9841880707224154, -0.12172840866682022, 2.365768628840039, 0.4961429262475947, 0.7965948666649523, -0.4740208901256851, -0.05669571649092953, 1.3577972581070583, -0.8048337241667037, -2.12362024909293, -0.33350244043324745, -0.886719352485378, 0.33419793089900884, 0.5367838249027502, -0.7438303679362013, -0.3202038822408791, -0.9161988612665409, -0.8596682999817407, 0.22598548673375538, 0.6287758265382943, 0.18649434877307466, 0.9524783451091219, 0.9881375825933089, -0.07260831396267549, -0.5506029235634193, -0.9381526140931042, -1.2390715625947926, 0.13968327403129469, -0.22301898188247601, 2.123691888593553, 0.12227343425882888, -1.4094317399227687, 1.4229859527722433, -2.14785503764361, -1.347532513457755, 0.3635645568066484, -0.014752111804594866, 1.2723950785462097, -1.4495666088633876, -1.1955237416669708, -0.591862973147249, -0.4145048435321895, -1.4257947334380214, 0.2093947875359238, -0.5928860038389254, -1.4731164134656474, -0.896580615301871, 1.1043515698603126, -0.43154951551604476, -0.16113690824405888, 0.8891574940728737, 0.2883768477152654, -1.0515389375700381]], "names": ["position", "series0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="182.774712175,145.894338645 185.936989835,139.569783325 189.099267495,145.894338645" transform="rotate(0, 185.936989835, 142.732060985)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="135.953275273,134.9144466 139.115552933,128.589891279 142.277830593,134.9144466" transform="rotate(0, 139.115552933, 131.75216894)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="209.84872154,137.424524874 213.0109992,131.099969554 216.17327686,137.424524874" transform="rotate(0, 213.0109992, 134.262247214)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="160.691072255,146.130012146 163.853349915,139.805456826 167.015627575,146.130012146" transform="rotate(0, 163.853349915, 142.967734486)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="149.201620781,138.194340127 152.363898442,131.869784807 155.526176102,138.194340127" transform="rotate(0, 152.363898442, 135.032062467)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="194.483593743,103.132752446 197.645871403,96.8081971258 200.808149064,103.132752446" transform="rotate(0, 197.645871403, 99.970474786)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="193.706963255,188.657300307 196.869240915,182.332744986 200.031518575,188.657300307" transform="rotate(0, 196.869240915, 185.495022647)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="151.569299501,176.171595854 154.731577161,169.847040533 157.893854821,176.171595854" transform="rotate(0, 154.731577161, 173.009318194)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="169.938929151,108.672267958 173.101206811,102.347712637 176.263484471,108.672267958" transform="rotate(0, 173.101206811, 105.509990298)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="106.332114846,208.597052737 109.494392507,202.272497417 112.656670167,208.597052737" transform="rotate(0, 109.494392507, 205.434775077)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="201.887348011,122.594073982 205.049625672,116.269518662 208.211903332,122.594073982" transform="rotate(0, 205.049625672, 119.431796322)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="197.434786247,225.729466627 200.597063907,219.404911307 203.759341567,225.729466627" transform="rotate(0, 200.597063907, 222.567188967)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="196.347009074,175.483576292 199.509286734,169.159020972 202.671564395,175.483576292" transform="rotate(0, 199.509286734, 172.321298632)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="112.568645963,127.631291833 115.730923623,121.306736513 118.893201283,127.631291833" transform="rotate(0, 115.730923623, 124.469014173)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="160.087628603,165.64008779 163.249906263,159.315532469 166.412183924,165.64008779" transform="rotate(0, 163.249906263, 162.477810129)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="169.556507552,164.772416471 172.718785212,158.447861151 175.881062873,164.772416471" transform="rotate(0, 172.718785212, 161.610138811)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="180.916350609,130.363332692 184.078628269,124.038777371 187.24090593,130.363332692" transform="rotate(0, 184.078628269, 127.201055031)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="177.639055333,230.027800157 180.801332993,223.703244837 183.963610654,230.027800157" transform="rotate(0, 180.801332993, 226.865522497)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="206.706974742,155.630212444 209.869252402,149.305657124 213.031530062,155.630212444" transform="rotate(0, 209.869252402, 152.467934784)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="125.92858894,141.761297367 129.0908666,135.436742047 132.25314426,141.761297367" transform="rotate(0, 129.0908666, 138.599019707)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="163.789355027,167.414682767 166.951632687,161.090127447 170.113910347,167.414682767" transform="rotate(0, 166.951632687, 164.252405107)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="151.021611694,182.14108261 154.183889354,175.816527289 157.346167014,182.14108261" transform="rotate(0, 154.183889354, 178.97880495)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="174.944514885,184.740307443 178.106792545,178.415752123 181.269070205,184.740307443" transform="rotate(0, 178.106792545, 181.578029783)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="185.084329714,140.109761561 188.246607374,133.78520624 191.408885035,140.109761561" transform="rotate(0, 188.246607374, 136.947483901)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="206.622293444,225.422294588 209.784571104,219.097739268 212.946848764,225.422294588" transform="rotate(0, 209.784571104, 222.260016928)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="156.278963952,141.80650491 159.441241612,135.481949589 162.603519272,141.80650491" transform="rotate(0, 159.441241612, 138.64422725)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="188.523676788,176.622484287 191.685954449,170.297928967 194.848232109,176.622484287" transform="rotate(0, 191.685954449, 173.460206627)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="118.320671305,169.431945087 121.482948966,163.107389766 124.645226626,169.431945087" transform="rotate(0, 121.482948966, 166.269667426)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="164.339632437,129.8270649 167.501910097,123.50250958 170.664187757,129.8270649" transform="rotate(0, 167.501910097, 126.66478724)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="199.322478983,130.444141272 202.484756643,124.119585952 205.647034303,130.444141272" transform="rotate(0, 202.484756643, 127.281863612)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="158.291761581,147.954077414 161.454039241,141.629522093 164.616316901,147.954077414" transform="rotate(0, 161.454039241, 144.791799753)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="179.000701717,151.476587707 182.162979377,145.152032387 185.325257037,151.476587707" transform="rotate(0, 182.162979377, 148.314310047)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="199.001664821,124.96083948 202.163942481,118.63628416 205.326220141,124.96083948" transform="rotate(0, 202.163942481, 121.79856182)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="198.955465645,81.9946295142 202.117743306,75.6700741939 205.280020966,81.9946295142" transform="rotate(0, 202.117743306, 78.832351854)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="193.823252196,131.99930945 196.985529857,125.67475413 200.147807517,131.99930945" transform="rotate(0, 196.985529857, 128.83703179)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="166.058161871,195.872398662 169.220439532,189.547843341 172.382717192,195.872398662" transform="rotate(0, 169.220439532, 192.710121001)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="173.009357242,240.666258491 176.171634902,234.341703171 179.333912563,240.666258491" transform="rotate(0, 176.171634902, 237.503980831)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="160.405399435,80.5305699326 163.567677095,74.2060146123 166.729954755,80.5305699326" transform="rotate(0, 163.567677095, 77.3682922725)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="193.202427806,226.711834544 196.364705467,220.387279224 199.526983127,226.711834544" transform="rotate(0, 196.364705467, 223.549556884)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="236.83772234,109.238180676 240.0,102.913625356 243.16227766,109.238180676" transform="rotate(0, 240.0, 106.075903016)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="171.64298894,125.706255305 174.8052666,119.381699985 177.967544261,125.706255305" transform="rotate(0, 174.8052666, 122.543977645)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="153.543018988,172.653970109 156.705296648,166.329414789 159.867574309,172.653970109" transform="rotate(0, 156.705296648, 169.491692449)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="170.514773989,129.489728727 173.677051649,123.165173406 176.839329309,129.489728727" transform="rotate(0, 173.677051649, 126.327451066)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="111.055555643,191.418580105 114.217833303,185.094024784 117.380110964,191.418580105" transform="rotate(0, 114.217833303, 188.256302444)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="176.475857187,110.576977685 179.638134848,104.252422365 182.800412508,110.576977685" transform="rotate(0, 179.638134848, 107.414700025)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="144.228620382,178.41753377 147.390898043,172.09297845 150.553175703,178.41753377" transform="rotate(0, 147.390898043, 175.25525611)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="165.644047826,129.555708697 168.806325486,123.231153377 171.968603146,129.555708697" transform="rotate(0, 168.806325486, 126.393431037)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="170.011955335,118.258696599 173.174232996,111.934141279 176.336510656,118.258696599" transform="rotate(0, 173.174232996, 115.096418939)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="190.772913265,162.361834344 193.935190925,156.037279023 197.097468585,162.361834344" transform="rotate(0, 193.935190925, 159.199556683)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="175.559836604,63.1622776602 178.722114264,56.8377223398 181.884391924,63.1622776602" transform="rotate(0, 178.722114264, 60.0)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="193.18367237,137.721578863 196.34595003,131.397023543 199.508227691,137.721578863" transform="rotate(0, 196.34595003, 134.559301203)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="128.775920834,125.739775933 131.938198495,119.415220612 135.100476155,125.739775933" transform="rotate(0, 131.938198495, 122.577498272)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="130.010574558,176.411000014 133.172852218,170.086444693 136.335129878,176.411000014" transform="rotate(0, 133.172852218, 173.248722354)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="166.654505327,159.768378297 169.816782988,153.443822976 172.979060648,159.768378297" transform="rotate(0, 169.816782988, 156.606100636)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="154.055716043,103.359436338 157.217993703,97.0348810173 160.380271363,103.359436338" transform="rotate(0, 157.217993703, 100.197158677)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="165.423667569,189.603573105 168.585945229,183.279017785 171.748222889,189.603573105" transform="rotate(0, 168.585945229, 186.441295445)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="179.467749219,242.195812075 182.630026879,235.871256754 185.792304539,242.195812075" transform="rotate(0, 182.630026879, 239.033534415)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="168.496627715,170.807227344 171.658905375,164.482672023 174.821183035,170.807227344" transform="rotate(0, 171.658905375, 167.644949684)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="185.430739478,192.86911188 188.593017138,186.54455656 191.755294798,192.86911188" transform="rotate(0, 188.593017138, 189.70683422)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="213.029985211,144.179826452 216.192262872,137.855271132 219.354540532,144.179826452" transform="rotate(0, 216.192262872, 141.017548792)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="142.057691796,136.100849645 145.219969456,129.776294324 148.382247116,136.100849645" transform="rotate(0, 145.219969456, 132.938571984)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="167.515596254,187.170804019 170.677873914,180.846248699 173.840151574,187.170804019" transform="rotate(0, 170.677873914, 184.008526359)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="178.170719479,170.276890601 181.332997139,163.95233528 184.495274799,170.276890601" transform="rotate(0, 181.332997139, 167.114612941)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="163.624522382,194.04473306 166.786800042,187.720177739 169.949077702,194.04473306" transform="rotate(0, 166.786800042, 190.8824554)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="198.613614973,191.790335754 201.775892633,185.465780434 204.938170293,191.790335754" transform="rotate(0, 201.775892633, 188.628058094)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="101.888594618,148.495259326 105.050872278,142.170704006 108.213149938,148.495259326" transform="rotate(0, 105.050872278, 145.332981666)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="226.688349507,132.432276118 229.850627167,126.107720797 233.012904827,132.432276118" transform="rotate(0, 229.850627167, 129.269998457)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="137.314884846,150.070136932 140.477162507,143.745581612 143.639440167,150.070136932" transform="rotate(0, 140.477162507, 146.907859272)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="175.464493353,119.52325719 178.626771013,113.19870187 181.789048673,119.52325719" transform="rotate(0, 178.626771013, 116.36097953)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="189.345145962,118.101192964 192.507423622,111.776637643 195.669701283,118.101192964" transform="rotate(0, 192.507423622, 114.938915303)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="147.375233952,160.402961008 150.537511612,154.078405688 153.699789272,160.402961008" transform="rotate(0, 150.537511612, 157.240683348)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="182.510655344,179.465035316 185.672933004,173.140479996 188.835210664,179.465035316" transform="rotate(0, 185.672933004, 176.302757656)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="189.331277657,194.920232614 192.493555317,188.595677294 195.655832977,194.920232614" transform="rotate(0, 192.493555317, 191.757954954)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="184.241331273,206.920659485 187.403608933,200.596104164 190.565886594,206.920659485" transform="rotate(0, 187.403608933, 203.758381824)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="143.409094863,151.936928245 146.571372523,145.612372925 149.733650183,151.936928245" transform="rotate(0, 146.571372523, 148.774650585)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="226.047300231,166.401228083 229.209577891,160.076672762 232.371855551,166.401228083" transform="rotate(0, 229.209577891, 163.238950423)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="175.889194446,72.8161204402 179.051472106,66.4915651198 182.213749766,72.8161204402" transform="rotate(0, 179.051472106, 69.65384278)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="137.032453491,152.631219881 140.194731151,146.306664561 143.357008811,152.631219881" transform="rotate(0, 140.194731151, 149.468942221)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="187.296406637,213.714498357 190.458684298,207.389943036 193.620961958,213.714498357" transform="rotate(0, 190.458684298, 210.552220696)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="170.609710423,100.759759026 173.771988083,94.4352037055 176.934265743,100.759759026" transform="rotate(0, 173.771988083, 97.5974813657)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="182.576352169,243.16227766 185.73862983,236.83772234 188.90090749,243.16227766" transform="rotate(0, 185.73862983, 240.0)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="69.1311797783,211.246002623 72.2934574384,204.921447303 75.4557350986,211.246002623" transform="rotate(0, 72.2934574384, 208.083724963)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="206.705493932,143.008706959 209.867771592,136.684151638 213.030049252,143.008706959" transform="rotate(0, 209.867771592, 139.846429299)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="173.795650274,158.095698117 176.957927934,151.771142797 180.120205594,158.095698117" transform="rotate(0, 176.957927934, 154.933420457)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="174.130782736,106.765212596 177.293060396,100.440657275 180.455338056,106.765212596" transform="rotate(0, 177.293060396, 103.602934935)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="157.383293555,215.315047482 160.545571215,208.990492161 163.707848876,215.315047482" transform="rotate(0, 160.545571215, 212.152769821)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="191.109616269,205.184004339 194.271893929,198.859449018 197.434171589,205.184004339" transform="rotate(0, 194.271893929, 202.021726679)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="197.236895418,181.110455819 200.399173078,174.785900499 203.561450738,181.110455819" transform="rotate(0, 200.399173078, 177.948178159)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="177.124876505,174.037543745 180.287154165,167.712988424 183.449431826,174.037543745" transform="rotate(0, 180.287154165, 170.875266085)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="208.701829851,214.367042532 211.864107511,208.042487212 215.026385171,214.367042532" transform="rotate(0, 211.864107511, 211.204764872)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="171.745585495,149.156884237 174.907863155,142.832328917 178.070140815,149.156884237" transform="rotate(0, 174.907863155, 145.994606577)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="158.231929659,181.151253533 161.394207319,174.826698212 164.55648498,181.151253533" transform="rotate(0, 161.394207319, 177.988975872)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="140.54765892,216.25419641 143.70993658,209.929641089 146.872214241,216.25419641" transform="rotate(0, 143.70993658, 213.091918749)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="153.028384211,193.262371805 156.190661871,186.937816485 159.352939531,193.262371805" transform="rotate(0, 156.190661871, 190.100094145)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="192.496032962,113.466664422 195.658310622,107.142109102 198.820588282,113.466664422" transform="rotate(0, 195.658310622, 110.304386762)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="167.18882355,174.717272757 170.35110121,168.392717437 173.51337887,174.717272757" transform="rotate(0, 170.35110121, 171.554995097)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="159.786585166,163.933416391 162.948862826,157.608861071 166.111140486,163.933416391" transform="rotate(0, 162.948862826, 160.771138731)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="184.37596392,122.048446268 187.538241581,115.723890948 190.700519241,122.048446268" transform="rotate(0, 187.538241581, 118.886168608)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="139.389009849,146.007137629 142.551287509,139.682582309 145.71356517,146.007137629" transform="rotate(0, 142.551287509, 142.844859969)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><polygon points="155.07981957,199.441995999 158.242097231,193.117440678 161.404374891,199.441995999" transform="rotate(0, 158.242097231, 196.279718338)"></polygon></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden;"><rect height="14" style="opacity:0.75;stroke:none;fill:white;" width="90" x="150" y="60"></rect><text style="font-size:10px;font-weight:normal;stroke:none;text-anchor:middle;alignment-baseline:middle;" x="195.0" y="67.0"></text></g><line style="" x1="72.2934574384" x2="240.0" y1="250" y2="250"></line><g><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="60.0" y="250">-4</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="116.329560968" y="250">-2</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="172.659121936" y="250">0</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="228.988682904" y="250">2</text></g><line style="" x1="50" x2="50" y1="60.0" y2="240.0"></line><g><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 234.103649586)" x="50" y="234.103649586">-2</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 194.224383324)" x="50" y="194.224383324">-1</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 154.345117063)" x="50" y="154.345117063">0</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 114.465850801)" x="50" y="114.465850801">1</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 74.5865845396)" x="50" y="74.5865845396">2</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="border-radius:6px;padding:5px;color:white;border:0;list-style:none;visibility:hidden;cursor:default;background:rgba(0%,0%,0%,0.75);position:fixed;margin:0;"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#t98a947c55b63430ba8c0429c4b676eb0 text");
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
              var text = document.querySelectorAll("#t98a947c55b63430ba8c0429c4b676eb0 text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="t98a947c55b63430ba8c0429c4b676eb0";
    
          function save_csv(dataset)
          {
            uri = "data:text/csv;charset=utf-8,";
            data = JSON.parse(dataset.textContent);
            uri += data.names.join(",") + "\n";
            for(var i = 0; i != data.data[0].length; ++i)
            {
              for(var j = 0; j != data.data.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data.data[j][i];
              }
              uri += "\n";
            }
    
            uri = encodeURI(uri);
            window.open(uri);
          }
    
          function open_popup(dataset)
          {
            return function(e)
            {
              var popup = document.querySelector("#" + root_id + " .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }
    
          }
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="t98a947c55b63430ba8c0429c4b676eb0";
    
          function sign(x)
          {
            if(x < 0)
              return -1;
            if(x > 0)
              return 1;
            return 0;
          }
    
          function log_n(x, base)
          {
            return Math.log(x) / Math.log(base);
          }
    
          function mix(a, b, amount)
          {
            return ((1.0 - amount) * a) + (amount * b);
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
            var x = null;
            var y = null;
    
            var axes = e.currentTarget.parentElement;
            var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
            point = d3_mousePoint(e.target, e);
    
            for(var i = 0; i != data["x"].length; ++i)
            {
              var segment = data["x"][i];
              if(segment.range.min <= point[0] && point[0] < segment.range.max)
              {
                var normalized = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  x = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            for(var i = 0; i != data["y"].length; ++i)
            {
              var segment = data["y"][i];
              if(segment.range.min <= point[1] && point[1] < segment.range.max)
              {
                var normalized = (segment.range.max - point[1]) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  y = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            if(x !== null && y !== null)
              text = "x=" + x + " y=" + y;
            else if(x !== null)
              text = "x=" + x;
            else if(y !== null)
              text = "y=" + y;
            else
              text = null;
    
            if(text !== null)
            {
              var coordinates = axes.querySelectorAll(".toyplot-coordinates");
              for(var i = 0; i != coordinates.length; ++i)
              {
                coordinates[i].style.visibility = "visible";
                coordinates[i].querySelector("text").textContent = text;
              }
            }
          }
    
          function clear_coordinates(e)
          {
            var axes = e.currentTarget.parentElement;
            var coordinates = axes.querySelectorAll(".toyplot-coordinates");
            for(var i = 0; i != coordinates.length; ++i)
              coordinates[i].style.visibility = "hidden";
          }
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-Axes2D .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
          }
        })();
        </script></div></div>


.. code:: python

    toyplot.scatterplot(x, y, marker="+", size=40, mstyle={"stroke":"black"}, width=300);


.. raw:: html

    <div align="center" class="toyplot" id="t59e647a5460648fb90eeddcfe328c635"><svg height="300px" id="t9fe2a8b517cc4906b18399f55aca8bf0" style="opacity:1.0;font-size:12px;font-family:helvetica;stroke-opacity:1.0;fill-opacity:1.0;stroke:#343434;stroke-width:1.0;background-color:transparent;fill:#343434;" width="300px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-Axes2D" id="t942cbb3e27424b9baad0467ba8188579"><toyplot:axes>{"y": [{"range": {"max": 240, "min": 60}, "scale": "linear", "domain": {"max": 2.3657686288400388, "min": -2.1478550376436099}}], "x": [{"range": {"max": 240, "min": 60}, "scale": "linear", "domain": {"max": 2.3909605154630329, "min": -4.0}}]}</toyplot:axes><clipPath id="t51e5ef083c334ba3b2ceed940d6e92ed"><rect height="200" width="200" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t51e5ef083c334ba3b2ceed940d6e92ed)" style="cursor:crosshair;"><rect height="200" style="pointer-events:all;visibility:hidden;" width="200" x="50" y="50"></rect><g class="toyplot-PlotMark" id="t1dae00915ee9453c89aba5dfd30f9a81" style="stroke:none;fill:none;"><toyplot:data-table title="Plot Data">{"data": [[0.47143516373249306, -1.1909756947064645, 1.4327069684260973, -0.3126518960917129, -0.7205887333650116, 0.8871629403077386, 0.8595884137174165, -0.6365235044173491, 0.015696372114428918, -2.2426849541854055, 1.150035724719818, 0.9919460223426778, 0.9533241281124304, -2.0212548201949705, -0.334077365808097, 0.002118364683486495, 0.405453411570191, 0.2890919409800353, 1.3211581921293856, -1.5469055532292402, -0.2026463246291819, -0.6559693441389339, 0.19342137647035826, 0.5534389109567419, 1.3181515541801367, -0.4693052847058996, 0.6755540851223808, -1.8170272265901968, -0.1831085401789987, 1.0589691875711504, -0.3978402281999914, 0.3374376536139724, 1.0475785728927218, 1.0459382556276653, 0.8637172916848387, -0.12209157484767426, 0.12471295376821585, -0.32279480560829565, 0.8416747129961416, 2.390960515463033, 0.07619958783723642, -0.5664459304649568, 0.036141936684072715, -2.0749776006900293, 0.24779219974854666, -0.8971567844396987, -0.1367948332613474, 0.018289191349219306, 0.7554139823981354, 0.2152685809694434, 0.841008794931391, -1.4458100770443063, -1.4019732815008439, -0.10091819994891389, -0.5482424491868549, -0.14461950836938436, 0.3540203321992379, -0.0355130252781402, 0.5657383060625951, 1.5456588046255575, -0.9742363337673154, -0.07034487710410242, 0.30796885521603423, -0.20849876310587975, 1.0338007325554992, -2.4004536338122957, 2.0306036208387996, -1.1426312890227635, 0.21188338677770105, 0.7047206243171088, -0.785435211763197, 0.4620597371620487, 0.7042282254621743, 0.5235079678938094, -0.9262543135302259, 2.0078429507780005, 0.2269625418708953, -1.1526591092509524, 0.6319794458091295, 0.0395126866933667, 0.46439232505089606, -3.5635166606247353, 1.3211056154702059, 0.15263055220453448, 0.16452954293239852, -0.4300956908764876, 0.7673687357524115, 0.9849198419098969, 0.270835848826804, 1.3919861934464073, 0.07984231300862901, -0.3999645806965225, -1.0278505586819058, -0.5847182112607883, 0.8165939265478418, -0.08194705182666534, -0.3447660142546443, 0.5282881452973941, -1.0689887834801322, -0.5118813091268151], [0.2912053597430635, 0.5665336963535724, 0.503591759111203, 0.2852956847818571, 0.48428811274975, 1.3634815124261457, -0.781105283625392, -0.4680176663374855, 1.2245743551261743, -1.2811082751440426, 0.8754755042743244, -1.710715324029529, -0.4507651031362744, 0.7491638059190651, -0.20393286610125122, -0.18217541166573417, 0.6806560043814565, -1.8184989903916142, 0.047071635325711084, 0.3948442093272043, -0.24843205438084665, -0.6177066479970167, -0.682883996449334, 0.4362576043409168, -1.703012774113238, 0.3937105991386652, -0.47932400357549726, -0.2990162929660804, 0.6941032876787643, 0.6786296737098565, 0.2395559950038969, 0.15122662929444983, 0.8161272333600409, 1.8935344675962007, 0.6396327631937027, -0.9620288319051914, -2.0852656421201097, 1.9302467674655757, -1.7353488744703927, 1.2103837049045143, 0.7974354194278735, -0.379810784047379, 0.7025622240016004, -0.850346271655115, 1.1768124501049289, -0.524336102632456, 0.7009077309156047, 0.9841880707224154, -0.12172840866682022, 2.365768628840039, 0.4961429262475947, 0.7965948666649523, -0.4740208901256851, -0.05669571649092953, 1.3577972581070583, -0.8048337241667037, -2.12362024909293, -0.33350244043324745, -0.886719352485378, 0.33419793089900884, 0.5367838249027502, -0.7438303679362013, -0.3202038822408791, -0.9161988612665409, -0.8596682999817407, 0.22598548673375538, 0.6287758265382943, 0.18649434877307466, 0.9524783451091219, 0.9881375825933089, -0.07260831396267549, -0.5506029235634193, -0.9381526140931042, -1.2390715625947926, 0.13968327403129469, -0.22301898188247601, 2.123691888593553, 0.12227343425882888, -1.4094317399227687, 1.4229859527722433, -2.14785503764361, -1.347532513457755, 0.3635645568066484, -0.014752111804594866, 1.2723950785462097, -1.4495666088633876, -1.1955237416669708, -0.591862973147249, -0.4145048435321895, -1.4257947334380214, 0.2093947875359238, -0.5928860038389254, -1.4731164134656474, -0.896580615301871, 1.1043515698603126, -0.43154951551604476, -0.16113690824405888, 0.8891574940728737, 0.2883768477152654, -1.0515389375700381]], "names": ["position", "series0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 185.936989835, 142.732060985)" x1="185.936989835" x2="185.936989835" y1="139.569783325" y2="145.894338645"></line><line transform="rotate(0, 185.936989835, 142.732060985)" x1="182.774712175" x2="189.099267495" y1="142.732060985" y2="142.732060985"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 139.115552933, 131.75216894)" x1="139.115552933" x2="139.115552933" y1="128.589891279" y2="134.9144466"></line><line transform="rotate(0, 139.115552933, 131.75216894)" x1="135.953275273" x2="142.277830593" y1="131.75216894" y2="131.75216894"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 213.0109992, 134.262247214)" x1="213.0109992" x2="213.0109992" y1="131.099969554" y2="137.424524874"></line><line transform="rotate(0, 213.0109992, 134.262247214)" x1="209.84872154" x2="216.17327686" y1="134.262247214" y2="134.262247214"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 163.853349915, 142.967734486)" x1="163.853349915" x2="163.853349915" y1="139.805456826" y2="146.130012146"></line><line transform="rotate(0, 163.853349915, 142.967734486)" x1="160.691072255" x2="167.015627575" y1="142.967734486" y2="142.967734486"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 152.363898442, 135.032062467)" x1="152.363898442" x2="152.363898442" y1="131.869784807" y2="138.194340127"></line><line transform="rotate(0, 152.363898442, 135.032062467)" x1="149.201620781" x2="155.526176102" y1="135.032062467" y2="135.032062467"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 197.645871403, 99.970474786)" x1="197.645871403" x2="197.645871403" y1="96.8081971258" y2="103.132752446"></line><line transform="rotate(0, 197.645871403, 99.970474786)" x1="194.483593743" x2="200.808149064" y1="99.970474786" y2="99.970474786"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 196.869240915, 185.495022647)" x1="196.869240915" x2="196.869240915" y1="182.332744986" y2="188.657300307"></line><line transform="rotate(0, 196.869240915, 185.495022647)" x1="193.706963255" x2="200.031518575" y1="185.495022647" y2="185.495022647"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 154.731577161, 173.009318194)" x1="154.731577161" x2="154.731577161" y1="169.847040533" y2="176.171595854"></line><line transform="rotate(0, 154.731577161, 173.009318194)" x1="151.569299501" x2="157.893854821" y1="173.009318194" y2="173.009318194"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 173.101206811, 105.509990298)" x1="173.101206811" x2="173.101206811" y1="102.347712637" y2="108.672267958"></line><line transform="rotate(0, 173.101206811, 105.509990298)" x1="169.938929151" x2="176.263484471" y1="105.509990298" y2="105.509990298"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 109.494392507, 205.434775077)" x1="109.494392507" x2="109.494392507" y1="202.272497417" y2="208.597052737"></line><line transform="rotate(0, 109.494392507, 205.434775077)" x1="106.332114846" x2="112.656670167" y1="205.434775077" y2="205.434775077"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 205.049625672, 119.431796322)" x1="205.049625672" x2="205.049625672" y1="116.269518662" y2="122.594073982"></line><line transform="rotate(0, 205.049625672, 119.431796322)" x1="201.887348011" x2="208.211903332" y1="119.431796322" y2="119.431796322"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 200.597063907, 222.567188967)" x1="200.597063907" x2="200.597063907" y1="219.404911307" y2="225.729466627"></line><line transform="rotate(0, 200.597063907, 222.567188967)" x1="197.434786247" x2="203.759341567" y1="222.567188967" y2="222.567188967"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 199.509286734, 172.321298632)" x1="199.509286734" x2="199.509286734" y1="169.159020972" y2="175.483576292"></line><line transform="rotate(0, 199.509286734, 172.321298632)" x1="196.347009074" x2="202.671564395" y1="172.321298632" y2="172.321298632"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 115.730923623, 124.469014173)" x1="115.730923623" x2="115.730923623" y1="121.306736513" y2="127.631291833"></line><line transform="rotate(0, 115.730923623, 124.469014173)" x1="112.568645963" x2="118.893201283" y1="124.469014173" y2="124.469014173"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 163.249906263, 162.477810129)" x1="163.249906263" x2="163.249906263" y1="159.315532469" y2="165.64008779"></line><line transform="rotate(0, 163.249906263, 162.477810129)" x1="160.087628603" x2="166.412183924" y1="162.477810129" y2="162.477810129"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 172.718785212, 161.610138811)" x1="172.718785212" x2="172.718785212" y1="158.447861151" y2="164.772416471"></line><line transform="rotate(0, 172.718785212, 161.610138811)" x1="169.556507552" x2="175.881062873" y1="161.610138811" y2="161.610138811"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 184.078628269, 127.201055031)" x1="184.078628269" x2="184.078628269" y1="124.038777371" y2="130.363332692"></line><line transform="rotate(0, 184.078628269, 127.201055031)" x1="180.916350609" x2="187.24090593" y1="127.201055031" y2="127.201055031"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 180.801332993, 226.865522497)" x1="180.801332993" x2="180.801332993" y1="223.703244837" y2="230.027800157"></line><line transform="rotate(0, 180.801332993, 226.865522497)" x1="177.639055333" x2="183.963610654" y1="226.865522497" y2="226.865522497"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 209.869252402, 152.467934784)" x1="209.869252402" x2="209.869252402" y1="149.305657124" y2="155.630212444"></line><line transform="rotate(0, 209.869252402, 152.467934784)" x1="206.706974742" x2="213.031530062" y1="152.467934784" y2="152.467934784"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 129.0908666, 138.599019707)" x1="129.0908666" x2="129.0908666" y1="135.436742047" y2="141.761297367"></line><line transform="rotate(0, 129.0908666, 138.599019707)" x1="125.92858894" x2="132.25314426" y1="138.599019707" y2="138.599019707"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 166.951632687, 164.252405107)" x1="166.951632687" x2="166.951632687" y1="161.090127447" y2="167.414682767"></line><line transform="rotate(0, 166.951632687, 164.252405107)" x1="163.789355027" x2="170.113910347" y1="164.252405107" y2="164.252405107"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 154.183889354, 178.97880495)" x1="154.183889354" x2="154.183889354" y1="175.816527289" y2="182.14108261"></line><line transform="rotate(0, 154.183889354, 178.97880495)" x1="151.021611694" x2="157.346167014" y1="178.97880495" y2="178.97880495"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 178.106792545, 181.578029783)" x1="178.106792545" x2="178.106792545" y1="178.415752123" y2="184.740307443"></line><line transform="rotate(0, 178.106792545, 181.578029783)" x1="174.944514885" x2="181.269070205" y1="181.578029783" y2="181.578029783"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 188.246607374, 136.947483901)" x1="188.246607374" x2="188.246607374" y1="133.78520624" y2="140.109761561"></line><line transform="rotate(0, 188.246607374, 136.947483901)" x1="185.084329714" x2="191.408885035" y1="136.947483901" y2="136.947483901"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 209.784571104, 222.260016928)" x1="209.784571104" x2="209.784571104" y1="219.097739268" y2="225.422294588"></line><line transform="rotate(0, 209.784571104, 222.260016928)" x1="206.622293444" x2="212.946848764" y1="222.260016928" y2="222.260016928"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 159.441241612, 138.64422725)" x1="159.441241612" x2="159.441241612" y1="135.481949589" y2="141.80650491"></line><line transform="rotate(0, 159.441241612, 138.64422725)" x1="156.278963952" x2="162.603519272" y1="138.64422725" y2="138.64422725"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 191.685954449, 173.460206627)" x1="191.685954449" x2="191.685954449" y1="170.297928967" y2="176.622484287"></line><line transform="rotate(0, 191.685954449, 173.460206627)" x1="188.523676788" x2="194.848232109" y1="173.460206627" y2="173.460206627"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 121.482948966, 166.269667426)" x1="121.482948966" x2="121.482948966" y1="163.107389766" y2="169.431945087"></line><line transform="rotate(0, 121.482948966, 166.269667426)" x1="118.320671305" x2="124.645226626" y1="166.269667426" y2="166.269667426"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 167.501910097, 126.66478724)" x1="167.501910097" x2="167.501910097" y1="123.50250958" y2="129.8270649"></line><line transform="rotate(0, 167.501910097, 126.66478724)" x1="164.339632437" x2="170.664187757" y1="126.66478724" y2="126.66478724"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 202.484756643, 127.281863612)" x1="202.484756643" x2="202.484756643" y1="124.119585952" y2="130.444141272"></line><line transform="rotate(0, 202.484756643, 127.281863612)" x1="199.322478983" x2="205.647034303" y1="127.281863612" y2="127.281863612"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 161.454039241, 144.791799753)" x1="161.454039241" x2="161.454039241" y1="141.629522093" y2="147.954077414"></line><line transform="rotate(0, 161.454039241, 144.791799753)" x1="158.291761581" x2="164.616316901" y1="144.791799753" y2="144.791799753"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 182.162979377, 148.314310047)" x1="182.162979377" x2="182.162979377" y1="145.152032387" y2="151.476587707"></line><line transform="rotate(0, 182.162979377, 148.314310047)" x1="179.000701717" x2="185.325257037" y1="148.314310047" y2="148.314310047"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 202.163942481, 121.79856182)" x1="202.163942481" x2="202.163942481" y1="118.63628416" y2="124.96083948"></line><line transform="rotate(0, 202.163942481, 121.79856182)" x1="199.001664821" x2="205.326220141" y1="121.79856182" y2="121.79856182"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 202.117743306, 78.832351854)" x1="202.117743306" x2="202.117743306" y1="75.6700741939" y2="81.9946295142"></line><line transform="rotate(0, 202.117743306, 78.832351854)" x1="198.955465645" x2="205.280020966" y1="78.832351854" y2="78.832351854"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 196.985529857, 128.83703179)" x1="196.985529857" x2="196.985529857" y1="125.67475413" y2="131.99930945"></line><line transform="rotate(0, 196.985529857, 128.83703179)" x1="193.823252196" x2="200.147807517" y1="128.83703179" y2="128.83703179"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 169.220439532, 192.710121001)" x1="169.220439532" x2="169.220439532" y1="189.547843341" y2="195.872398662"></line><line transform="rotate(0, 169.220439532, 192.710121001)" x1="166.058161871" x2="172.382717192" y1="192.710121001" y2="192.710121001"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 176.171634902, 237.503980831)" x1="176.171634902" x2="176.171634902" y1="234.341703171" y2="240.666258491"></line><line transform="rotate(0, 176.171634902, 237.503980831)" x1="173.009357242" x2="179.333912563" y1="237.503980831" y2="237.503980831"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 163.567677095, 77.3682922725)" x1="163.567677095" x2="163.567677095" y1="74.2060146123" y2="80.5305699326"></line><line transform="rotate(0, 163.567677095, 77.3682922725)" x1="160.405399435" x2="166.729954755" y1="77.3682922725" y2="77.3682922725"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 196.364705467, 223.549556884)" x1="196.364705467" x2="196.364705467" y1="220.387279224" y2="226.711834544"></line><line transform="rotate(0, 196.364705467, 223.549556884)" x1="193.202427806" x2="199.526983127" y1="223.549556884" y2="223.549556884"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 240.0, 106.075903016)" x1="240.0" x2="240.0" y1="102.913625356" y2="109.238180676"></line><line transform="rotate(0, 240.0, 106.075903016)" x1="236.83772234" x2="243.16227766" y1="106.075903016" y2="106.075903016"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 174.8052666, 122.543977645)" x1="174.8052666" x2="174.8052666" y1="119.381699985" y2="125.706255305"></line><line transform="rotate(0, 174.8052666, 122.543977645)" x1="171.64298894" x2="177.967544261" y1="122.543977645" y2="122.543977645"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 156.705296648, 169.491692449)" x1="156.705296648" x2="156.705296648" y1="166.329414789" y2="172.653970109"></line><line transform="rotate(0, 156.705296648, 169.491692449)" x1="153.543018988" x2="159.867574309" y1="169.491692449" y2="169.491692449"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 173.677051649, 126.327451066)" x1="173.677051649" x2="173.677051649" y1="123.165173406" y2="129.489728727"></line><line transform="rotate(0, 173.677051649, 126.327451066)" x1="170.514773989" x2="176.839329309" y1="126.327451066" y2="126.327451066"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 114.217833303, 188.256302444)" x1="114.217833303" x2="114.217833303" y1="185.094024784" y2="191.418580105"></line><line transform="rotate(0, 114.217833303, 188.256302444)" x1="111.055555643" x2="117.380110964" y1="188.256302444" y2="188.256302444"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 179.638134848, 107.414700025)" x1="179.638134848" x2="179.638134848" y1="104.252422365" y2="110.576977685"></line><line transform="rotate(0, 179.638134848, 107.414700025)" x1="176.475857187" x2="182.800412508" y1="107.414700025" y2="107.414700025"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 147.390898043, 175.25525611)" x1="147.390898043" x2="147.390898043" y1="172.09297845" y2="178.41753377"></line><line transform="rotate(0, 147.390898043, 175.25525611)" x1="144.228620382" x2="150.553175703" y1="175.25525611" y2="175.25525611"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 168.806325486, 126.393431037)" x1="168.806325486" x2="168.806325486" y1="123.231153377" y2="129.555708697"></line><line transform="rotate(0, 168.806325486, 126.393431037)" x1="165.644047826" x2="171.968603146" y1="126.393431037" y2="126.393431037"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 173.174232996, 115.096418939)" x1="173.174232996" x2="173.174232996" y1="111.934141279" y2="118.258696599"></line><line transform="rotate(0, 173.174232996, 115.096418939)" x1="170.011955335" x2="176.336510656" y1="115.096418939" y2="115.096418939"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 193.935190925, 159.199556683)" x1="193.935190925" x2="193.935190925" y1="156.037279023" y2="162.361834344"></line><line transform="rotate(0, 193.935190925, 159.199556683)" x1="190.772913265" x2="197.097468585" y1="159.199556683" y2="159.199556683"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 178.722114264, 60.0)" x1="178.722114264" x2="178.722114264" y1="56.8377223398" y2="63.1622776602"></line><line transform="rotate(0, 178.722114264, 60.0)" x1="175.559836604" x2="181.884391924" y1="60.0" y2="60.0"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 196.34595003, 134.559301203)" x1="196.34595003" x2="196.34595003" y1="131.397023543" y2="137.721578863"></line><line transform="rotate(0, 196.34595003, 134.559301203)" x1="193.18367237" x2="199.508227691" y1="134.559301203" y2="134.559301203"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 131.938198495, 122.577498272)" x1="131.938198495" x2="131.938198495" y1="119.415220612" y2="125.739775933"></line><line transform="rotate(0, 131.938198495, 122.577498272)" x1="128.775920834" x2="135.100476155" y1="122.577498272" y2="122.577498272"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 133.172852218, 173.248722354)" x1="133.172852218" x2="133.172852218" y1="170.086444693" y2="176.411000014"></line><line transform="rotate(0, 133.172852218, 173.248722354)" x1="130.010574558" x2="136.335129878" y1="173.248722354" y2="173.248722354"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 169.816782988, 156.606100636)" x1="169.816782988" x2="169.816782988" y1="153.443822976" y2="159.768378297"></line><line transform="rotate(0, 169.816782988, 156.606100636)" x1="166.654505327" x2="172.979060648" y1="156.606100636" y2="156.606100636"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 157.217993703, 100.197158677)" x1="157.217993703" x2="157.217993703" y1="97.0348810173" y2="103.359436338"></line><line transform="rotate(0, 157.217993703, 100.197158677)" x1="154.055716043" x2="160.380271363" y1="100.197158677" y2="100.197158677"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 168.585945229, 186.441295445)" x1="168.585945229" x2="168.585945229" y1="183.279017785" y2="189.603573105"></line><line transform="rotate(0, 168.585945229, 186.441295445)" x1="165.423667569" x2="171.748222889" y1="186.441295445" y2="186.441295445"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 182.630026879, 239.033534415)" x1="182.630026879" x2="182.630026879" y1="235.871256754" y2="242.195812075"></line><line transform="rotate(0, 182.630026879, 239.033534415)" x1="179.467749219" x2="185.792304539" y1="239.033534415" y2="239.033534415"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 171.658905375, 167.644949684)" x1="171.658905375" x2="171.658905375" y1="164.482672023" y2="170.807227344"></line><line transform="rotate(0, 171.658905375, 167.644949684)" x1="168.496627715" x2="174.821183035" y1="167.644949684" y2="167.644949684"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 188.593017138, 189.70683422)" x1="188.593017138" x2="188.593017138" y1="186.54455656" y2="192.86911188"></line><line transform="rotate(0, 188.593017138, 189.70683422)" x1="185.430739478" x2="191.755294798" y1="189.70683422" y2="189.70683422"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 216.192262872, 141.017548792)" x1="216.192262872" x2="216.192262872" y1="137.855271132" y2="144.179826452"></line><line transform="rotate(0, 216.192262872, 141.017548792)" x1="213.029985211" x2="219.354540532" y1="141.017548792" y2="141.017548792"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 145.219969456, 132.938571984)" x1="145.219969456" x2="145.219969456" y1="129.776294324" y2="136.100849645"></line><line transform="rotate(0, 145.219969456, 132.938571984)" x1="142.057691796" x2="148.382247116" y1="132.938571984" y2="132.938571984"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 170.677873914, 184.008526359)" x1="170.677873914" x2="170.677873914" y1="180.846248699" y2="187.170804019"></line><line transform="rotate(0, 170.677873914, 184.008526359)" x1="167.515596254" x2="173.840151574" y1="184.008526359" y2="184.008526359"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 181.332997139, 167.114612941)" x1="181.332997139" x2="181.332997139" y1="163.95233528" y2="170.276890601"></line><line transform="rotate(0, 181.332997139, 167.114612941)" x1="178.170719479" x2="184.495274799" y1="167.114612941" y2="167.114612941"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 166.786800042, 190.8824554)" x1="166.786800042" x2="166.786800042" y1="187.720177739" y2="194.04473306"></line><line transform="rotate(0, 166.786800042, 190.8824554)" x1="163.624522382" x2="169.949077702" y1="190.8824554" y2="190.8824554"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 201.775892633, 188.628058094)" x1="201.775892633" x2="201.775892633" y1="185.465780434" y2="191.790335754"></line><line transform="rotate(0, 201.775892633, 188.628058094)" x1="198.613614973" x2="204.938170293" y1="188.628058094" y2="188.628058094"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 105.050872278, 145.332981666)" x1="105.050872278" x2="105.050872278" y1="142.170704006" y2="148.495259326"></line><line transform="rotate(0, 105.050872278, 145.332981666)" x1="101.888594618" x2="108.213149938" y1="145.332981666" y2="145.332981666"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 229.850627167, 129.269998457)" x1="229.850627167" x2="229.850627167" y1="126.107720797" y2="132.432276118"></line><line transform="rotate(0, 229.850627167, 129.269998457)" x1="226.688349507" x2="233.012904827" y1="129.269998457" y2="129.269998457"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 140.477162507, 146.907859272)" x1="140.477162507" x2="140.477162507" y1="143.745581612" y2="150.070136932"></line><line transform="rotate(0, 140.477162507, 146.907859272)" x1="137.314884846" x2="143.639440167" y1="146.907859272" y2="146.907859272"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 178.626771013, 116.36097953)" x1="178.626771013" x2="178.626771013" y1="113.19870187" y2="119.52325719"></line><line transform="rotate(0, 178.626771013, 116.36097953)" x1="175.464493353" x2="181.789048673" y1="116.36097953" y2="116.36097953"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 192.507423622, 114.938915303)" x1="192.507423622" x2="192.507423622" y1="111.776637643" y2="118.101192964"></line><line transform="rotate(0, 192.507423622, 114.938915303)" x1="189.345145962" x2="195.669701283" y1="114.938915303" y2="114.938915303"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 150.537511612, 157.240683348)" x1="150.537511612" x2="150.537511612" y1="154.078405688" y2="160.402961008"></line><line transform="rotate(0, 150.537511612, 157.240683348)" x1="147.375233952" x2="153.699789272" y1="157.240683348" y2="157.240683348"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 185.672933004, 176.302757656)" x1="185.672933004" x2="185.672933004" y1="173.140479996" y2="179.465035316"></line><line transform="rotate(0, 185.672933004, 176.302757656)" x1="182.510655344" x2="188.835210664" y1="176.302757656" y2="176.302757656"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 192.493555317, 191.757954954)" x1="192.493555317" x2="192.493555317" y1="188.595677294" y2="194.920232614"></line><line transform="rotate(0, 192.493555317, 191.757954954)" x1="189.331277657" x2="195.655832977" y1="191.757954954" y2="191.757954954"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 187.403608933, 203.758381824)" x1="187.403608933" x2="187.403608933" y1="200.596104164" y2="206.920659485"></line><line transform="rotate(0, 187.403608933, 203.758381824)" x1="184.241331273" x2="190.565886594" y1="203.758381824" y2="203.758381824"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 146.571372523, 148.774650585)" x1="146.571372523" x2="146.571372523" y1="145.612372925" y2="151.936928245"></line><line transform="rotate(0, 146.571372523, 148.774650585)" x1="143.409094863" x2="149.733650183" y1="148.774650585" y2="148.774650585"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 229.209577891, 163.238950423)" x1="229.209577891" x2="229.209577891" y1="160.076672762" y2="166.401228083"></line><line transform="rotate(0, 229.209577891, 163.238950423)" x1="226.047300231" x2="232.371855551" y1="163.238950423" y2="163.238950423"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 179.051472106, 69.65384278)" x1="179.051472106" x2="179.051472106" y1="66.4915651198" y2="72.8161204402"></line><line transform="rotate(0, 179.051472106, 69.65384278)" x1="175.889194446" x2="182.213749766" y1="69.65384278" y2="69.65384278"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 140.194731151, 149.468942221)" x1="140.194731151" x2="140.194731151" y1="146.306664561" y2="152.631219881"></line><line transform="rotate(0, 140.194731151, 149.468942221)" x1="137.032453491" x2="143.357008811" y1="149.468942221" y2="149.468942221"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 190.458684298, 210.552220696)" x1="190.458684298" x2="190.458684298" y1="207.389943036" y2="213.714498357"></line><line transform="rotate(0, 190.458684298, 210.552220696)" x1="187.296406637" x2="193.620961958" y1="210.552220696" y2="210.552220696"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 173.771988083, 97.5974813657)" x1="173.771988083" x2="173.771988083" y1="94.4352037055" y2="100.759759026"></line><line transform="rotate(0, 173.771988083, 97.5974813657)" x1="170.609710423" x2="176.934265743" y1="97.5974813657" y2="97.5974813657"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 185.73862983, 240.0)" x1="185.73862983" x2="185.73862983" y1="236.83772234" y2="243.16227766"></line><line transform="rotate(0, 185.73862983, 240.0)" x1="182.576352169" x2="188.90090749" y1="240.0" y2="240.0"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 72.2934574384, 208.083724963)" x1="72.2934574384" x2="72.2934574384" y1="204.921447303" y2="211.246002623"></line><line transform="rotate(0, 72.2934574384, 208.083724963)" x1="69.1311797783" x2="75.4557350986" y1="208.083724963" y2="208.083724963"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 209.867771592, 139.846429299)" x1="209.867771592" x2="209.867771592" y1="136.684151638" y2="143.008706959"></line><line transform="rotate(0, 209.867771592, 139.846429299)" x1="206.705493932" x2="213.030049252" y1="139.846429299" y2="139.846429299"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 176.957927934, 154.933420457)" x1="176.957927934" x2="176.957927934" y1="151.771142797" y2="158.095698117"></line><line transform="rotate(0, 176.957927934, 154.933420457)" x1="173.795650274" x2="180.120205594" y1="154.933420457" y2="154.933420457"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 177.293060396, 103.602934935)" x1="177.293060396" x2="177.293060396" y1="100.440657275" y2="106.765212596"></line><line transform="rotate(0, 177.293060396, 103.602934935)" x1="174.130782736" x2="180.455338056" y1="103.602934935" y2="103.602934935"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 160.545571215, 212.152769821)" x1="160.545571215" x2="160.545571215" y1="208.990492161" y2="215.315047482"></line><line transform="rotate(0, 160.545571215, 212.152769821)" x1="157.383293555" x2="163.707848876" y1="212.152769821" y2="212.152769821"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 194.271893929, 202.021726679)" x1="194.271893929" x2="194.271893929" y1="198.859449018" y2="205.184004339"></line><line transform="rotate(0, 194.271893929, 202.021726679)" x1="191.109616269" x2="197.434171589" y1="202.021726679" y2="202.021726679"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 200.399173078, 177.948178159)" x1="200.399173078" x2="200.399173078" y1="174.785900499" y2="181.110455819"></line><line transform="rotate(0, 200.399173078, 177.948178159)" x1="197.236895418" x2="203.561450738" y1="177.948178159" y2="177.948178159"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 180.287154165, 170.875266085)" x1="180.287154165" x2="180.287154165" y1="167.712988424" y2="174.037543745"></line><line transform="rotate(0, 180.287154165, 170.875266085)" x1="177.124876505" x2="183.449431826" y1="170.875266085" y2="170.875266085"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 211.864107511, 211.204764872)" x1="211.864107511" x2="211.864107511" y1="208.042487212" y2="214.367042532"></line><line transform="rotate(0, 211.864107511, 211.204764872)" x1="208.701829851" x2="215.026385171" y1="211.204764872" y2="211.204764872"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 174.907863155, 145.994606577)" x1="174.907863155" x2="174.907863155" y1="142.832328917" y2="149.156884237"></line><line transform="rotate(0, 174.907863155, 145.994606577)" x1="171.745585495" x2="178.070140815" y1="145.994606577" y2="145.994606577"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 161.394207319, 177.988975872)" x1="161.394207319" x2="161.394207319" y1="174.826698212" y2="181.151253533"></line><line transform="rotate(0, 161.394207319, 177.988975872)" x1="158.231929659" x2="164.55648498" y1="177.988975872" y2="177.988975872"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 143.70993658, 213.091918749)" x1="143.70993658" x2="143.70993658" y1="209.929641089" y2="216.25419641"></line><line transform="rotate(0, 143.70993658, 213.091918749)" x1="140.54765892" x2="146.872214241" y1="213.091918749" y2="213.091918749"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 156.190661871, 190.100094145)" x1="156.190661871" x2="156.190661871" y1="186.937816485" y2="193.262371805"></line><line transform="rotate(0, 156.190661871, 190.100094145)" x1="153.028384211" x2="159.352939531" y1="190.100094145" y2="190.100094145"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 195.658310622, 110.304386762)" x1="195.658310622" x2="195.658310622" y1="107.142109102" y2="113.466664422"></line><line transform="rotate(0, 195.658310622, 110.304386762)" x1="192.496032962" x2="198.820588282" y1="110.304386762" y2="110.304386762"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 170.35110121, 171.554995097)" x1="170.35110121" x2="170.35110121" y1="168.392717437" y2="174.717272757"></line><line transform="rotate(0, 170.35110121, 171.554995097)" x1="167.18882355" x2="173.51337887" y1="171.554995097" y2="171.554995097"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 162.948862826, 160.771138731)" x1="162.948862826" x2="162.948862826" y1="157.608861071" y2="163.933416391"></line><line transform="rotate(0, 162.948862826, 160.771138731)" x1="159.786585166" x2="166.111140486" y1="160.771138731" y2="160.771138731"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 187.538241581, 118.886168608)" x1="187.538241581" x2="187.538241581" y1="115.723890948" y2="122.048446268"></line><line transform="rotate(0, 187.538241581, 118.886168608)" x1="184.37596392" x2="190.700519241" y1="118.886168608" y2="118.886168608"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 142.551287509, 142.844859969)" x1="142.551287509" x2="142.551287509" y1="139.682582309" y2="146.007137629"></line><line transform="rotate(0, 142.551287509, 142.844859969)" x1="139.389009849" x2="145.71356517" y1="142.844859969" y2="142.844859969"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:rgba(40%,76.1%,64.7%,1);"><line transform="rotate(0, 158.242097231, 196.279718338)" x1="158.242097231" x2="158.242097231" y1="193.117440678" y2="199.441995999"></line><line transform="rotate(0, 158.242097231, 196.279718338)" x1="155.07981957" x2="161.404374891" y1="196.279718338" y2="196.279718338"></line></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden;"><rect height="14" style="opacity:0.75;stroke:none;fill:white;" width="90" x="150" y="60"></rect><text style="font-size:10px;font-weight:normal;stroke:none;text-anchor:middle;alignment-baseline:middle;" x="195.0" y="67.0"></text></g><line style="" x1="72.2934574384" x2="240.0" y1="250" y2="250"></line><g><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="60.0" y="250">-4</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="116.329560968" y="250">-2</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="172.659121936" y="250">0</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="228.988682904" y="250">2</text></g><line style="" x1="50" x2="50" y1="60.0" y2="240.0"></line><g><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 234.103649586)" x="50" y="234.103649586">-2</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 194.224383324)" x="50" y="194.224383324">-1</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 154.345117063)" x="50" y="154.345117063">0</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 114.465850801)" x="50" y="114.465850801">1</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 74.5865845396)" x="50" y="74.5865845396">2</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="border-radius:6px;padding:5px;color:white;border:0;list-style:none;visibility:hidden;cursor:default;background:rgba(0%,0%,0%,0.75);position:fixed;margin:0;"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#t59e647a5460648fb90eeddcfe328c635 text");
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
              var text = document.querySelectorAll("#t59e647a5460648fb90eeddcfe328c635 text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="t59e647a5460648fb90eeddcfe328c635";
    
          function save_csv(dataset)
          {
            uri = "data:text/csv;charset=utf-8,";
            data = JSON.parse(dataset.textContent);
            uri += data.names.join(",") + "\n";
            for(var i = 0; i != data.data[0].length; ++i)
            {
              for(var j = 0; j != data.data.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data.data[j][i];
              }
              uri += "\n";
            }
    
            uri = encodeURI(uri);
            window.open(uri);
          }
    
          function open_popup(dataset)
          {
            return function(e)
            {
              var popup = document.querySelector("#" + root_id + " .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }
    
          }
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="t59e647a5460648fb90eeddcfe328c635";
    
          function sign(x)
          {
            if(x < 0)
              return -1;
            if(x > 0)
              return 1;
            return 0;
          }
    
          function log_n(x, base)
          {
            return Math.log(x) / Math.log(base);
          }
    
          function mix(a, b, amount)
          {
            return ((1.0 - amount) * a) + (amount * b);
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
            var x = null;
            var y = null;
    
            var axes = e.currentTarget.parentElement;
            var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
            point = d3_mousePoint(e.target, e);
    
            for(var i = 0; i != data["x"].length; ++i)
            {
              var segment = data["x"][i];
              if(segment.range.min <= point[0] && point[0] < segment.range.max)
              {
                var normalized = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  x = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            for(var i = 0; i != data["y"].length; ++i)
            {
              var segment = data["y"][i];
              if(segment.range.min <= point[1] && point[1] < segment.range.max)
              {
                var normalized = (segment.range.max - point[1]) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  y = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            if(x !== null && y !== null)
              text = "x=" + x + " y=" + y;
            else if(x !== null)
              text = "x=" + x;
            else if(y !== null)
              text = "y=" + y;
            else
              text = null;
    
            if(text !== null)
            {
              var coordinates = axes.querySelectorAll(".toyplot-coordinates");
              for(var i = 0; i != coordinates.length; ++i)
              {
                coordinates[i].style.visibility = "visible";
                coordinates[i].querySelector("text").textContent = text;
              }
            }
          }
    
          function clear_coordinates(e)
          {
            var axes = e.currentTarget.parentElement;
            var coordinates = axes.querySelectorAll(".toyplot-coordinates");
            for(var i = 0; i != coordinates.length; ++i)
              coordinates[i].style.visibility = "hidden";
          }
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-Axes2D .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
          }
        })();
        </script></div></div>


Here is every builtin marker in Toyplot, along with their short-form
strings:

.. code:: python

    markers = ["","|","-","+","x","*","^",">","v","<","s","d","o","oo","o|","o-","o+","ox","o*"]
    labels = ["\"%s\"" % marker for marker in markers]
    canvas = toyplot.Canvas(800, 150)
    axes = canvas.axes(show=False)
    axes.scatterplot(numpy.repeat(0, len(markers)), marker=markers, mstyle={"stroke":"black","fill":"#fec"}, size=200)
    axes.text(numpy.arange(len(markers)), numpy.repeat(-0.5, len(markers)), text=markers, style={"fill":"black", "font-size":"16px"});


.. raw:: html

    <div align="center" class="toyplot" id="t206bb8d5ea8742d5b5247d4b762e01e6"><svg height="150px" id="t0af9cd8460ed425984b5e7bb27d49041" style="opacity:1.0;font-size:12px;font-family:helvetica;stroke-opacity:1.0;fill-opacity:1.0;stroke:#343434;stroke-width:1.0;background-color:transparent;fill:#343434;" width="800px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-Axes2D" id="t6130a54ceb4d4fc1aa20ab492f28975e"><toyplot:axes>{"y": [{"range": {"max": 90, "min": 60}, "scale": "linear", "domain": {"max": 0.0, "min": -0.5}}], "x": [{"range": {"max": 740, "min": 60}, "scale": "linear", "domain": {"max": 20.0, "min": 0.0}}]}</toyplot:axes><clipPath id="te0ee5a15f4e04716b1e9a63b96802f9f"><rect height="50" width="700" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#te0ee5a15f4e04716b1e9a63b96802f9f)" style="cursor:crosshair;"><rect height="50" style="pointer-events:all;visibility:hidden;" width="700" x="50" y="50"></rect><g class="toyplot-PlotMark" id="t4a3a4de7ad964887bc7642192c5538d6" style="stroke:none;fill:none;"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], "names": ["position", "series0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><line transform="rotate(0, 94.0, 60.0)" x1="94.0" x2="94.0" y1="52.9289321881" y2="67.0710678119"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><line transform="rotate(90, 128.0, 60.0)" x1="128.0" x2="128.0" y1="52.9289321881" y2="67.0710678119"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><line transform="rotate(0, 162.0, 60.0)" x1="162.0" x2="162.0" y1="52.9289321881" y2="67.0710678119"></line><line transform="rotate(0, 162.0, 60.0)" x1="154.928932188" x2="169.071067812" y1="60.0" y2="60.0"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><line transform="rotate(45, 196.0, 60.0)" x1="196.0" x2="196.0" y1="52.9289321881" y2="67.0710678119"></line><line transform="rotate(45, 196.0, 60.0)" x1="188.928932188" x2="203.071067812" y1="60.0" y2="60.0"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><line transform="rotate(0, 230.0, 60.0)" x1="230.0" x2="230.0" y1="52.9289321881" y2="67.0710678119"></line><line transform="rotate(-60, 230.0, 60.0)" x1="230.0" x2="230.0" y1="52.9289321881" y2="67.0710678119"></line><line transform="rotate(60, 230.0, 60.0)" x1="230.0" x2="230.0" y1="52.9289321881" y2="67.0710678119"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><polygon points="256.928932188,67.0710678119 264.0,52.9289321881 271.071067812,67.0710678119" transform="rotate(0, 264.0, 60.0)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><polygon points="290.928932188,67.0710678119 298.0,52.9289321881 305.071067812,67.0710678119" transform="rotate(90, 298.0, 60.0)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><polygon points="324.928932188,67.0710678119 332.0,52.9289321881 339.071067812,67.0710678119" transform="rotate(180, 332.0, 60.0)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><polygon points="358.928932188,67.0710678119 366.0,52.9289321881 373.071067812,67.0710678119" transform="rotate(-90, 366.0, 60.0)"></polygon></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><rect height="14.1421356237" transform="rotate(0, 400.0, 60.0)" width="14.1421356237" x="392.928932188" y="52.9289321881"></rect></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><rect height="14.1421356237" transform="rotate(45, 434.0, 60.0)" width="14.1421356237" x="426.928932188" y="52.9289321881"></rect></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><circle cx="468.0" cy="60.0" r="7.07106781187"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><circle cx="502.0" cy="60.0" r="7.07106781187"></circle><circle cx="502.0" cy="60.0" r="3.53553390593"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><circle cx="536.0" cy="60.0" r="7.07106781187"></circle><line transform="rotate(0, 536.0, 60.0)" x1="536.0" x2="536.0" y1="52.9289321881" y2="67.0710678119"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><circle cx="570.0" cy="60.0" r="7.07106781187"></circle><line transform="rotate(90, 570.0, 60.0)" x1="570.0" x2="570.0" y1="52.9289321881" y2="67.0710678119"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><circle cx="604.0" cy="60.0" r="7.07106781187"></circle><line transform="rotate(0, 604.0, 60.0)" x1="604.0" x2="604.0" y1="52.9289321881" y2="67.0710678119"></line><line transform="rotate(0, 604.0, 60.0)" x1="596.928932188" x2="611.071067812" y1="60.0" y2="60.0"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><circle cx="638.0" cy="60.0" r="7.07106781187"></circle><line transform="rotate(45, 638.0, 60.0)" x1="638.0" x2="638.0" y1="52.9289321881" y2="67.0710678119"></line><line transform="rotate(45, 638.0, 60.0)" x1="630.928932188" x2="645.071067812" y1="60.0" y2="60.0"></line></g><g class="toyplot-Datum" style="opacity:1.0;stroke:black;fill:#fec;"><circle cx="672.0" cy="60.0" r="7.07106781187"></circle><line transform="rotate(0, 672.0, 60.0)" x1="672.0" x2="672.0" y1="52.9289321881" y2="67.0710678119"></line><line transform="rotate(-60, 672.0, 60.0)" x1="672.0" x2="672.0" y1="52.9289321881" y2="67.0710678119"></line><line transform="rotate(60, 672.0, 60.0)" x1="672.0" x2="672.0" y1="52.9289321881" y2="67.0710678119"></line></g></g></g><g class="toyplot-TextMark" id="t21a7576dba314dbba7f6e6b27d7c1a07" style="stroke:none;alignment-baseline:middle;font-weight:normal;font-size:16px;text-anchor:middle;fill:black;"><toyplot:data-table title="Text Data">{"data": [["", "|", "-", "+", "x", "*", "^", "&gt;", "v", "&lt;", "s", "d", "o", "oo", "o|", "o-", "o+", "ox", "o*"], [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0], [-0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5]], "names": ["text", "series0", "series1"]}</toyplot:data-table><g class="toyplot-Series"><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 60.0, 90.0)" x="60.0" y="90.0"></text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 94.0, 90.0)" x="94.0" y="90.0">|</text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 128.0, 90.0)" x="128.0" y="90.0">-</text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 162.0, 90.0)" x="162.0" y="90.0">+</text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 196.0, 90.0)" x="196.0" y="90.0">x</text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 230.0, 90.0)" x="230.0" y="90.0">*</text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 264.0, 90.0)" x="264.0" y="90.0">^</text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 298.0, 90.0)" x="298.0" y="90.0">&gt;</text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 332.0, 90.0)" x="332.0" y="90.0">v</text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 366.0, 90.0)" x="366.0" y="90.0">&lt;</text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 400.0, 90.0)" x="400.0" y="90.0">s</text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 434.0, 90.0)" x="434.0" y="90.0">d</text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 468.0, 90.0)" x="468.0" y="90.0">o</text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 502.0, 90.0)" x="502.0" y="90.0">oo</text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 536.0, 90.0)" x="536.0" y="90.0">o|</text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 570.0, 90.0)" x="570.0" y="90.0">o-</text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 604.0, 90.0)" x="604.0" y="90.0">o+</text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 638.0, 90.0)" x="638.0" y="90.0">ox</text><text class="toyplot-Datum" style="opacity:1.0;font-size:16px;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;fill:black;" transform="rotate(0.0, 672.0, 90.0)" x="672.0" y="90.0">o*</text></g></g></g><g class="toyplot-coordinates" style="visibility:hidden;"><rect height="14" style="opacity:0.75;stroke:none;fill:white;" width="90" x="650" y="60"></rect><text style="font-size:10px;font-weight:normal;stroke:none;text-anchor:middle;alignment-baseline:middle;" x="695.0" y="67.0"></text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="border-radius:6px;padding:5px;color:white;border:0;list-style:none;visibility:hidden;cursor:default;background:rgba(0%,0%,0%,0.75);position:fixed;margin:0;"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#t206bb8d5ea8742d5b5247d4b762e01e6 text");
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
              var text = document.querySelectorAll("#t206bb8d5ea8742d5b5247d4b762e01e6 text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="t206bb8d5ea8742d5b5247d4b762e01e6";
    
          function save_csv(dataset)
          {
            uri = "data:text/csv;charset=utf-8,";
            data = JSON.parse(dataset.textContent);
            uri += data.names.join(",") + "\n";
            for(var i = 0; i != data.data[0].length; ++i)
            {
              for(var j = 0; j != data.data.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data.data[j][i];
              }
              uri += "\n";
            }
    
            uri = encodeURI(uri);
            window.open(uri);
          }
    
          function open_popup(dataset)
          {
            return function(e)
            {
              var popup = document.querySelector("#" + root_id + " .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }
    
          }
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="t206bb8d5ea8742d5b5247d4b762e01e6";
    
          function sign(x)
          {
            if(x < 0)
              return -1;
            if(x > 0)
              return 1;
            return 0;
          }
    
          function log_n(x, base)
          {
            return Math.log(x) / Math.log(base);
          }
    
          function mix(a, b, amount)
          {
            return ((1.0 - amount) * a) + (amount * b);
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
            var x = null;
            var y = null;
    
            var axes = e.currentTarget.parentElement;
            var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
            point = d3_mousePoint(e.target, e);
    
            for(var i = 0; i != data["x"].length; ++i)
            {
              var segment = data["x"][i];
              if(segment.range.min <= point[0] && point[0] < segment.range.max)
              {
                var normalized = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  x = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            for(var i = 0; i != data["y"].length; ++i)
            {
              var segment = data["y"][i];
              if(segment.range.min <= point[1] && point[1] < segment.range.max)
              {
                var normalized = (segment.range.max - point[1]) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  y = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            if(x !== null && y !== null)
              text = "x=" + x + " y=" + y;
            else if(x !== null)
              text = "x=" + x;
            else if(y !== null)
              text = "y=" + y;
            else
              text = null;
    
            if(text !== null)
            {
              var coordinates = axes.querySelectorAll(".toyplot-coordinates");
              for(var i = 0; i != coordinates.length; ++i)
              {
                coordinates[i].style.visibility = "visible";
                coordinates[i].querySelector("text").textContent = text;
              }
            }
          }
    
          function clear_coordinates(e)
          {
            var axes = e.currentTarget.parentElement;
            var coordinates = axes.querySelectorAll(".toyplot-coordinates");
            for(var i = 0; i != coordinates.length; ++i)
              coordinates[i].style.visibility = "hidden";
          }
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-Axes2D .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
          }
        })();
        </script></div></div>


You can also specify custom markers, specifying the marker as an SVG
path containing only relative commands:

.. code:: python

    custom_marker = {"shape":"path", "path":"m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z"}
    canvas, axes, mark = toyplot.scatterplot(0, 0, size=0.1, marker=custom_marker, fill="#004712", width=400);
    axes.hlines(0, style={"stroke-width":0.1})
    axes.vlines(0, style={"stroke-width":0.1})



.. parsed-literal::

    <toyplot.AxisLinesMark at 0x10bd917d0>




.. raw:: html

    <div align="center" class="toyplot" id="t9aafd97e6f7746c8b1277658521befea"><svg height="400px" id="t7ae82bdd0fe24ac48ddae4e7d7478b22" style="opacity:1.0;font-size:12px;font-family:helvetica;stroke-opacity:1.0;fill-opacity:1.0;stroke:#343434;stroke-width:1.0;background-color:transparent;fill:#343434;" width="400px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-Axes2D" id="t2dc1f9101b02440eb7273916f4576a6a"><toyplot:axes>{"y": [{"range": {"max": 340, "min": 60}, "scale": "linear", "domain": {"max": 0.5, "min": -0.5}}], "x": [{"range": {"max": 340, "min": 60}, "scale": "linear", "domain": {"max": 0.5, "min": -0.5}}]}</toyplot:axes><clipPath id="t26f8807670a94f03b26c85bcd8103912"><rect height="300" width="300" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#t26f8807670a94f03b26c85bcd8103912)" style="cursor:crosshair;"><rect height="300" style="pointer-events:all;visibility:hidden;" width="300" x="50" y="50"></rect><g class="toyplot-PlotMark" id="t6b7fb575b2c44db7beaa4019e281cc23" style="stroke:none;fill:none;"><toyplot:data-table title="Plot Data">{"data": [[0.0], [0.0]], "names": ["position", "series0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(0%,27.8%,7.06%,1);"><path d="M 200.0 200.0m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(200.0, 200.0) scale(0.316227766017) translate(-200.0, -200.0)"></path></g></g></g><g class="toyplot-AxisLinesMark" id="t415945c0d1024fb1823fd26eb3fbfbed" style="stroke-width:0.1;"><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgba(0%,0%,0%,1);stroke-width:0.1;" x1="50" x2="350" y1="200.0" y2="200.0"></line></g></g><g class="toyplot-AxisLinesMark" id="t371434f241f6493d80669c9121c33573" style="stroke-width:0.1;"><g class="toyplot-Series"><line class="toyplot-Datum" style="opacity:1.0;stroke:rgba(0%,0%,0%,1);stroke-width:0.1;" x1="200.0" x2="200.0" y1="50" y2="350"></line></g></g></g><g class="toyplot-coordinates" style="visibility:hidden;"><rect height="14" style="opacity:0.75;stroke:none;fill:white;" width="90" x="250" y="60"></rect><text style="font-size:10px;font-weight:normal;stroke:none;text-anchor:middle;alignment-baseline:middle;" x="295.0" y="67.0"></text></g><line style="" x1="200.0" x2="200.0" y1="350" y2="350"></line><g><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="60.0" y="350">-0.5</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="200.0" y="350">0.0</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="340.0" y="350">0.5</text></g><line style="" x1="50" x2="50" y1="200.0" y2="200.0"></line><g><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 340.0)" x="50" y="340.0">-0.5</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 200.0)" x="50" y="200.0">0.0</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 60.0)" x="50" y="60.0">0.5</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="border-radius:6px;padding:5px;color:white;border:0;list-style:none;visibility:hidden;cursor:default;background:rgba(0%,0%,0%,0.75);position:fixed;margin:0;"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#t9aafd97e6f7746c8b1277658521befea text");
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
              var text = document.querySelectorAll("#t9aafd97e6f7746c8b1277658521befea text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="t9aafd97e6f7746c8b1277658521befea";
    
          function save_csv(dataset)
          {
            uri = "data:text/csv;charset=utf-8,";
            data = JSON.parse(dataset.textContent);
            uri += data.names.join(",") + "\n";
            for(var i = 0; i != data.data[0].length; ++i)
            {
              for(var j = 0; j != data.data.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data.data[j][i];
              }
              uri += "\n";
            }
    
            uri = encodeURI(uri);
            window.open(uri);
          }
    
          function open_popup(dataset)
          {
            return function(e)
            {
              var popup = document.querySelector("#" + root_id + " .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }
    
          }
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="t9aafd97e6f7746c8b1277658521befea";
    
          function sign(x)
          {
            if(x < 0)
              return -1;
            if(x > 0)
              return 1;
            return 0;
          }
    
          function log_n(x, base)
          {
            return Math.log(x) / Math.log(base);
          }
    
          function mix(a, b, amount)
          {
            return ((1.0 - amount) * a) + (amount * b);
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
            var x = null;
            var y = null;
    
            var axes = e.currentTarget.parentElement;
            var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
            point = d3_mousePoint(e.target, e);
    
            for(var i = 0; i != data["x"].length; ++i)
            {
              var segment = data["x"][i];
              if(segment.range.min <= point[0] && point[0] < segment.range.max)
              {
                var normalized = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  x = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            for(var i = 0; i != data["y"].length; ++i)
            {
              var segment = data["y"][i];
              if(segment.range.min <= point[1] && point[1] < segment.range.max)
              {
                var normalized = (segment.range.max - point[1]) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  y = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            if(x !== null && y !== null)
              text = "x=" + x + " y=" + y;
            else if(x !== null)
              text = "x=" + x;
            else if(y !== null)
              text = "y=" + y;
            else
              text = null;
    
            if(text !== null)
            {
              var coordinates = axes.querySelectorAll(".toyplot-coordinates");
              for(var i = 0; i != coordinates.length; ++i)
              {
                coordinates[i].style.visibility = "visible";
                coordinates[i].querySelector("text").textContent = text;
              }
            }
          }
    
          function clear_coordinates(e)
          {
            var axes = e.currentTarget.parentElement;
            var coordinates = axes.querySelectorAll(".toyplot-coordinates");
            for(var i = 0; i != coordinates.length; ++i)
              coordinates[i].style.visibility = "hidden";
          }
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-Axes2D .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
          }
        })();
        </script></div></div>


In this example the marker was exported as SVG from a drawing
application, and the path was run through an `online conversion
process <http://bl.ocks.org/themcmurder/6393419>`__ to ensure that it
contained only relative commands.

.. code:: python

    x = numpy.linspace(0, 10, 10)
    y = 10 + x ** 2
    canvas, axes, mark = toyplot.scatterplot(x, y, size=.015, fill="#004712", marker=custom_marker, xlabel="Years", ylabel="Oak Tree Population", padding=25, width=600);


.. raw:: html

    <div align="center" class="toyplot" id="t51ffab7c5884461aabc9f53c4b9bd101"><svg height="600px" id="tfd80411beb60496a87995cb80bd27174" style="opacity:1.0;font-size:12px;font-family:helvetica;stroke-opacity:1.0;fill-opacity:1.0;stroke:#343434;stroke-width:1.0;background-color:transparent;fill:#343434;" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-Axes2D" id="tccaefaa5e5b745598430c9556d762d88"><toyplot:axes>{"y": [{"range": {"max": 525, "min": 75}, "scale": "linear", "domain": {"max": 120.0, "min": 0.0}}], "x": [{"range": {"max": 525, "min": 75}, "scale": "linear", "domain": {"max": 10.0, "min": 0.0}}]}</toyplot:axes><clipPath id="tb77bf1e02e5649f9962b6e341e9fd393"><rect height="500" width="500" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#tb77bf1e02e5649f9962b6e341e9fd393)" style="cursor:crosshair;"><rect height="500" style="pointer-events:all;visibility:hidden;" width="500" x="50" y="50"></rect><g class="toyplot-PlotMark" id="t3a4cb3b8d69e46379a579077887f47d9" style="stroke:none;fill:none;"><toyplot:data-table title="Plot Data">{"data": [[0.0, 1.1111111111111112, 2.2222222222222223, 3.3333333333333335, 4.444444444444445, 5.555555555555555, 6.666666666666667, 7.777777777777779, 8.88888888888889, 10.0], [10.0, 11.234567901234568, 14.938271604938272, 21.111111111111114, 29.75308641975309, 40.864197530864196, 54.44444444444445, 70.49382716049384, 89.01234567901236, 110.0]], "names": ["position", "series0"]}</toyplot:data-table><g class="toyplot-Series"><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(0%,27.8%,7.06%,1);"><path d="M 75.0 487.5m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(75.0, 487.5) scale(0.122474487139) translate(-75.0, -487.5)"></path></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(0%,27.8%,7.06%,1);"><path d="M 125.0 482.87037037m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(125.0, 482.87037037) scale(0.122474487139) translate(-125.0, -482.87037037)"></path></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(0%,27.8%,7.06%,1);"><path d="M 175.0 468.981481481m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(175.0, 468.981481481) scale(0.122474487139) translate(-175.0, -468.981481481)"></path></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(0%,27.8%,7.06%,1);"><path d="M 225.0 445.833333333m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(225.0, 445.833333333) scale(0.122474487139) translate(-225.0, -445.833333333)"></path></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(0%,27.8%,7.06%,1);"><path d="M 275.0 413.425925926m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(275.0, 413.425925926) scale(0.122474487139) translate(-275.0, -413.425925926)"></path></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(0%,27.8%,7.06%,1);"><path d="M 325.0 371.759259259m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(325.0, 371.759259259) scale(0.122474487139) translate(-325.0, -371.759259259)"></path></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(0%,27.8%,7.06%,1);"><path d="M 375.0 320.833333333m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(375.0, 320.833333333) scale(0.122474487139) translate(-375.0, -320.833333333)"></path></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(0%,27.8%,7.06%,1);"><path d="M 425.0 260.648148148m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(425.0, 260.648148148) scale(0.122474487139) translate(-425.0, -260.648148148)"></path></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(0%,27.8%,7.06%,1);"><path d="M 475.0 191.203703704m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(475.0, 191.203703704) scale(0.122474487139) translate(-475.0, -191.203703704)"></path></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(0%,27.8%,7.06%,1);"><path d="M 525.0 112.5m -165 45 c 8.483 6.576 17.276 11.581 26.38 15.013 c 9.101 3.431 18.562 5.146 28.381 5.146 c 9.723 0 17.801 -1.595 24.235 -4.789 c 6.434 -3.192 11.271 -7.887 14.513 -14.084 c 3.239 -6.194 4.861 -13.868 4.861 -23.02 h 6.72 c 0.19 2.384 0.286 5.054 0.286 8.007 c 0 15.92 -6.244 27.405 -18.73 34.458 c 12.01 -2.002 22.852 -4.74 32.528 -8.222 c 9.673 -3.478 20.231 -8.458 31.669 -14.94 l 4.003 7.148 c -13.346 8.389 -28.359 15.109 -45.038 20.16 c -16.682 5.054 -32.123 7.578 -46.325 7.578 c -13.44 0 -26.451 -2.12 -39.033 -6.363 c -12.583 -4.24 -22.877 -9.937 -30.884 -17.086 c -2.766 -2.667 -4.146 -5.098 -4.146 -7.291 c 0 -1.238 0.476 -2.335 1.43 -3.289 c 0.952 -0.951 2.048 -1.43 3.289 -1.43 c 1.236 0.000995874 3.191 1.002 5.861 3.004 Z m 140.262 -81.355 c 8.579 0 12.868 4.195 12.868 12.582 c 0 7.055 -2.288 13.654 -6.863 19.802 c -4.575 6.148 -10.701 11.059 -18.373 14.727 c -7.674 3.671 -15.942 5.505 -24.807 5.505 c -9.343 0 -17.943 -1.881 -25.808 -5.647 c -7.864 -3.765 -14.083 -8.815 -18.659 -15.156 c -4.575 -6.338 -6.863 -13.176 -6.863 -20.517 c 0 -3.908 1.048 -6.767 3.146 -8.579 c 2.096 -1.81 5.48 -2.716 10.151 -2.716 h 75.208 Z m -30.741 -8.00601 c -2.766 0 -4.839 -0.451 -6.219 -1.358 c -1.383 -0.905 -2.359 -2.549 -2.931 -4.933 c -0.572 -2.381 -0.858 -5.623 -0.858 -9.723 c 0 -6.863 1.477 -14.963 4.432 -24.306 c 0.19 -1.238 0.286 -2.049 0.286 -2.431 c 0 -0.952 -0.382 -1.43 -1.144 -1.43 c -0.857 0 -1.955 0.954 -3.288 2.859 c -5.815 8.579 -9.629 19.351 -11.438 32.313 c -0.478 3.528 -1.383 5.911 -2.717 7.149 c -1.336 1.24 -3.624 1.859 -6.863 1.859 h -11.724 c -4.29 0 -7.27 -0.69 -8.936 -2.073 c -1.669 -1.381 -2.502 -3.979 -2.502 -7.792 c 0 -5.147 1.573 -9.959 4.718 -14.441 c 2.096 -3.239 4.455 -6.005 7.078 -8.292 c 2.621 -2.288 7.696 -5.956 15.227 -11.009 c 4.669 -3.146 8.172 -5.885 10.509 -8.221 c 2.335 -2.335 4.169 -5.076 5.505 -8.221 c 0.858 -2.288 2.145 -3.432 3.86 -3.432 c 1.43 0 2.764 1.336 4.003 4.003 c 1.62 3.242 3.192 5.647 4.718 7.22 c 1.524 1.573 4.669 4.075 9.437 7.506 c 18.301 12.393 27.452 23.402 27.452 33.028 c 0 7.817 -4.576 11.724 -13.726 11.724 h -24.879 Z m 156.705 -2.57399 c 5.812 -8.007 12.152 -12.01 19.016 -12.01 c 2.953 0 5.719 0.764 8.293 2.288 c 2.574 1.526 4.598 3.503 6.076 5.934 c 1.477 2.431 2.217 4.933 2.217 7.506 c 0 4.576 1.381 6.863 4.146 6.863 c 1.43 0 3.479 -0.809 6.146 -2.431 c 3.336 -1.716 6.482 -2.574 9.438 -2.574 c 4.766 0 8.625 1.669 11.582 5.004 c 2.953 3.337 4.432 7.435 4.432 12.296 c 0 5.147 -1.383 8.985 -4.146 11.51 c -2.766 2.527 -7.148 4.028 -13.154 4.504 c -2.859 0.192 -4.695 0.525 -5.504 1.001 c -0.811 0.478 -1.215 1.526 -1.215 3.146 c 0 0.286 0.547 2.194 1.643 5.719 c 1.096 3.527 1.645 6.387 1.645 8.578 c 0 4.004 -1.5 7.245 -4.504 9.723 c -3.002 2.48 -6.887 3.718 -11.652 3.718 c -3.051 0 -8.006 -1.048 -14.869 -3.146 c -2.289 -0.762 -3.861 -1.144 -4.719 -1.144 c -1.43 0 -2.574 0.429 -3.432 1.286 c -0.857 0.858 -1.287 2.051 -1.287 3.575 c 0 1.336 0.715 3.527 2.145 6.576 c 1.145 2.288 1.717 4.433 1.717 6.435 c 0 3.623 -1.525 6.673 -4.576 9.15 c -3.051 2.479 -6.816 3.718 -11.295 3.718 c -3.051 0 -6.959 -1.001 -11.725 -3.003 c -3.812 -1.523 -6.244 -2.287 -7.291 -2.287 c -3.719 0 -5.576 2.812 -5.576 8.436 c 0 14.107 -9.057 21.16 -27.166 21.16 c -10.105 0 -19.588 -2.381 -28.453 -7.148 c -8.865 -4.766 -16.062 -11.39 -21.589 -19.874 c 10.867 -4.955 25.783 -13.916 44.751 -26.88 c 13.248 -8.673 24.043 -15.084 32.385 -19.23 c 8.34 -4.146 17.562 -7.601 27.666 -10.366 c 8.102 -2.381 19.396 -4.526 33.887 -6.434 c 1.047 0 1.572 -0.286 1.572 -0.858 c 0 -1.144 -3.527 -1.716 -10.58 -1.716 c -12.393 0 -25.164 1.908 -38.318 5.719 c -14.68 4.481 -30.883 12.203 -48.613 23.163 c -14.488 8.579 -24.258 14.347 -29.311 17.301 c -5.053 2.955 -8.244 4.789 -9.578 5.504 c -1.335 0.715 -4.099 2.026 -8.293 3.933 c -3.146 -7.625 -4.718 -15.632 -4.718 -24.021 c 0 -6.099 0.809 -11.914 2.431 -17.443 c 1.62 -5.527 3.812 -10.317 6.577 -14.37 c 2.763 -4.05 5.955 -7.196 9.58 -9.437 c 3.621 -2.238 7.48 -3.36 11.58 -3.36 c 4.098 0 8.008 1.669 11.725 5.004 c 2.953 2.766 5.193 4.146 6.721 4.146 c 3.621 0 5.67 -2.953 6.146 -8.864 c 1.811 -16.394 8.959 -24.592 21.447 -24.592 c 3.812 0 7.006 0.979 9.58 2.931 c 2.574 1.955 5.004 5.219 7.291 9.794 c 2.002 3.431 4.291 5.147 6.863 5.147 c 3.61802 -0.00100613 7.909 -3.19301 12.866 -9.58 Z" transform="translate(525.0, 112.5) scale(0.122474487139) translate(-525.0, -112.5)"></path></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden;"><rect height="14" style="opacity:0.75;stroke:none;fill:white;" width="90" x="450" y="60"></rect><text style="font-size:10px;font-weight:normal;stroke:none;text-anchor:middle;alignment-baseline:middle;" x="495.0" y="67.0"></text></g><line style="" x1="75.0" x2="525.0" y1="550" y2="550"></line><g><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="75.0" y="550">0</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="300.0" y="550">5</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="525.0" y="550">10</text></g><text style="stroke:none;font-weight:bold;baseline-shift:-200%;text-anchor:middle;alignment-baseline:middle;" x="300.0" y="550">Years</text><line style="" x1="50" x2="50" y1="112.5" y2="487.5"></line><g><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 525.0)" x="50" y="525.0">0</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 375.0)" x="50" y="375.0">40</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 225.0)" x="50" y="225.0">80</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 75.0)" x="50" y="75.0">120</text></g><text style="stroke:none;font-weight:bold;baseline-shift:200%;text-anchor:middle;alignment-baseline:middle;" transform="rotate(-90, 50, 300.0)" x="50" y="300.0">Oak Tree Population</text></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="border-radius:6px;padding:5px;color:white;border:0;list-style:none;visibility:hidden;cursor:default;background:rgba(0%,0%,0%,0.75);position:fixed;margin:0;"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#t51ffab7c5884461aabc9f53c4b9bd101 text");
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
              var text = document.querySelectorAll("#t51ffab7c5884461aabc9f53c4b9bd101 text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="t51ffab7c5884461aabc9f53c4b9bd101";
    
          function save_csv(dataset)
          {
            uri = "data:text/csv;charset=utf-8,";
            data = JSON.parse(dataset.textContent);
            uri += data.names.join(",") + "\n";
            for(var i = 0; i != data.data[0].length; ++i)
            {
              for(var j = 0; j != data.data.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data.data[j][i];
              }
              uri += "\n";
            }
    
            uri = encodeURI(uri);
            window.open(uri);
          }
    
          function open_popup(dataset)
          {
            return function(e)
            {
              var popup = document.querySelector("#" + root_id + " .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }
    
          }
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="t51ffab7c5884461aabc9f53c4b9bd101";
    
          function sign(x)
          {
            if(x < 0)
              return -1;
            if(x > 0)
              return 1;
            return 0;
          }
    
          function log_n(x, base)
          {
            return Math.log(x) / Math.log(base);
          }
    
          function mix(a, b, amount)
          {
            return ((1.0 - amount) * a) + (amount * b);
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
            var x = null;
            var y = null;
    
            var axes = e.currentTarget.parentElement;
            var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
            point = d3_mousePoint(e.target, e);
    
            for(var i = 0; i != data["x"].length; ++i)
            {
              var segment = data["x"][i];
              if(segment.range.min <= point[0] && point[0] < segment.range.max)
              {
                var normalized = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  x = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            for(var i = 0; i != data["y"].length; ++i)
            {
              var segment = data["y"][i];
              if(segment.range.min <= point[1] && point[1] < segment.range.max)
              {
                var normalized = (segment.range.max - point[1]) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  y = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            if(x !== null && y !== null)
              text = "x=" + x + " y=" + y;
            else if(x !== null)
              text = "x=" + x;
            else if(y !== null)
              text = "y=" + y;
            else
              text = null;
    
            if(text !== null)
            {
              var coordinates = axes.querySelectorAll(".toyplot-coordinates");
              for(var i = 0; i != coordinates.length; ++i)
              {
                coordinates[i].style.visibility = "visible";
                coordinates[i].querySelector("text").textContent = text;
              }
            }
          }
    
          function clear_coordinates(e)
          {
            var axes = e.currentTarget.parentElement;
            var coordinates = axes.querySelectorAll(".toyplot-coordinates");
            for(var i = 0; i != coordinates.length; ++i)
              coordinates[i].style.visibility = "hidden";
          }
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-Axes2D .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
          }
        })();
        </script></div></div>


Markers can also be added to regular plots to show the datums:

.. code:: python

    toyplot.plot(numpy.linspace(0, 1, 20) ** 2, marker="o", size=40, width=300);


.. raw:: html

    <div align="center" class="toyplot" id="te2deec51663840fcb3f4570d78d8824e"><svg height="300px" id="tbd097a483dd3432a91b880323eab6d46" style="opacity:1.0;font-size:12px;font-family:helvetica;stroke-opacity:1.0;fill-opacity:1.0;stroke:#343434;stroke-width:1.0;background-color:transparent;fill:#343434;" width="300px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot"><g class="toyplot-Axes2D" id="t331fa1a5c6d84f44af226e0f5779d960"><toyplot:axes>{"y": [{"range": {"max": 240, "min": 60}, "scale": "linear", "domain": {"max": 1.0, "min": 0.0}}], "x": [{"range": {"max": 240, "min": 60}, "scale": "linear", "domain": {"max": 20.0, "min": 0}}]}</toyplot:axes><clipPath id="te5f1fc235eec4a47b6999da67bf34554"><rect height="200" width="200" x="50" y="50"></rect></clipPath><g class="toyplot-coordinate-events" clip-path="url(#te5f1fc235eec4a47b6999da67bf34554)" style="cursor:crosshair;"><rect height="200" style="pointer-events:all;visibility:hidden;" width="200" x="50" y="50"></rect><g class="toyplot-PlotMark" id="t5949fb8a45cc4ee8a986c14019a867ac" style="fill:none;"><toyplot:data-table title="Plot Data">{"data": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0.0, 0.0027700831024930744, 0.011080332409972297, 0.02493074792243767, 0.04432132963988919, 0.06925207756232686, 0.09972299168975068, 0.13573407202216065, 0.17728531855955676, 0.22437673130193903, 0.27700831024930744, 0.33518005540166207, 0.39889196675900274, 0.4681440443213295, 0.5429362880886426, 0.6232686980609419, 0.709141274238227, 0.8005540166204984, 0.8975069252077561, 1.0]], "names": ["position", "series0"]}</toyplot:data-table><g class="toyplot-Series"><path d="M 60.0 240.0 L 69.0 239.501385042 L 78.0 238.005540166 L 87.0 235.512465374 L 96.0 232.022160665 L 105.0 227.534626039 L 114.0 222.049861496 L 123.0 215.567867036 L 132.0 208.088642659 L 141.0 199.612188366 L 150.0 190.138504155 L 159.0 179.667590028 L 168.0 168.199445983 L 177.0 155.734072022 L 186.0 142.271468144 L 195.0 127.811634349 L 204.0 112.354570637 L 213.0 95.9002770083 L 222.0 78.4487534626 L 231.0 60.0" style="stroke:rgba(40%,76.1%,64.7%,1);stroke-width:2.0;stroke-opacity:1.0;fill:none;"></path><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="60.0" cy="240.0" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="69.0" cy="239.501385042" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="78.0" cy="238.005540166" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="87.0" cy="235.512465374" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="96.0" cy="232.022160665" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="105.0" cy="227.534626039" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="114.0" cy="222.049861496" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="123.0" cy="215.567867036" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="132.0" cy="208.088642659" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="141.0" cy="199.612188366" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="150.0" cy="190.138504155" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="159.0" cy="179.667590028" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="168.0" cy="168.199445983" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="177.0" cy="155.734072022" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="186.0" cy="142.271468144" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="195.0" cy="127.811634349" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="204.0" cy="112.354570637" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="213.0" cy="95.9002770083" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="222.0" cy="78.4487534626" r="3.16227766017"></circle></g><g class="toyplot-Datum" style="opacity:1.0;stroke:none;fill:rgba(40%,76.1%,64.7%,1);"><circle cx="231.0" cy="60.0" r="3.16227766017"></circle></g></g></g></g><g class="toyplot-coordinates" style="visibility:hidden;"><rect height="14" style="opacity:0.75;stroke:none;fill:white;" width="90" x="150" y="60"></rect><text style="font-size:10px;font-weight:normal;stroke:none;text-anchor:middle;alignment-baseline:middle;" x="195.0" y="67.0"></text></g><line style="" x1="60.0" x2="231.0" y1="250" y2="250"></line><g><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="60.0" y="250">0</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="105.0" y="250">5</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="150.0" y="250">10</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="195.0" y="250">15</text><text style="font-size:10px;baseline-shift:-80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" x="240.0" y="250">20</text></g><line style="" x1="50" x2="50" y1="60.0" y2="240.0"></line><g><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 240.0)" x="50" y="240.0">0.0</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 150.0)" x="50" y="150.0">0.5</text><text style="font-size:10px;baseline-shift:80%;alignment-baseline:middle;font-weight:normal;stroke:none;text-anchor:middle;" transform="rotate(-90, 50, 60.0)" x="50" y="60.0">1.0</text></g></g></svg><div class="toyplot-controls"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="border-radius:6px;padding:5px;color:white;border:0;list-style:none;visibility:hidden;cursor:default;background:rgba(0%,0%,0%,0.75);position:fixed;margin:0;"><li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0;"></li><li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0;">Save as .csv</li></ul><script>
        (function()
        {
          // Workaround for browsers that don't support alignment-baseline
          if(window.CSS !== undefined && window.CSS.supports !== undefined)
          {
            if(!window.CSS.supports("alignment-baseline", "middle"))
            {
              var re = /\s*alignment-baseline\s*:\s*([^;\s]*)\s*/;
              var text = document.querySelectorAll("#te2deec51663840fcb3f4570d78d8824e text");
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
              var text = document.querySelectorAll("#te2deec51663840fcb3f4570d78d8824e text");
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
        // Allow users to extract embedded raw data
        (function()
        {
          var root_id="te2deec51663840fcb3f4570d78d8824e";
    
          function save_csv(dataset)
          {
            uri = "data:text/csv;charset=utf-8,";
            data = JSON.parse(dataset.textContent);
            uri += data.names.join(",") + "\n";
            for(var i = 0; i != data.data[0].length; ++i)
            {
              for(var j = 0; j != data.data.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data.data[j][i];
              }
              uri += "\n";
            }
    
            uri = encodeURI(uri);
            window.open(uri);
          }
    
          function open_popup(dataset)
          {
            return function(e)
            {
              var popup = document.querySelector("#" + root_id + " .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = dataset.getAttribute("title");
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(dataset); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }
    
          }
    
          var datasets = document.querySelectorAll("#" + root_id + " toyplot\\:data-table");
          for(var i = 0; i != datasets.length; ++i)
          {
            var dataset = datasets[i];
            var mark = dataset.parentElement;
            mark.oncontextmenu = open_popup(dataset);
          }
        })();
        </script><script>
        (function()
        {
          var root_id="te2deec51663840fcb3f4570d78d8824e";
    
          function sign(x)
          {
            if(x < 0)
              return -1;
            if(x > 0)
              return 1;
            return 0;
          }
    
          function log_n(x, base)
          {
            return Math.log(x) / Math.log(base);
          }
    
          function mix(a, b, amount)
          {
            return ((1.0 - amount) * a) + (amount * b);
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
            var x = null;
            var y = null;
    
            var axes = e.currentTarget.parentElement;
            var data = JSON.parse(axes.querySelector("toyplot\\:axes").textContent);
    
            point = d3_mousePoint(e.target, e);
    
            for(var i = 0; i != data["x"].length; ++i)
            {
              var segment = data["x"][i];
              if(segment.range.min <= point[0] && point[0] < segment.range.max)
              {
                var normalized = (point[0] - segment.range.min) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  x = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  x = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            for(var i = 0; i != data["y"].length; ++i)
            {
              var segment = data["y"][i];
              if(segment.range.min <= point[1] && point[1] < segment.range.max)
              {
                var normalized = (segment.range.max - point[1]) / (segment.range.max - segment.range.min);
                if(segment.scale == "linear")
                {
                  y = Number(mix(segment.domain.min, segment.domain.max, normalized)).toFixed(2);
                }
                else if(segment.scale == "log")
                {
                  y = Number(sign(segment.domain.min) * Math.pow(segment.base, mix(log_n(Math.abs(segment.domain.min), segment.base), log_n(Math.abs(segment.domain.max), segment.base), normalized))).toFixed(2);
                }
              }
            }
    
            if(x !== null && y !== null)
              text = "x=" + x + " y=" + y;
            else if(x !== null)
              text = "x=" + x;
            else if(y !== null)
              text = "y=" + y;
            else
              text = null;
    
            if(text !== null)
            {
              var coordinates = axes.querySelectorAll(".toyplot-coordinates");
              for(var i = 0; i != coordinates.length; ++i)
              {
                coordinates[i].style.visibility = "visible";
                coordinates[i].querySelector("text").textContent = text;
              }
            }
          }
    
          function clear_coordinates(e)
          {
            var axes = e.currentTarget.parentElement;
            var coordinates = axes.querySelectorAll(".toyplot-coordinates");
            for(var i = 0; i != coordinates.length; ++i)
              coordinates[i].style.visibility = "hidden";
          }
    
          var axes = document.querySelectorAll("#" + root_id + " .toyplot-Axes2D .toyplot-coordinate-events");
          for(var i = 0; i != axes.length; ++i)
          {
            axes[i].onmousemove = display_coordinates;
            axes[i].onmouseout = clear_coordinates;
          }
        })();
        </script></div></div>


