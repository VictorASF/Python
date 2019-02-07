n1 = float(input('Insira o valor do imovel R$: '))
n2 = float(input('Insira seu salario R$: '))
n3 = int(input('Insira em quantos anos deseja pagar: '))

meses = n3*12
valor_prestacao = n1/meses
sal = n2*(30/100)

if sal >= valor_prestacao:
    print('Emprestimo {}aprovado{}'.format('\033[4;32m', '\033[m'))
    print('Valor da prestacao R$:{:.2f}'.format(valor_prestacao))
    print('Tempo de pagamento {} meses'.format(meses))
else:
    print('Emprestimo {}negado{}'.format('\033[4;31m', '\033[m'))


