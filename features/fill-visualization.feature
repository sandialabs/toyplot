Feature: Fill visualization
    Scenario Outline: Fill visualization
        Given <data>
        When creating a fill plot <details>
        Then the result should be <result>

        Examples:
            | data                         | details                                        | result                                                      |
            | position and boundary data   | with one boundary                              | a fill plot between the boundary and the origin with implicit x      |
            | position and boundary data   | with one boundary and position                 | a fill plot between the boundary and the origin                       |
            | position and boundary data   | with two boundaries and position               | a fill plot between the two boundaries                               |
            | position and boundary data   | with multiple boundaries                       | multiple fill series between the boundaries with implicit x |
            | position and boundary data   | with multiple boundaries and position          | multiple fill series between the boundaries                 |
            | position and boundary data   | with multiple boundaries and position along y  | multiple fill series between the boundaries along y         |
            | position and boundary data   | with multiple boundaries and per-series titles | multiple fill series between the boundaries with titles     |
            | position and magnitude data  | with one magnitude                             | one fill series stacked above the origin with implicit x |
            | position and magnitude data  | with one magnitude and position                | one fill series stacked above the origin           |
            | position and magnitude data  | with multiple magnitudes                       | multiple fill series stacked above the origin with implicit x |
            | position and magnitude data  | with multiple magnitudes and position          | multiple fill series stacked above the origin           |
            | position and magnitude data  | with multiple magnitudes and position along y         | multiple fill series stacked above the origin along y |
            | position and magnitude data  | with multiple magnitudes and per-series titles          | multiple fill series stacked above the origin with titles |
            | position and magnitude data  | with multiple magnitudes and symmetric baseline | multiple fill series stacked with symmetric baseline |
            | position and magnitude data  | with multiple magnitudes and wiggle baseline    | multiple fill series stacked with wiggle baseline |


    Scenario Outline: Sparse fill visualization
        Given a default canvas
        And a set of cartesian axes
        And <scenario>
        Then the figure should match the <reference> reference image

        Examples:
            | scenario              | reference |
            | axes-fill-boundaries-masked-nan | axes-fill-boundaries-masked-nan |
            | axes-fill-magnitudes-masked-nan | axes-fill-magnitudes-masked-nan |
