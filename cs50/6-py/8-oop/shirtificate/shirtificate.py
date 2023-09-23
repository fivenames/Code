from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 48)
pdf.set_auto_page_break(False)

pdf.cell(w=0, h=48, txt='CS50 Shirtificate', align='C')
pdf.image('shirtificate.png', x=10, y=64, w=pdf.epw)
pdf.set_font("helvetica", "B", 32)
pdf.cell(w=-186, h=248, txt='Wuming took CS50', align='C')

pdf.output("shirtificate.pdf")