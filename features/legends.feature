Feature: Legends
  Scenario Outline: Render legends
    Given a default canvas
    And a set of cartesian axes
    And <scenario>
    And the marks are used to create a legend
    Then the figure should match the <reference> reference image

    Examples:
      | scenario                                | reference                       |
      | the data is rendered as boundary bars   | legend-boundary-bars               |
      | the data is rendered as magnitude bars  | legend-magnitude-bars               |
      | the data is rendered as boundary fills  | legend-boundary-fills               |
      | the data is rendered as magnitude fills  | legend-magnitude-fills               |
      | the data is rendered as plots           | legend-plots               |
      | the data is rendered as scatterplots    | legend-scatterplots               |

