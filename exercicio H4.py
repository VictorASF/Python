n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
print('Media: {}'.format(media))
if media<5:
    print('Reprovado')
elif 5 < media < 6.9:
    print('Recuperação')
else:
    print('Aprovado')