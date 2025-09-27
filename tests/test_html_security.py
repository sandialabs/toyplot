import unittest
import xml.etree.ElementTree as xml

import toyplot
import toyplot.html
import toyplot.data
from toyplot.html import RenderContext, _render_javascript  # accessing internal for targeted test


class TestHTMLSecurity(unittest.TestCase):

    def test_script_closing_tag_escaped(self):
        # Create a minimal render context
        root = xml.Element("div")
        context = RenderContext(scenegraph=None, root=root)
        # Simulate a module definition (not strictly necessary, but realistic)
        context.define("toyplot/test/module", value={"k": 1})
        # Inject a javascript call with an argument containing the sentinel sequence
        malicious = "safe prefix </script><script>alert('xss')</script> suffix"
        context.require(
            dependencies=["toyplot/test/module"],
            arguments=[malicious],
            code="""function(mod, arg){ if(!mod.k){ throw new Error('module fail'); } }""",
        )
        # Assign a parent for script injection destination
        context = context.copy(parent=root)
        _render_javascript(context)

        # Extract script content
        scripts = [child.text for child in root.findall("script")]
        self.assertTrue(scripts, "No <script> element generated.")
        combined = "\n".join(scripts)

        # Raw closing sequence must not appear
        self.assertNotIn("</script>", combined, "Unescaped </script> found in script block!")
        # Escaped form should appear
        self.assertIn("<\\/script>", combined, "Escaped </script> not present.")
