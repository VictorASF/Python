import random
h=0
while True:
    c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    d = random.choice(c)
    a = int(input('Qual o numero sorteado(1-10): '))
    if a == d:
        print('Parabens voce acertou o numero é: {}'.format(a))
        break
    h+=1
    print('Incorreto')
print('O numero de tentativas foram {}'.format(h+1))