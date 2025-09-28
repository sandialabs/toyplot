import unittest

import toyplot.require as require


class TestHyperlinkValidation(unittest.TestCase):

    def test_hyperlink_accepts_allowed_schemes(self):
        self.assertIsNone(require.hyperlink(None))
        self.assertEqual(require.hyperlink(""), "")
        self.assertEqual(require.hyperlink("/relative/path"), "/relative/path")
        self.assertEqual(require.hyperlink("https://example.com"), "https://example.com")
        self.assertEqual(require.hyperlink("HTTP://EXAMPLE.COM"), "HTTP://EXAMPLE.COM")
        self.assertEqual(require.hyperlink("mailto:user@example.com"), "mailto:user@example.com")
        self.assertEqual(require.hyperlink("ftp://example.com/resource"), "ftp://example.com/resource")

    def test_hyperlink_rejects_disallowed_schemes(self):
        with self.assertRaises(ValueError):
            require.hyperlink("javascript:alert(1)")
        with self.assertRaises(ValueError):
            require.hyperlink("data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0PiIp")
        with self.assertRaises(ValueError):
            require.hyperlink("vbscript:msgbox('hi')")
        with self.assertRaises(ValueError):
            require.hyperlink("  javascript:alert(1)")


if __name__ == "__main__":
    unittest.main()
