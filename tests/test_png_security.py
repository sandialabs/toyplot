import unittest
import os

try:
    import toyplot.reportlab.png
    GHOSTSCRIPT_AVAILABLE = True
except OSError:
    GHOSTSCRIPT_AVAILABLE = False


@unittest.skipUnless(GHOSTSCRIPT_AVAILABLE, "Ghostscript not available")
class TestPNGSecurity(unittest.TestCase):
    def test_gs_command_absolute_path(self):
        """Test that _gs_command is an absolute path."""
        self.assertIsNotNone(toyplot.reportlab.png._gs_command)
        self.assertTrue(os.path.isabs(toyplot.reportlab.png._gs_command))

    def test_gs_version_parsed(self):
        """Test that _gs_version is set."""
        self.assertIsNotNone(toyplot.reportlab.png._gs_version)


if __name__ == "__main__":
    unittest.main()