import datetime

hora = datetime.time(18, 43, 50)

print('Horario: {}'.format(hora))

dia = datetime.date.today()

print('Dia: {}'.format(dia))

datahora = datetime.datetime.combine(dia, hora)

print('Data e Hora: {}'.format(datahora))
