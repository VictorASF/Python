print(' Ja é natal vamos ter aumento ')
n1 = float(input('Insira seu salario R$: '))
if n1<1500:
    n2 = n1*(20/100)
else:
    n2 = n1*(10/100)
print('Seu aumento foi de R$:{:.2f} e seu salario ficou em R$: {:.2f} '.format(n2, n1+n2))