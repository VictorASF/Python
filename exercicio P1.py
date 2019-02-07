from fpdf import FPDF
pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font('Arial', '', 16)
pdf.cell(0, 15, 'Vermelho', 0, 1)
pdf.cell(0, 15, 'Verde', 0, 1)
pdf.cell(0, 15, 'Marrom', 0, 1)
pdf.cell(0, 15, 'Laranja', 0, 1)
pdf.output('cores.pdf', 'F')
#
#
#
pdf2 = FPDF('P', 'mm', 'A4')
pdf2.add_page()
pdf2.set_font('Times', 'B', 20)
pdf2.set_text_color(255, 0, 0)
pdf2.cell(0, 15, 'Vermelho', 0, 1)
pdf2.set_font('Arial', 'I', 14)
pdf2.set_text_color(0, 255, 0)
pdf2.cell(0, 15, 'Verde', 0, 1)
pdf2.set_font('Arial', 'U', 12)
pdf2.set_text_color(102, 51, 0)
pdf2.cell(0, 15, 'Marrom', 0, 1)
pdf2.set_font('Times', '', 25)
pdf2.set_text_color(255, 102, 0)
pdf2.cell(0, 15, 'Laranja', 0, 1)
pdf2.output('cores_1.pdf', 'F')
#
#
#
pdf3 = FPDF('P', 'pt', 'Letter')
pdf3.add_page()
pdf3.set_font('Times', 'B', 16)
pdf3.cell(0, 50, 'Vermelho', 0, 1)
pdf3.cell(0, 50, 'Verde', 0, 1)
pdf3.cell(0, 50, 'Azul', 0, 1)
pdf3.cell(0, 50, 'Marrom', 0, 1)
pdf3.cell(0, 50, 'Rosa', 0, 1)
pdf3.cell(0, 50, 'Laranja', 0, 1)
pdf3.output('cores_2.pdf', 'F')


