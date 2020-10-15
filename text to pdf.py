from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size=15)

f = open("input.txt", "r") # change the input.pdf to your file name

for x in f:
	pdf.cell(200, 10, txt=x, ln=1, align='C')

pdf.output("input.pdf") # change the name that u want as output name

