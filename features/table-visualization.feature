Feature: Table axes
    Scenario Outline: Table axes API
        Given a default canvas
        And a sample toyplot.data.Table
        And an instance of toyplot.coordinates.Table
        Then the table can be rendered <phrase>
        And the figure should match the <reference> reference image

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
        Then an instance of toyplot.coordinates.Table can be rendered without a header
        And the figure should match the table-without-header reference image

    Scenario: Render table using convenience API
        Given a default canvas
        And a sample toyplot.data.Table
        Then the table can be rendered using the convenience API
        And the figure should match the table-convenience-api reference image

    Scenario: Render table containing null values
        Given a default canvas
        And a sample toyplot.data.Table containing null values
        And an instance of toyplot.coordinates.Table
        Then the figure should match the table-nulls reference image

    Scenario Outline: Render table without data
        Given a default canvas
        And an instance of toyplot.coordinates.Table with <dimensions>
        Then the figure should match the <reference> reference image

        Examples:
            | dimensions | reference |
            | 4 rows and 3 columns | table-four-rows-three-columns |

    Scenario Outline: Table merging
        Given a default canvas
        And an instance of toyplot.coordinates.Table with every region enabled
        And every grid line is enabled
        And every region is colored
        And <region> <selection> is merged
        Then the figure should match the <reference> reference image

        Examples:
            | region   | selection | reference                 |
            | cells    | 0,2,0,2   | table-merge-cells-0-2-0-2 |
            | cells    | 2,4,2,4   | table-merge-cells-2-4-2-4 |
            | cells    | 6,8,6,8   | table-merge-cells-6-8-6-8 |
            | top-left | 0,3,0,3   | table-merge-top-left-0-3-0-3 |


    Scenario Outline: Table deletion
        Given a default canvas
        And an instance of toyplot.coordinates.Table with every region enabled
        And every grid line is enabled
        And <selection> is deleted
        And every region is colored
        Then the figure should match the <reference> reference image

        Examples:
            | selection | reference |
            | the first row | table-delete-first-row |
            | a middle row | table-delete-middle-row |
            | the last row | table-delete-last-row |
            | the first column | table-delete-first-column |
            | a middle column | table-delete-middle-column |
            | the last column | table-delete-last-column |

    Scenario Outline: Table insertion
        Given a default canvas
        And an instance of toyplot.coordinates.Table with every region enabled
        And every grid line is enabled
        And every region is colored
        And a <region> <celltype> is inserted <position> <selection>
        Then the figure should match the <reference> reference image

        Examples:
            | region | celltype | position  | selection | reference                        |
            | top    | row      | before    | 0         | table-insert-top-row-before-0    |
            | top    | row      | after     | 2         | table-insert-top-row-after-2     |
            | body   | row      | before    | 0         | table-insert-body-row-before-0   |
            | body   | row      | after     | 2         | table-insert-body-row-after-2    |
            | bottom | row      | before    | 0         | table-insert-bottom-row-before-0   |
            | bottom | row      | after     | 2         | table-insert-bottom-row-after-2    |

            | left   | column      | before    | 0         | table-insert-left-column-before-0    |
            | left   | column      | after     | 2         | table-insert-left-column-after-2     |
            | body   | column      | before    | 0         | table-insert-body-column-before-0   |
            | body   | column      | after     | 2         | table-insert-body-column-after-2    |
            | right  | column      | before    | 0         | table-insert-right-column-before-0   |
            | right  | column      | after     | 2         | table-insert-right-column-after-2    |
