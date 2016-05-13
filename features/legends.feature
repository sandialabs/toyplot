Feature: Legends
  Scenario Outline: Render legends
    Given a default canvas
    And a set of cartesian axes
    And <data>
    And the data is rendered as <mark>
    And the marks are added to a legend
    And the legend is added to the <target>
    Then the visualization should match the <reference> reference image

    Examples:
      | data                                    | mark       | target    | reference                       |
      | single and multi series data            | bars       | canvas    | legend-canvas-bar               |
      | single and multi series data            | fills       | canvas    | legend-canvas-fill               |
      | single and multi series data            | plots       | canvas    | legend-canvas-plot               |
      | single and multi series data            | scatterplots       | canvas    | legend-canvas-scatterplot               |

