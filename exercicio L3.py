l = ['Vermelho', 'Azul', 'Preto', 'Branco', 'Amarelo', 'Verde']
a = str(input('Insira uma cor: '))
a = a.capitalize()
if a in l:
    for i in range (len(l)):
        if a == l[i]:
            d = i+1
    print('{} está na lista na {}° posição'.format(a,d))
else:
    print('{} não consta na lista'.format(a))
