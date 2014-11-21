Feature: Column formatters
  Scenario Outline: Default formatter
    Given an instance of toyplot.format.DefaultFormatter
    Then formatting <input> with the toyplot.format.DefaultFormatter should produce valid output

    Examples:
      | input                             |
      | strings                           |
      | integers                          |

  Scenario Outline: Float formatter
    Given an instance of toyplot.format.FloatFormatter
    Then formatting <input> with the toyplot.format.FloatFormatter should produce valid output

    Examples:
      | input                             |
      | floats                            |
      | mixed floats and integers         |
      | integers                          |
