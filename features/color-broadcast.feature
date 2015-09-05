Feature: Color broadcasting
#    Scenario Outline: Color broadcasting
#        Given a broadcast color <color>
#        And a broadcast shape <shape>
#        Then toyplot.color.broadcast should return <result>
#
#        Examples: Single values
#            | color                                            | shape                  | result                                  |
#            | "red"                                            | (2)                    | an all-red color array with shape (2)   |
#            | "red"                                            | (2,3)                  | an all-red color array with shape (2,3) |
#            | (1,0,0)                                          | (2)                    | an all-red color array with shape (2)   |
#            | (1,0,0)                                          | (2,3)                  | an all-red color array with shape (2,3) |
#            | (1,0,0,1)                                        | (2)                    | an all-red color array with shape (2)   |
#            | (1,0,0,1)                                        | (2,3)                  | an all-red color array with shape (2,3) |
#            | toyplot.color.rgb(1,0,0)                         | (2)                    | an all-red color array with shape (2)   |
#            | toyplot.color.rgb(1,0,0)                         | (2,3)                  | an all-red color array with shape (2,3) |
#            | toyplot.color.rgba(1,0,0,1)                      | (2)                    | an all-red color array with shape (2)   |
#            | toyplot.color.rgba(1,0,0,1)                      | (2,3)                  | an all-red color array with shape (2,3) |
#
#        Examples: Sequences
#            | color                                            | shape                  | result                                  |
#            | ["red",(0,0,1)]                                  | (2)                    | a red-blue color array with shape (2)   |
#            | ["red",(0,0,1,1)]                                | (2)                    | a red-blue color array with shape (2)   |
#            | ["red",(0,0,1)]                                  | (3,2)                  | a red-blue color array with shape (3,2) |
#            | ["red",(0,0,1,1)]                                | (3,2)                  | a red-blue color array with shape (3,2) |
#
#        Examples: Arrays
#            | color                                            | shape                  | result                                  |
#            | numpy.array(["red","rgb(0,0,255)"])              | (2)                    | a red-blue color array with shape (2)   |
#            | numpy.array(["red","rgb(0,0,255)"])              | (3,2)                  | a red-blue color array with shape (3,2) |
#            | numpy.array(["red","rgba(0,0,255,1)"])           | (2)                    | a red-blue color array with shape (2)   |
#            | numpy.array(["red","rgba(0,0,255,1)"])           | (3,2)                  | a red-blue color array with shape (3,2) |
##        | numpy.array([["red","green"],["blue","yellow"]]) | (2,2)                  | a red-green-blue-yellow color array with shape (2,2) |
#            | numpy.array([1,2,3])                             | (3)                    | a blues color array with shape (3)      |
#            | numpy.array([1,2,3])                             | (2,3)                  | a blues color array with shape (2,3) and identical columns    |
#            | numpy.array([[1,2,3],[4,5,6]])                   | (2,3)                  | a blues color array with shape (2,3)    |
#            | toyplot.color.array([(1,0,0,1),(0,0,1,1)])       | (2)                    | a red-blue color array with shape (2)   |
#            | toyplot.color.array([(1,0,0,1),(0,0,1,1)])       | (3,2)                  | a red-blue color array with shape (3,2) |


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
            | fills                         | default colors                                       |
            | fills                         | one explicit color                                   |
            | fills                         | per-series explicit colors                           |
            | fills                         | palette colors                                       |
            | fills                         | colormap colors                                      |
            | fills                         | per-series value colors                              |
            | fills                         | per-series value + palette colors                    |
            | fills                         | per-series value + colormap colors                   |
            | hlines                         | default colors                                       |
            | hlines                         | one explicit color                                   |
            | hlines                         | per-datum explicit colors                            |
            | hlines                         | palette colors                                       |
            | hlines                         | colormap colors                                      |
            | hlines                         | per-datum value colors                               |
            | hlines                         | per-datum value + palette colors                     |
            | hlines                         | per-datum value + colormap colors                    |
            | vlines                         | default colors                                       |
            | vlines                         | one explicit color                                   |
            | vlines                         | per-datum explicit colors                            |
            | vlines                         | palette colors                                       |
            | vlines                         | colormap colors                                      |
            | vlines                         | per-datum value colors                               |
            | vlines                         | per-datum value + palette colors                     |
            | vlines                         | per-datum value + colormap colors                    |
