d1 = {'Corsa':(26000,2016),'Astra':(30000,2010),'Civic':(60000,2017)}
while True:
    a = str(input('Insira o nome do carro: '))
    a = a.strip()
    a = a.capitalize()
    if a == '':
        break
    if d1.get(a):
        print('{} - Valor: {} - Ano: {}'.format(a,d1[a][0],d1[a][1]))
    else:
        print('O carro não existe nessa loja ')