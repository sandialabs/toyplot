Feature: Bar visualization
    Scenario Outline: Bar visualization
        Given a default canvas
        And a set of cartesian axes
        And <scenario>
        Then the figure should match the <reference> reference image

        Examples:
            | scenario              | reference |
            | axes-bars-boundaries-masked-nan | axes-bars-boundaries-masked-nan |
            | axes-bars-histogram | axes-bars-histogram |
            | axes-bars-magnitudes-masked-nan | axes-bars-magnitudes-masked-nan |
            | axes-bars-n-boundaries-along-y | axes-bars-n-boundaries-along-y |
            | axes-bars-n-boundaries-centers | axes-bars-n-boundaries-centers |
            | axes-bars-n-boundaries-edges | axes-bars-n-boundaries-edges |
            | axes-bars-n-boundaries-titles | axes-bars-n-boundaries-titles |
            | axes-bars-n-boundaries | axes-bars-n-boundaries |
            | axes-bars-n-magnitudes-along-y | axes-bars-n-magnitudes-along-y |
            | axes-bars-n-magnitudes-centers | axes-bars-n-magnitudes-centers |
            | axes-bars-n-magnitudes-edges | axes-bars-n-magnitudes-edges |
            | axes-bars-n-magnitudes-symmetric | axes-bars-n-magnitudes-symmetric |
            | axes-bars-n-magnitudes-titles | axes-bars-n-magnitudes-titles |
            | axes-bars-n-magnitudes-wiggle | axes-bars-n-magnitudes-wiggle |
            | axes-bars-n-magnitudes | axes-bars-n-magnitudes |
            | axes-bars-one-boundary-centers | axes-bars-one-boundary-centers |
            | axes-bars-one-boundary-edges | axes-bars-one-boundary-edges |
            | axes-bars-one-boundary | axes-bars-one-boundary |
            | axes-bars-one-magnitude-centers | axes-bars-one-magnitude-centers |
            | axes-bars-one-magnitude-edges | axes-bars-one-magnitude-edges |
            | axes-bars-one-magnitude | axes-bars-one-magnitude |
            | bars-one-magnitude | bars-one-magnitude |


