Feature: Rendered animations
  Scenario Outline: Render animated canvas
    Given an animated canvas
    When rendering a <format> video
    Then the backend should return a <format> video

    Examples:
      | format |
      | mp4    |
      | webm   |

