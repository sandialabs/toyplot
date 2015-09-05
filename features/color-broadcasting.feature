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
        Then <mark> can be rendered with <color>

        Examples:
            | mark                         | color                                                |
            | bars                         | default colors                                       |
            | bars                         | one explicit color                                   |
            | bars                         | per-series explicit colors                           |
            | bars                         | per-datum explicit colors                            |
            | bars                         | palette colors                                       |
            | bars                         | colormap colors                                      |
            | bars                         | value colors                                         |
            | bars                         | value + palette colors                               |
            | bars                         | value + colormap colors                              |
            | hlines                       | default colors                                       |
            | hlines                       | palette colors                                       |
            | hlines                       | colormap colors                                      |
            | hlines                       | value colors                                         |
            | hlines                       | value + palette colors                               |
            | hlines                       | value + colormap colors                              |
            | vlines                       | default colors                                       |
            | vlines                       | palette colors                                       |
            | vlines                       | colormap colors                                      |
            | vlines                       | value colors                                         |
            | vlines                       | value + palette colors                               |
            | vlines                       | value + colormap colors                              |
