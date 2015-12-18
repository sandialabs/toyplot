import xml.etree.ElementTree as xml

equation = "E=\\frac{m_1v^2}{2}"

root = xml.Element(
    "div",
    style="font-family: helvetica; font-size: 14px",
    )

xml.SubElement(
    root,
    "script",
    type="text/javascript",
    src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML",
    )

svg = xml.SubElement(
    root,
    "svg",
    xmlns="http://www.w3.org/2000/svg",
    attrib={"xmlns:toyplot": "http://www.sandia.gov/toyplot"},
    width="400px",
    height="400px",
    viewBox="0 0 400 400",
    preserveAspectRatio="xMidYMid meet",
    )

xml.SubElement(
    svg,
    "circle",
    cx="200",
    cy="200",
    r="2",
    )

fo = xml.SubElement(
    svg,
    "foreignObject",
    x="100",
    y="200",
    width="200",
    height="100",
    )

fo.text = "Displaying \\(%s\\) for your enjoyment." % equation
#fo.text = "$$%s$$" % equation

with open("latex-math-html.html", "wb") as stream:
    stream.write(xml.tostring(root, method="html"))

