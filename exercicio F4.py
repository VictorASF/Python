n1 = int(input('Insira a distancia da viagem em Km: '))

if n1<=100:
    print('Sua viagem de {} km custará R$: {:.2f}'.format(n1, n1*0.60))
else:
    print('Sua viagem de {} km custará R$: {:.2f}'.format(n1, n1*0.50))