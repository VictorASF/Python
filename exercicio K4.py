l1 = []
while True:
    a = str(input('Numero: '))
    a = a.strip()
    if a != '':
        if a.isnumeric:
            l1.append(a)
        else:
            break
    else:
        break
for i in range(len(l1)):
    print(l1[i], end=' ')
l1.sort()
print('\n')
for i in range(len(l1)):
    print(l1[i], end=' ')
print('\n')
for i in range((len(l1))//2):
    print(l1[i], end=' ')