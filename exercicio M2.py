d1 = {}

while True:
    a = str(input('Insira o numero do apartamento: '))
    b = str(input('Nome do proprietario: '))
    b = b.strip()
    b = b.capitalize()
    if a!= '' and b != '':
        d1[int(a)] = b
    else:
        break

print(f'\nDicionario: {d1}')
print('\nApartamento do predio')
for chave,valor in d1.items():
    print(f'Numero:{chave} -- Proprietario: {valor}')
