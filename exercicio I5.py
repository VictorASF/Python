n = 0
soma = 0
for a in range (1,7):
    n = int(input('Insira um numero {}: '.format(a)))

    if n%2==0:
        soma = soma + n
print('Soma dos numeros pares: {}'.format(soma))
