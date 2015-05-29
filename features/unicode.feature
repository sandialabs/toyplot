Feature: Unicode
  Scenario Outline: Unicode text
    Given a default canvas
    When creating a plot with unicode text in <location>, the plot will match <reference>

    Examples:
      | location                                 | reference                       |
      | a cartesian axes x label                 | unicode-cartesian-x-label       |
      | a cartesian axes y label                 | unicode-cartesian-y-label       |
      | a cartesian axes label                   | unicode-cartesian-label         |
      | a cartesian axes tick labels             | unicode-cartesian-tick-labels   |
      | a cartesian axes text mark               | unicode-cartesian-text          |
      | canvas text                              | unicode-canvas-text             |

