Feature: Video
    Scenario: Animation frame
        When an animation frame is created, its fields are populated correctly.

    Scenario: Canvas frame
        When a canvas is used to create an animation frame, its fields are populated correctly.

    Scenario Outline: Render animated canvas
        Given that the <backend> backend is available
        And an animated canvas
        Then the canvas can be rendered as <format>

        Examples:
            | backend            | format       |
            | toyplot.png        | png frames   |
            | toyplot.mp4        | mp4 video    |

