n1 = float(input('Qual o valor do livro R$: '))
n2 = int(input('''[1] Dinheiro
[2] Cartão a vista
[3] 2x no cartão
[4] 3x ou mais no cartão
Opção: '''))

if n2 == 1:
    print('Valor final R$: {:.2f}'.format(n1-(n1*(10/100))))
elif n2 == 2:
    print('Valor final R$: {:.2f}'.format(n1-(n1*(5/100))))
elif n2 == 3:
    print('''Valor final de cada parcela R$: {:.2f}
    Valor total: {:.2f}'''.format(n1/2,n1))
elif n2 == 4:
    n1 = n1+(n1*(20/100))
    print('''Valor final de cada parcela R$: {:.2f}
    Valor total: {:.2f}'''.format(n1/3,n1))