Feature: Color conversion
  Scenario Outline: Conversion from css
    When toyplot.color.css receives <input>
    Then toyplot.color.css should return <output>

    Examples: Valid Inputs
      | input                    | output                          |
      | red                      | (1, 0, 0, 1)                    |
      | Red                      | (1, 0, 0, 1)                    |
      | RED                      | (1, 0, 0, 1)                    |
      | aqua                     | (0, 1, 1, 1)                    |
      | ivory                    | (1, 1, 240/255, 1)              |
      | transparent              | (0, 0, 0, 0)                    |
      | #f0f                     | (1, 0, 1, 1)                    |
      | #F0F                     | (1, 0, 1, 1)                    |
      | #F8F                     | (1, 8/15, 1, 1)                 |
      | #ff00ff                  | (1, 0, 1, 1)                    |
      | #FF00ff                  | (1, 0, 1, 1)                    |
      | #FF88ff                  | (1, 8/15, 1, 1)                 |
      | rgb(255, 128, 3)         | (255/255, 128/255, 3/255, 1)    |
      | rgb(76%, 32%, 89%)       | (.76, .32, .89, 1)              |
      | rgba(255, 128, 3, 0.45)  | (255/255, 128/255, 3/255, 0.45) |
      | rgba(76%, 32%, 89%, .76) | (.76, .32, .89, .76)            |
      | hsl(0, 100%, 50%)        | (1, 0, 0, 1)                    |
      | hsla(0, 100%, 50%, 0.32) | (1, 0, 0, 0.32)                 |

    Examples: Invalid Inputs
      | input                    | output                          |
      | baloney                  | None                            |

  Scenario Outline: Conversion to css
    When toyplot.color.to_css receives <input>
    Then toyplot.color.to_css should return <output>

    Examples: Valid Inputs
      | input                            | output                  |
      | toyplot.color.rgba(1, .5, .4, 1) | rgba(100%,50%,40%,1)    |
