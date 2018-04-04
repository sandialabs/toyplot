import toyplot
import nose.tools

def test_float_formatter():
    formatter = toyplot.format.UnitFormatter()
    val = formatter.format(12.2, "inches")
    nose.tools.assert_equal(1, val)

def test_currency_formatter():
    formatter = toyplot.format.CurrencyFormatter(curr="gbp")
    val = formatter.format(23423410.5)
    nose.tools.assert_equal(1, val)
