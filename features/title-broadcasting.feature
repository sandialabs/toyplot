Feature: Title Broadcasting
    Scenario Outline: Title broadcasting use-cases
        Given a set of cartesian axes
        And a set of diverging series
        And a set of per-series title values
        And a set of per-datum title values
        Then <mark> can be rendered with <title>

        Examples:
            | mark                         | title                                              |
            | bars                         | one explicit title                                 |
            | bars                         | per-series titles                                 |
            | bars                         | per-datum titles                                  |
            | fills                        | one explicit title                                 |
            | fills                        | per-series titles                                 |
            | hlines                       | one explicit title                                 |
            | hlines                       | per-datum titles                                  |
            | plots                        | one explicit title                                 |
            | plots                        | per-series titles                                 |
            | rects                        | one explicit title                                 |
            | rects                        | per-datum titles                                  |
            | scatterplots                 | one explicit title                                 |
            | scatterplots                 | per-series titles                                 |
            | scatterplots                 | per-datum titles                                  |
            | text                         | one explicit title                                 |
            | text                         | per-datum titles                                  |
            | vlines                       | one explicit title                                 |
            | vlines                       | per-datum titles                                  |
