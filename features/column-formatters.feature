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
      | integers                          |

  Scenario Outline: Unit formatter
    Given an instance of toyplot.format.UnitFormatter
    Then formatting <input> with the toyplot.format.UnitFormatter should produce valid output

    Examples:
      | input                             |
      | inch units                        |
      | point units                       |

  Scenario Outline: Currency formatter
    Given an instance of toyplot.format.CurrencyFormatter
    Then formatting <input> with the toyplot.format.CurrencyFormatter should produce valid output

    Examples:
      | input                             |
      | Canadian currency                 |
      | European currency                 |
      | British currency                  |
