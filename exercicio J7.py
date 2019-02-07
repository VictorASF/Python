menorv = 9999999999999999999999999999999999
menorp = ' '
maior = 0
soma = 0
while True:
    np = str(input('Nome do produto: '))
    nv = float(input('Valor R$: '))
    soma += nv
    if nv < menorv:
        menorv = nv
        menorp = np
    if nv >= 100:
        maior += 1
    a = str(input('Deseja inserir outro produto (S/N): '))
    a = a.upper()
    if a == 'N':
        break
print('''Total de valores R$: {:.2f}
Produtos que valem mais de R$:100,00: {}
Produto de menor valor: {} que vale R$:{:.2f}'''.format(soma, maior, menorp, menorv))