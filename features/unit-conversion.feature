Feature: Unit conversion
  Scenario Outline: General unit conversion
    When converting <input> to <target> the result should be <response>

    Examples:
      | input                         | target        | response         |
      | 72 without default units      | points        | raise ValueError |
      | 72 with default units pt      | in            | return 1.0       |
      | 72pt                          | in            | return 1.0       |
      | (72, pt)                      | in            | return 1.0       |
      | 96px                          | in            | return 1.0       |
      | 96px                          | pt            | return 72.0      |
      | .5in                          | pt            | return 36.0      |
      | 1in                           | cm            | return 2.54      |
      | 1 furlong                     | in            | raise ValueError |
