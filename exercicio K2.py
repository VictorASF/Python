lista = []
d = ' '
while True:
    d = str(input('Insira um nome: '))
    d = d.strip()
    d = d.capitalize()
    if d != '':
        lista.append(d)
    else:
        break
lista.sort()
for idx, item in enumerate(lista):
    print(lista[idx], end=' ')
a = int(input('Insira uma posição para ser removida (0-{}):'.format(len(lista)-1)))
del(lista[a])
for idx, item in enumerate(lista):
    print(lista[idx], end=' ')