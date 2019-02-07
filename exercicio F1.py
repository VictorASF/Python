import random

n1 = [0, 1, 2, 3, 4, 5]
n2 = random.choice(n1)
print('='*10 + 'SORTEADOR' + '='*10)

n3 = int(input('Qual o numero sorteado (0 - 5): '))

if n3 == n2:
    print('Parabens você venceu')
else:
    print('Você perdeu o numero sorteado foi {}'.format(n2))