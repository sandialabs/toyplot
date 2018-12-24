Feature: Bar visualization
    Scenario Outline: Bar visualization
        Given a default canvas
        And a set of cartesian axes
        And <scenario>
        Then the figure should match the <reference> reference image

        Examples:
            | scenario              | reference |
            | bars-boundaries-masked-nan | bars-boundaries-masked-nan |
            | bars-histogram | bars-histogram |
            | bars-magnitudes-masked-nan | bars-magnitudes-masked-nan |
            | bars-n-boundaries-along-y | bars-n-boundaries-along-y |
            | bars-n-boundaries-centers | bars-n-boundaries-centers |
            | bars-n-boundaries-edges | bars-n-boundaries-edges |
            | bars-n-boundaries-titles | bars-n-boundaries-titles |
            | bars-n-boundaries | bars-n-boundaries |
            | bars-n-magnitudes-along-y | bars-n-magnitudes-along-y |
            | bars-n-magnitudes-centers | bars-n-magnitudes-centers |
            | bars-n-magnitudes-edges | bars-n-magnitudes-edges |
            | bars-n-magnitudes-symmetric | bars-n-magnitudes-symmetric |
            | bars-n-magnitudes-titles | bars-n-magnitudes-titles |
            | bars-n-magnitudes-wiggle | bars-n-magnitudes-wiggle |
            | bars-n-magnitudes | bars-n-magnitudes |
            | bars-one-boundary-centers | bars-one-boundary-centers |
            | bars-one-boundary-edges | bars-one-boundary-edges |
            | bars-one-boundary | bars-one-boundary |
            | bars-one-magnitude-centers | bars-one-magnitude-centers |
            | bars-one-magnitude-edges | bars-one-magnitude-edges |
            | bars-one-magnitude | bars-one-magnitude |


