Feature: Column formatters
  Scenario Outline: Basic formatter
    Given an instance of toyplot.format.BasicFormatter
    Then formatting <input> should produce <output>

    Examples:
      | input      | output               |
      | "foo"      | ("foo","","")        |
      | 3          | ("3","","")       |
      | 3.4        | ("3.4","","")     |
      | numpy.nan  | ("nan","","")        |

  Scenario Outline: Basic formatter with nanshow off
    Given an instance of toyplot.format.BasicFormatter with nanshow off
    Then formatting <input> should produce <output>

    Examples:
      | input      | output               |
      | "foo"      | ("foo","","")        |
      | 3          | ("3","","")       |
      | 3.4        | ("3.4","","")     |
      | numpy.nan  | ("","","")        |

  Scenario Outline: Float formatter
    Given an instance of toyplot.format.FloatFormatter
    Then formatting <input> should produce <output>

    Examples:
      | input      | output               |
      | "foo"      | ("foo","","")        |
      | 3          | ("3","","")       |
      | 3.4        | ("3",".","4")     |
      | numpy.nan  | ("nan","","")        |

  Scenario Outline: Unit formatter
    Given an instance of toyplot.format.UnitFormatter using "inches"
    Then formatting <input> should produce <output>

    Examples:
      | input      | output               |
      | "foo"      | ("foo","","")        |
      | 3          | ("3 in","","")       |
      | 3.4        | ("3",".","4 in")     |
      | numpy.nan  | ("nan","","")        |

  Scenario Outline: Canadian currency formatter
    Given an instance of toyplot.format.CurrencyFormatter using "cad"
    Then formatting <input> should produce <output>

    Examples:
      | input      | output               |
      | "foo"      | ("foo","","")        |
      | 3          | ("$3",".","00")       |
      | 3.4        | ("$3",".","40")     |
      | numpy.nan  | ("nan","","")        |

  Scenario Outline: Euro currency formatter
    Given an instance of toyplot.format.CurrencyFormatter using "eur"
    Then formatting <input> should produce <output>

    Examples:
      | input      | output               |
      | "foo"      | ("foo","","")        |
      | 3          | (u"\u20ac3",".","00")       |
      | 3.4        | (u"\u20ac3",".","40")     |
      | 9000.56    | (u"\u20ac9,000",".","56")     |
      | numpy.nan  | ("nan","","")        |

  Scenario Outline: Pound sterling currency formatter
    Given an instance of toyplot.format.CurrencyFormatter using "gbp"
    Then formatting <input> should produce <output>

    Examples:
      | input      | output               |
      | "foo"      | ("foo","","")        |
      | 3          | (u"\u00a33",".","00")       |
      | 3.4        | (u"\u00a33",".","40")     |
      | 23423410.5 | (u"\u00a323,423,410",".","50")     |
      | numpy.nan  | ("nan","","")        |
