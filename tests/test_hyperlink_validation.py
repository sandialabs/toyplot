import unittest
from toyplot.require import hyperlink

class TestHyperlinkValidation(unittest.TestCase):
    def test_safe_schemes(self):
        self.assertEqual(hyperlink("http://example.com"), "http://example.com")
        self.assertEqual(hyperlink("https://example.com"), "https://example.com")
        self.assertEqual(hyperlink("mailto:user@example.com"), "mailto:user@example.com")
        self.assertEqual(hyperlink("ftp://example.com"), "ftp://example.com")
        self.assertEqual(hyperlink("/relative/path"), "/relative/path")
        self.assertEqual(hyperlink("example.com"), "example.com")
        self.assertEqual(hyperlink(None), None)
        self.assertEqual(hyperlink(""), "")

    def test_unsafe_schemes(self):
        for url in [
            "javascript:alert(1)",
            "data:text/html;base64,SGVsbG8sIFdvcmxkIQ==",
            "vbscript:msgbox('hi')",
            "file:///etc/passwd",
        ]:
            with self.assertRaises(ValueError, msg=f"Should reject: {url}"):
                hyperlink(url)
