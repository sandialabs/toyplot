Feature: Color Broadcasting
    Scenario Outline: Color broadcasting use-cases
        Given a set of cartesian axes
        And a set of diverging series
        And a set of per-series values
        And a set of per-series colors
        And a set of per-datum values
        And a set of per-datum colors
        Then <mark> can be rendered with <color>

        Examples:
            | mark                         | color                                                |
            | bars                         | default colors                                       |
            | bars                         | one explicit color                                   |
            | bars                         | per-series explicit colors                           |
            | bars                         | per-datum explicit colors                            |
            | bars                         | palette colors                                       |
            | bars                         | colormap colors                                      |
            | bars                         | per-series value colors                              |
            | bars                         | per-series value + palette colors                    |
            | bars                         | per-series value + colormap colors                   |
            | bars                         | per-datum value colors                               |
            | bars                         | per-datum value + palette colors                     |
            | bars                         | per-datum value + colormap colors                    |
            | fills                        | default colors                                       |
            | fills                        | one explicit color                                   |
            | fills                        | per-series explicit colors                           |
            | fills                        | palette colors                                       |
            | fills                        | colormap colors                                      |
            | fills                        | per-series value colors                              |
            | fills                        | per-series value + palette colors                    |
            | fills                        | per-series value + colormap colors                   |
            | hlines                       | default colors                                       |
            | hlines                       | one explicit color                                   |
            | hlines                       | per-datum explicit colors                            |
            | hlines                       | palette colors                                       |
            | hlines                       | colormap colors                                      |
            | hlines                       | per-datum value colors                               |
            | hlines                       | per-datum value + palette colors                     |
            | hlines                       | per-datum value + colormap colors                    |
            | plots                        | default colors                                       |
            | plots                        | one explicit color                                   |
            | plots                        | per-series explicit colors                           |
            | plots                        | palette colors                                       |
            | plots                        | colormap colors                                      |
            | plots                        | per-series value colors                              |
            | plots                        | per-series value + palette colors                    |
            | plots                        | per-series value + colormap colors                   |
            | plots                        | default marker colors                                |
            | plots                        | one explicit marker color                            |
            | plots                        | per-series explicit marker colors                    |
            | plots                        | palette marker colors                                |
            | plots                        | colormap marker colors                               |
            | plots                        | per-series value marker colors                       |
            | plots                        | per-series value + palette marker colors             |
            | plots                        | per-series value + colormap marker colors            |
            | plots                        | per-datum value marker colors                        |
            | plots                        | per-datum value + palette marker colors              |
            | plots                        | per-datum value + colormap marker colors             |
            | rects                        | default colors                                       |
            | rects                        | one explicit color                                   |
            | rects                        | per-datum explicit colors                            |
            | rects                        | palette colors                                       |
            | rects                        | colormap colors                                      |
            | rects                        | per-datum value colors                               |
            | rects                        | per-datum value + palette colors                     |
            | rects                        | per-datum value + colormap colors                    |
            | scatterplots                 | default colors                                       |
            | scatterplots                 | one explicit color                                   |
            | scatterplots                 | per-series explicit colors                           |
            | scatterplots                 | per-datum explicit colors                            |
            | scatterplots                 | palette colors                                       |
            | scatterplots                 | colormap colors                                      |
            | scatterplots                 | per-series value colors                              |
            | scatterplots                 | per-series value + palette colors                    |
            | scatterplots                 | per-series value + colormap colors                   |
            | scatterplots                 | per-datum value colors                               |
            | scatterplots                 | per-datum value + palette colors                     |
            | scatterplots                 | per-datum value + colormap colors                    |
            | text                         | default colors                                       |
            | text                         | one explicit color                                   |
            | text                         | per-datum explicit colors                            |
            | text                         | palette colors                                       |
            | text                         | colormap colors                                      |
            | text                         | per-datum value colors                               |
            | text                         | per-datum value + palette colors                     |
            | text                         | per-datum value + colormap colors                    |
            | vlines                       | default colors                                       |
            | vlines                       | one explicit color                                   |
            | vlines                       | per-datum explicit colors                            |
            | vlines                       | palette colors                                       |
            | vlines                       | colormap colors                                      |
            | vlines                       | per-datum value colors                               |
            | vlines                       | per-datum value + palette colors                     |
            | vlines                       | per-datum value + colormap colors                    |

