Feature: Opacity Broadcasting
    Scenario Outline: Opacity broadcasting use-cases
        Given a set of cartesian axes
        And a set of diverging series
        And a set of per-series opacity values
        And a set of per-datum opacity values
        Then <mark> can be rendered with <opacity>

        Examples:
            | mark                         | opacity                                              |
            | bars                         | one explicit opacity                                 |
            | bars                         | per-series opacities                                 |
            | bars                         | per-datum opacities                                  |
            | fills                        | one explicit opacity                                 |
            | fills                        | per-series opacities                                 |
            | hlines                       | one explicit opacity                                 |
            | hlines                       | per-datum opacities                                  |
            | rects                        | one explicit opacity                                 |
            | rects                        | per-datum opacities                                  |
            | text                         | one explicit opacity                                 |
            | text                         | per-datum opacities                                  |
            | vlines                       | one explicit opacity                                 |
            | vlines                       | per-datum opacities                                  |
