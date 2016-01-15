Feature: Cartesian axes
    Scenario Outline: Cartesian axes API
        Given a set of cartesian axes
        And a sample plot
        Then the cartesian axes can be rendered <phrase>
        And the generated figure will match <reference>

    Examples:
        | phrase                                                | reference        |
        | with defaults                                         | axes-cartesian-defaults |
        | with hidden axes                                      | axes-cartesian-show |
        | with axes label                                       | axes-cartesian-label |

    Examples: x axis
        | phrase                                                | reference        |
        | with hidden x axis                                    | axes-cartesian-x-show |
        | with log-10 x scale                                   | axes-cartesian-x-scale |
        | with hidden x spine                                   | axes-cartesian-x-spine-show |
        | with x spine at an explicit position                  | axes-cartesian-x-spine-position |
        | with x spine at the high end of y                     | axes-cartesian-x-spine-position-high |
        | with styled x spine                                   | axes-cartesian-x-spine-style |
        | with visible x ticks                                  | axes-cartesian-x-ticks-show |
        | with sized x ticks                                    | axes-cartesian-x-ticks-sized |
        | with styled x ticks                                   | axes-cartesian-x-ticks-style |
        | with x ticks controlled by a locator                  | axes-cartesian-x-ticks-locator |
        | with x axis per-tick styles identified by index       | axes-cartesian-x-ticks-tick-index-style |
        | with x axis per-tick styles identified by value       | axes-cartesian-x-ticks-tick-value-style |
        | with hidden x tick labels                             | axes-cartesian-x-ticks-labels-show |
        | with angled x tick labels                             | axes-cartesian-x-ticks-labels-angle |
        | with styled x tick labels                             | axes-cartesian-x-ticks-labels-style |
        | with x axis per-tick-label styles identified by index | axes-cartesian-x-ticks-labels-label-index-style |
        | with x axis per-tick-label styles identified by value | axes-cartesian-x-ticks-labels-label-value-style |
        | with x axis label                                     | axes-cartesian-x-label |
        | with explicit x axis domain                           | axes-cartesian-x-domain |

    Examples: y axis
        | phrase                                                | reference    |
        | with hidden y axis                                    | axes-cartesian-y-show  |
        | with log-10 y scale                                   | axes-cartesian-y-scale |
        | with hidden y spine                                   | axes-cartesian-y-spine-show |
        | with y spine at an explicit position                  | axes-cartesian-y-spine-position |
        | with y spine at the high end of x                     | axes-cartesian-y-spine-position-high |
        | with styled y spine                                   | axes-cartesian-y-spine-style |
        | with visible y ticks                                  | axes-cartesian-y-ticks-show |
        | with sized y ticks                                    | axes-cartesian-y-ticks-sized |
        | with styled y ticks                                   | axes-cartesian-y-ticks-style |
        | with y ticks controlled by a locator                  | axes-cartesian-y-ticks-locator |
        | with y axis per-tick styles identified by index       | axes-cartesian-y-ticks-tick-index-style |
        | with y axis per-tick styles identified by value       | axes-cartesian-y-ticks-tick-value-style |
        | with hidden y tick labels                             | axes-cartesian-y-ticks-labels-show |
        | with angled y tick labels                             | axes-cartesian-y-ticks-labels-angle |
        | with styled y tick labels                             | axes-cartesian-y-ticks-labels-style |
        | with y axis per-tick-label styles identified by index | axes-cartesian-y-ticks-labels-label-index-style |
        | with y axis per-tick-label styles identified by value | axes-cartesian-y-ticks-labels-label-value-style |
        | with y axis label                                     | axes-cartesian-y-label |
        | with explicit y axis domain                           | axes-cartesian-y-domain |

    Scenario: Shared axis
        Given a set of cartesian axes
        And a sample plot
        And a shared axis
        Then the generated figure will match axes-cartesian-shared-x-axis

