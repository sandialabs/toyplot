Feature: Video output
  Scenario Outline: Render animated canvas
    Given that the <backend> backend is available
    And an animated canvas
    Then the canvas can be rendered as <format>

    Examples:
      | backend            | format       |
      | toyplot.png        | png frames   |
      | toyplot.mp4        | mp4 video    |

