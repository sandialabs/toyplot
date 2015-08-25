Feature: Video output
  Scenario Outline: Render animated canvas
    Given that the <backend> backend is available
    And an animated canvas
    Then the canvas can be rendered as <format> video

    Examples:
      | backend            | format |
      | toyplot.mp4        | mp4    |
      | toyplot.webm       | webm   |

