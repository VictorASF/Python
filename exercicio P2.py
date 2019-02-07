from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
while True:

    carro = str(input('Nome do carro: ').strip())
    if carro == '':
        break
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 20, carro, 0, 1, 'C')
pdf.output('Carros.pdf', 'F')