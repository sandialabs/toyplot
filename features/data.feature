Feature: Data Table
  Scenario: Table manipulation
    Given a new toyplot.data.table
    Then adding columns should change the table
    And extracting columns should return a new table
    And deleting columns should change the table
    And indexing should return a new table with one row
    And slicing should return a new table with a range of rows
    And extracting rows by index should return a new table with one row
    And extracting rows using multiple indices should return a new table with the specified rows
    And new columns must have a string name
    And new columns must have the same number of rows as existing columns
    And new columns must be one-dimensional

  Scenario Outline: Table creation
    When toyplot.data.Table is initialized with <input>
    Then the toyplot.data.Table <response>

    Examples: Valid Inputs
      | input                             | response             |
      | nothing                           | is empty             |
      | an OrderedDict containing columns | contains the columns |

    Examples: Invalid Inputs
      | input                             | response             |
      | a dict containing columns         | raises ValueError    |

