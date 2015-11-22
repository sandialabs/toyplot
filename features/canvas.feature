Feature: Canvas
  Scenario Outline: Canvas layouts
    When adding axes to a canvas, they can be positioned using <layout>.

    Examples:
      | layout                                    |
      | the default layout                        |
      | explicit bounds                           |
      | grid layout                               |
      | corner layout                             |
      | rect layout                               |

