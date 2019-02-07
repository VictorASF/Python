maior = 0
menor = 99999999999999999
for a in range (1,6):
    n1 = float(input('Digite o peso: '))
    if maior<n1:
        maior=n1
    elif n1<menor:
        menor=n1
print('''Maior peso: {}Kg
Menor peso: {}Kg'''.format(maior, menor))