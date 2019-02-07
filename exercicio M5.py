l1 = []
l2 = []
d1 = {}
while True:
    a = str(input('Nome....: '))
    b = str(input('Telefone: '))
    a = a.strip()
    a = a.capitalize()
    if a == '':
        break
    else:
        l1.append(a)
        l2.append(b)
for i in range(len(l1)):
    d1[l1[i]] = int(l2[i])
print(d1)
for ky,vl in d1.items():
    print('Nome: {} -- Telefone: {}'.format(ky,vl))
