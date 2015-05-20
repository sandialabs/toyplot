Feature: Projection
  Scenario Outline: Round trip projection
    Given A <type> projection with <domain> and <range>
    Then <value> should project to <projection>

    Examples:
      | type       | domain    | range    | value      | projection |
      | linear     | 0, 1      | 0, 100   | 0          | 0          |
      | linear     | 0, 1      | 0, 100   | 0.5        | 50         |
      | linear     | 0, 1      | 0, 100   | 1          | 100        |
      | log10      | 1, 100    | 0, 100   | 1          | 0          |
      | log10      | 1, 100    | 0, 100   | 10         | 50         |
      | log10      | 1, 100    | 0, 100   | 100        | 100        |
      | log10      | -100, 100 | 0, 100   | -100       | 0          |
      | log10      | -100, 100 | 0, 100   | 0          | 50         |
      | log10      | -100, 100 | 0, 100   | 100        | 100        |
