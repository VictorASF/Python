n50 = 0
n20 = 0
n10 = 0
n1= 0
vs = int(input('Quanto deseja sacar: '))
while vs > 0:
    if vs-50 >= 0:
        n50 += 1
        vs = vs-50
    elif vs-20 >= 0:
        n20 += 1
        vs = vs-20
    elif vs-10 >= 0:
        n10 += 1
        vs = vs-10
    else:
        n1 += 1
        vs = vs-1

if n50>0:
    print('Total de cedulas de R$:50.00: {}'.format(n50))
if n20>0:
    print('Total de cedulas de R$:20.00: {}'.format(n20))
if n10>0:
    print('Total de cedulas de R$:10.00: {}'.format(n10))
if n1>0:
    print('Total de cedulas de R$:1.00: {}'.format(n1))
