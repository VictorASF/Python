n1 = int(input('Qual a velocidade do carro em Km/h: '))

if n1>80:
    print('Foi multado otario, agora tu vai pagar {} temers'.format((n1-80)*5))
else:
    print('Passou suave mas na proxima seu dinheiro é meu')