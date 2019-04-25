import random

meu = [6, 13, 25, 33, 42, 50]

meganum = list(range(1,61))

n = int(input('Numero de testes: '))

soma = 0

for i in range(n):
    sorteado = []

    cont = 0

    while meu != sorteado:
        mega_sort = meganum.copy()

        sorteado = []

        for j in range(6):

            numero = random.choice(mega_sort)
            sorteado.append(numero)
            mega_sort.remove(numero)

        sorteado.sort()

        cont += 1

    soma += cont

    print('Resultado {}: {} tentativas'.format(i+1, cont))

print('Media: {}'.format(soma/n))

