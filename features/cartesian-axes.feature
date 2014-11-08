Feature: Cartesian axes
  Scenario Outline: Cartesian axes API
    Given a set of cartesian axes
    And a default plot
    Then the cartesian axes can be rendered <phrase>

    Examples:
      | phrase                                                |
      | with defaults                                         |
      | with hidden axes                                      |
      | with axes label                                       |

    Examples: x axis
      | phrase                                                |
      | with hidden x axis                                    |
      | with log-10 x scale                                   |
      | with hidden x spine                                   |
      | with x spine at an explicit position                  |
      | with x spine at the high end of y                     |
      | with styled x spine                                   |
      | with visible x ticks                                  |
      | with sized x ticks                                    |
      | with styled x ticks                                   |
      | with x ticks controlled by a locator                  |
      | with x axis per-tick styles identified by index       |
      | with x axis per-tick styles identified by value       |
      | with hidden x tick labels                             |
      | with angled x tick labels                             |
      | with styled x tick labels                             |
      | with x axis per-tick-label styles identified by index |
      | with x axis per-tick-label styles identified by value |
      | with x axis label                                     |
      | with explicit x axis domain                           |

    Examples: y axis
      | phrase                                                |
      | with hidden y axis                                    |
      | with log-10 y scale                                   |
      | with hidden y spine                                   |
      | with y spine at an explicit position                  |
      | with y spine at the high end of x                     |
      | with styled y spine                                   |
      | with visible y ticks                                  |
      | with sized y ticks                                    |
      | with styled y ticks                                   |
      | with y ticks controlled by a locator                  |
      | with y axis per-tick styles identified by index       |
      | with y axis per-tick styles identified by value       |
      | with hidden y tick labels                             |
      | with angled y tick labels                             |
      | with styled y tick labels                             |
      | with y axis per-tick-label styles identified by index |
      | with y axis per-tick-label styles identified by value |
      | with y axis label                                     |
      | with explicit y axis domain                           |

