from datetime import datetime
n1 = int(input('Insira sua idade: '))
now = datetime.now()

if n1>18:
    print('O ano do alistamento passou você devia ter se alistado em {}'.format(now.year-(n1-18)))
elif n1<18:
    print('O ano de alistamento ainda está por vir, você deve comparecer na junta militar em {}'.format(now.year+(18-n1)))
else:
    print('O ano de alistamento é esse, corra para junta militar mais proxima')