Feature: Unit conversion
  Scenario Outline: General unit conversion
    When converting <input> to <target> the response should be <response>

    Examples:
      | input                         | target        | response         |
      | "0" without default units     | points        | 0.0              |
      | 0 without default units       | points        | 0.0              |
      | 72 without default units      | points        | raise ValueError |
      | 72 with default units pt      | in            | 1.0              |
      | "72pt"                        | in            | 1.0              |
      | (72, "pt")                    | in            | 1.0              |
      | "100%" without reference      | in            | raise ValueError |
      | "100%" with reference 1.0     | in            | 1.0              |
      | "40%" with reference 1.0      | in            | 0.4              |
      | "96px"                        | in            | 1.0              |
      | "96px"                        | pt            | 72.0             |
      | ".5in"                        | pt            | 36.0             |
      | "1in"                         | cm            | 2.54             |
      | "1furlong"                    | in            | raise ValueError |
      | ("72pt",)                     | in            | raise ValueError |
      | "1in"                         | furlong       | raise ValueError |
