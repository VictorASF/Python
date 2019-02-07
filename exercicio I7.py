from datetime import datetime

now = datetime.now()
maior = 0
menor = 0
for a in range(1, 6):
    n1 = int(input('Ano de nascimento: '))
    if now.year - n1 >= 18:
        maior += 1
    else:
        menor += 1
print('''Maior que 18: {}
Menores que 18: {}'''.format(maior, menor))
