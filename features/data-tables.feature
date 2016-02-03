Feature: Data tables
  Scenario: Data table manipulation
    Given a new toyplot.data.table
    Then the table should be empty
    And adding columns should change the table
    And columns can be retrieved by name
    And partial columns can be retrieved by name and index
    And partial columns can be retrieved by name and slice
    And partial tables can be retrieved by row index
    And partial tables can be retrieved by row slice
    And partial tables can be retrieved by row index and column name
    And partial tables can be retrieved by row slice and column name
    And partial tables can be retrieved by row index and column names
    And partial tables can be retrieved by row slice and column names
    And partial tables can be retrieved by column names
    And partial tables can be retrieved by row indices
    And columns can be replaced by name
    And partial columns can be modified by name and separate index
    And partial columns can be modified by name and separate slice
    And partial columns can be modified by name and index
    And partial columns can be modified by name and slice
    And partial columns can be masked by name and index
    And partial columns can be masked by name and slice
    And deleting columns should change the table
    And new columns must have a string name
    And new columns must have the same number of rows as existing columns
    And new columns must be one-dimensional
    And per-column metadata can be specified
    And the table can be converted to a numpy matrix

  Scenario Outline: Data table creation
    When toyplot.data.Table is initialized with <input>
    Then the toyplot.data.Table <response>

    Examples:
      | input                             | response                                        |
      | nothing                           | is empty                                        |
      | a toyplot.data.Table              | contains the columns                            |
      | an OrderedDict containing columns | contains the columns                            |
      | a dict containing columns         | contains the columns, sorted by key             |
      | a sequence of name, column tuples | contains the columns                            |
      | a matrix                          | contains the matrix columns with generated keys |
      | an array                          | raises ValueError                               |
      | an integer                        | raises ValueError                               |
      | a csv file                        | contains the csv file columns                   |
      | a csv file and conversion         | contains the csv file columns with numeric type |
      | a pandas dataframe                | contains the data frame columns                 |
      | a pandas dataframe with duplicate column names | contains the data frame columns with uniqified column names |

  Scenario Outline: Data table rendering
    Given a toyplot.data.table with some data
    Then the table can be rendered as format <format>

    Examples:
      | format                  |
      | ipython html string     |
