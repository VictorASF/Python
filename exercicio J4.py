num = 0
soma = 0
quant = 0
while num != 999:
    num = int(input('Insira o numero: '))
    if num != 999:
        soma += num
        quant += 1
print('A soma total foi {} e a quantidade de numeros digitados foram {}'.format(soma, quant))