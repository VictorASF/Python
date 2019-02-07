import datetime

hoje = datetime.datetime.now()

print('Data Atual: {}'.format(hoje))
print('Dia: {}'.format(hoje.day))
print('Minutos: {}'.format(hoje.minute))

soma = datetime.timedelta(days=1)
novohoje = hoje + (soma*1.8)

print('Nova Data: {}'.format(hoje))
print('Diferença: {}'.format(novohoje-hoje))



