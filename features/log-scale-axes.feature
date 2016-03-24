Feature: Log scale axes
    Scenario Outline: Log scale axes
        Given <data>
        And a default canvas
        And <axes>
        When plotting x, x with markers
        Then the generated figure will match <reference>

        Examples:
            | data                             | axes                   | reference                                        |
            | values from -1000 to -1          | log 10 axes on x and y | axes-log-scale-negative-1000-negative-1               |
            | values from -1000 to -0.01       | log 10 axes on x and y | axes-log-scale-negative-1000-negative-0.01            |
            | values from -1000 to 0           | log 10 axes on x and y | axes-log-scale-negative-1000-zero                |
            | values from -1000 to 0.5         | log 10 axes on x and y | axes-log-scale-negative-1000-0.5              |
            | values from 0 to 1000            | log 10 axes on x and y | axes-log-scale-zero-1000                 |
            | values from 0.01 to 1000         | log 10 axes on x and y | axes-log-scale-0.01-1000              |
            | values from 1 to 1000            | log 10 axes on x and y | axes-log-scale-1-1000                 |
            | values from -0.5 to 1000         | log 10 axes on x and y | axes-log-scale-negative-0.5-1000              |
            | values from -1000 to 1000        | log 10 axes on x and y | axes-log-scale-negative-1000-1000             |
            | values from -1000 to -1          | log 2 axes on x and y  | axes-log-2-scale-negative-1000-negative-1        |
            | values from 1 to 1000            | log 2 axes on x and y  | axes-log-2-scale-1-1000          |
            | values from -1000 to 1000        | log 2 axes on x and y  | axes-log-2-scale-negative-1000-1000      |
            | values from -1000 to 1000        | log 10 axes on x and y with custom format | axes-log-10-scale-negative-1000-1000-custom-format |


    Scenario Outline: Log scale axes with restricted domain
        Given <data>
        And a default canvas
        And <axes>
        When plotting the values with bars
        Then the generated figure will match <reference>

        Examples:
            | data                             | axes                                 | reference                                               |
            | squared values from 0 to 10      | log 10 axes on y with domain min 10  | axes-log-10-scale-0-100-domain-min-10                   |
            | squared values from -10 to 0     | log 10 axes on y with domain max -10 | axes-log-10-scale-negative-100-0-domain-max-negative-10 |

