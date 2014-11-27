Feature: Log scale axes
  Scenario Outline: Log scale axes
    Given <data>
    And <axes>
    And plotting x, x with markers
    Then the result should be <result>

    Examples:
      | data                             | axes                   | result                                        |
      | values from -1000 to -1          | log 10 axes on x and y | a log-log plot from -1000 to -1               |
      | values from -1000 to -0.01       | log 10 axes on x and y | a log-log plot from -1000 to -0.01            |
      | values from -1000 to 0           | log 10 axes on x and y | a log-log plot from -1000 to 0                |
      | values from -1000 to 0.5         | log 10 axes on x and y | a log-log plot from -1000 to 0.5              |
      | values from 0 to 1000            | log 10 axes on x and y | a log-log plot from 0 to 1000                 |
      | values from 0.01 to 1000         | log 10 axes on x and y | a log-log plot from 0.01 to 1000              |
      | values from 1 to 1000            | log 10 axes on x and y | a log-log plot from 1 to 1000                 |
      | values from -0.5 to 1000         | log 10 axes on x and y | a log-log plot from -0.5 to 1000              |
      | values from -1000 to 1000        | log 10 axes on x and y | a log-log plot from -1000 to 1000             |
      | values from -1000 to -1          | log 2 axes on x and y  | a base 2 log-log plot from -1000 to -1        |
      | values from 1 to 1000            | log 2 axes on x and y  | a base 2 log-log plot from 1 to 1000          |
      | values from -1000 to 1000        | log 2 axes on x and y  | a base 2 log-log plot from -1000 to 1000      |
