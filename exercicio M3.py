d1 = {}

for i in range (1,4):
    a = str(input('Nota {}: '.format(i)))
    d1[i] = float(a)
print('Selecione a nota que sera cancelada')
for ky, vl in d1.items():
    print('{} - {} '.format(ky,vl))

l1 = list(d1.keys())
print(l1,end='')
b = int(input('? '))
for h in range (0,3):
    if b == l1[h]:
        l1.pop(h)
        d1.pop(b)
print('Media: {}'.format(
    (d1[l1[0]] + d1[l1[-1]])/2
))