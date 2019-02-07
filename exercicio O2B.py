arq = open('carros.txt', 'a')

while True:
    a = str(input('Nome do carro: ').strip().capitalize())
    if a != '':
        arq.writelines('{}\n'.format(a))
    else:
        break
arq.close()
arq = open('carros.txt','r')
print('{:^28}'.format('Carros'))
print('-'*30)
for linha in arq:
    print(linha)
print('-'*30)
arq.close()