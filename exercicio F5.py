n1 = int(input('Insira um ano: '))

if n1%4==0 and n1%100!= 0:
    print('O ano {} é bissexto'.format(n1))
else:
    print('O ano {} não é bissexto'.format(n1))