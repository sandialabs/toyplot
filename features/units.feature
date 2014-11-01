Feature: Unit conversion
  Scenario Outline: Conversion to points
    When toyplot.units.points receives <input>
    Then toyplot.units.points should <result>

    Examples: Valid Inputs
      | input     | result           |
      | 72        | return 72        |
      | .5 inch   | return 36        |

    Examples: Invalid Inputs
      | input     | result           |
      | string    | raise ValueError |
      | 1 furlong | raise ValueError |

