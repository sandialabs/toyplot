Feature: Unit conversion
  Scenario Outline: Conversion to points
    When toyplot.units.points receives <input>
    Then toyplot.units.points should <response>

    Examples: Valid Inputs
      | input     | response         |
      | 72        | return 72        |
      | .5 inch   | return 36        |

    Examples: Invalid Inputs
      | input     | response         |
      | string    | raise ValueError |
      | 1 furlong | raise ValueError |

