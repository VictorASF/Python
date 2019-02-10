from fpdf import FPDF
lista=[['HB20 1.0 Confort Plus', 'Hyundai', 2014, 33590],
       ['Allure 1.6 16V', 'Peugeot', 2017, 71990],
       ['Argo Drive 1.6 Firefly', 'Fiat', 2018, 44990],
       ['Corolla Sedan SEG 1.8 16V', 'Toyota', 2010, 44900],
       ['320iA GT Sport 2.0 Turbo 16V', 'BMW', 2014, 167000],
       ['MALIBU LTZ 2.4 16V', 'Chevrolet', 2014, 97265]]
i = 0
pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.set_draw_color(255, 255, 204)
pdf.set_fill_color(255, 255, 204)
pdf.set_text_color(0)
pdf.cell(0, 30, 'Loja - Ronco da Cuica', 1, 1, 'C', 1)
pdf.image('foto.jpg', 10, 10, 30, 30)
pdf.image('foto.jpg', 170, 10, 30, 30)
pdf.set_draw_color(255, 102, 153)
pdf.set_fill_color(255, 102, 153)
pdf.set_text_color(0, 0, 255)
pdf.set_font('Courier', 'B', 14)
pdf.cell(0, 20, '{:<26}   {:<12}   {:<6}   {:<8}'.format('Carro', 'Marca', 'Ano', 'Valor'), 1, 1, '', 1)
pdf.set_font('Courier', '', 12)
for v in lista:
    if i%2 == 0:
        pdf.set_text_color(0)
        pdf.cell(0, 15, '{:<31}   {:<14}   {:<6}    R$ {:.2f}'.format(v[0], v[1], v[2], v[3]), 0, 1, '', 0)
        i += 1
    else:
        pdf.set_text_color(204, 0, 153)
        pdf.cell(0, 15, '{:<31}   {:<14}   {:<6}    R$ {:.2f}'.format(v[0], v[1], v[2], v[3]), 0, 1, '', 0)
        i += 1
pdf.image('motor.jpg',75,230,60)
pdf.output('Loja.pdf', 'F')
