Feature: Opacity Broadcasting
    Scenario Outline: Opacity broadcasting use-cases
        Given a set of cartesian axes
        And a set of diverging series
        And a set of per-series opacity values
        And a set of per-datum opacity values
        Then <mark> can be rendered with <opacity>

        Examples:
            | mark                         | opacity                                              |
            | hlines                       | one explicit opacity                                 |
            | hlines                       | per-datum opacities                                  |
            | vlines                       | one explicit opacity                                 |
            | vlines                       | per-datum opacities                                  |
