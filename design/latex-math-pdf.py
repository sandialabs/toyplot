import pdfrw
import pdfrw.buildxobj
import pdfrw.toreportlab
import reportlab.pdfgen.canvas
import subprocess

equation_tex = """
    \documentclass{standalone}
    \\begin{document}
    $E=\\frac{m_1v^2}{2}$
    \end{document}
"""

pdflatex = subprocess.Popen(["pdflatex"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = pdflatex.communicate(equation_tex)
if pdflatex.returncode:
    print stdout, stderr

canvas = reportlab.pdfgen.canvas.Canvas("latex-math-pdf.pdf")

for page in pdfrw.PdfReader("texput.pdf").pages:
    page = pdfrw.buildxobj.pagexobj(page)

    canvas.saveState()
    canvas.translate(100, 100)
    canvas.doForm(pdfrw.toreportlab.makerl(canvas, page))
    canvas.restoreState()

canvas.showPage()
canvas.save()
