# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

import subprocess

markup = "The answer is: $E=\\frac{m_1v^2}{2}$"

markup_tex = """
    \documentclass{standalone}
    \\begin{document}
    %s
    \end{document}
""" % markup
print markup


# Produces texput.pdf, a PDF file that references external fonts.
render = subprocess.Popen(["pdflatex"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = render.communicate(markup_tex)
if render.returncode:
    print stdout, stderr

# Embed fonts by converting text to outlines.
embed = subprocess.Popen(["gs", "-dNoOutputFonts", "-sDEVICE=pdfwrite", "-o", "-", "texput.pdf"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = embed.communicate()
if embed.returncode:
    print stdout, stderr

# Convert the result to a gnuplot metafile we can use for drawing.
convert = subprocess.Popen(["pstoedit", "-f", "gmfa", "-"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = convert.communicate(stdout)
if convert.returncode:
    print stdout, stderr

print stdout

