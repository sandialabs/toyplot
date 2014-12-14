Feature: Table axes
  Scenario Outline: Table axes API
    Given a sample toyplot.data.Table
    And an instance of toyplot.axes.Table
    Then the table can be rendered <phrase>

    Examples:
      | phrase                                 |
      | with defaults                          |
      | with header styles                     |
      | with column styles                     |
      | with row styles                        |
      | with cell styles                       |
      | and row styles override column styles  |
      | and cell styles override row styles    |
      | and cell styles override column styles |
      | with extra horizontal lines            |
      | with extra vertical lines              |
      | with a full grid                       |
      | with grid styles                       |
      | with doubled lines                     |
      | with custom doubled line separation    |
      | with column offsets                    |
      | with custom header content             |
      | with custom cell content               |
      | with embedded plots                    |
      | with custom column widths              |
      | with left justification                |
      | with center justification              |
      | with right justification               |
      | with a title                           |

