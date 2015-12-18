import xml.etree.ElementTree as xml

markup = "The answer is: \\(E=\\frac{m_1v^2}{2}\\)"
angle = -30
align = None
ashift = None
bshift = -16

def draw_text(parent, markup, ax, ay, angle=None, align=None, ashift=None, bshift=None, twidth=None, theight=None):
    if angle is None:
        angle = 0

    if align is None:
        if angle > 0:
            align = "right"
        elif angle < 0:
            align = "left"
        else:
            align = "center"

    if ashift is None:
        if angle > 0:
            ashift = -10
        elif angle < 0:
            ashift = 10
        else:
            ashift = 0

    if bshift is None:
        bshift = 0

    if twidth is None:
        twidth = 200

    if theight is None:
        theight = 200

    if align == "left":
        x = ax
        y = ay
    elif align == "center":
        x = ax - twidth / 2
        y = ay
    elif align == "right":
        x = ax - twidth
        y = ay

    xml.SubElement(parent, "circle", cx=repr(ax), cy=repr(ay), r="1")

    fo = xml.SubElement(
        parent,
        "foreignObject",
        x=repr(x),
        y=repr(y),
        width=repr(twidth),
        height=repr(theight),
        transform="rotate(%s, %s, %s) translate(%s, %s)" % (-angle, ax, ay, ashift, bshift)
        )

    container = xml.SubElement(
        fo,
        "div",
        xmlns="http://www.w3.org/1999/xhtml",
        style="text-align: %s" % align,
        )

    try:
        container.append(xml.fromstring(markup))
    except:
        container.text = markup


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

draw_text(parent=svg, markup=markup, ax=200, ay=200, angle=angle, align=align, ashift=ashift, bshift=bshift)
draw_text(parent=svg, markup="<p>0.3<br></br><span style='font-size:75%'>(0.8, 0.6, 0.2)</span></p>", ax=200, ay=300)

with open("latex-math-html.html", "wb") as stream:
    stream.write(xml.tostring(root, method="html"))

