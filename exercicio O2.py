
arq = open('carros.txt', 'w')

while True:
    a = str(input('Nome do carro: ').strip().capitalize())
    if a != '':
        arq.write(a + '\n')
    else:
        break
print('Exibindo os carros')
print('-'*30)
arq.close()
arq = open('carros.txt', 'r')
for linha in arq:
    print(linha)
print('-'*30)
arq.close()
