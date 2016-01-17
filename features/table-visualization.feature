Feature: Table axes
    Scenario Outline: Table axes API
        Given a default canvas
        And a sample toyplot.data.Table
        And an instance of toyplot.axes.Table
        Then the table can be rendered <phrase>
        And the visualization should match the <reference> reference image

        Examples:
            | phrase                                 | reference |
            | with defaults                          | table-defaults |
            | with header styles                     | table-header-style |
            | with column styles                     | table-column-style |
            | with row styles                        | table-row-style |
            | with cell styles                       | table-cell-style |
            | and row styles override column styles  | table-column-row-style |
            | and cell styles override row styles    | table-row-cell-style |
            | and cell styles override column styles | table-column-cell-style |
            | with extra horizontal lines            | table-hlines |
            | with extra vertical lines              | table-vlines |
            | with a full grid                       | table-full-grid |
            | with grid styles                       | table-grid-styles |
            | with doubled lines                     | table-doubled-lines |
            | with custom doubled line separation    | table-doubled-line-separation |
            | with column offsets                    | table-column-offsets |
            | with custom header content             | table-header-content |
            | with custom cell content               | table-cell-content |
            | with embedded plots                    | table-embedded-plots |
            | with custom column widths              | table-custom-column-widths |
            | with left justification                | table-left-justification |
            | with center justification              | table-center-justification |
            | with right justification               | table-right-justification |
            | with a label                           | table-label |
            | with multiple embedded axes in merged cells | table-multiple-axes |
            | with real world units                  | table-units |

    Scenario: Render table without header
        Given a default canvas
        And a sample toyplot.data.Table
        Then an instance of toyplot.axes.Table can be rendered without a header
        And the visualization should match the table-without-header reference image

    Scenario: Render table using convenience API
        Given a default canvas
        And a sample toyplot.data.Table
        Then the table can be rendered using the convenience API
        And the visualization should match the table-convenience-api reference image

    Scenario: Render table containing null values
        Given a default canvas
        And a sample toyplot.data.Table containing null values
        And an instance of toyplot.axes.Table
        Then the visualization should match the table-nulls reference image

    Scenario Outline: Render table without data
        Given a default canvas
        And an instance of toyplot.axes.Table with <dimensions>
        Then the visualization should match the <reference> reference image

        Examples:
            | dimensions | reference |
            | 4 rows and 3 columns | table-four-rows-three-columns |
