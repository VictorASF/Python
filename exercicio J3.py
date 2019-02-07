print('='*10+'OPERADOR'+'='*10)
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
a = 0

while a !=5:
    a = int(input('''MENU
    1 - Somar
    2 - Multiplicar
    3 - Maior valor
    4 - Entrar novos numeros
    5 - Sair
    Opção: '''))

    if a == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
    elif a == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
    elif a == 3:
        if n1>n2:
            print('{} é maior que {}, o primeiro numero é maior'.format(n1, n2))
        elif n1<n2:
            print('{} é menor que {}, o segundo numero é maior'.format(n1, n2))
        else:
            print('{} é igual a {}, os valores são iguais'.format(n1, n2))
    elif a == 4:
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo numero: '))
    elif a == 5:
        print('Saindo do programa')
        break
    else:
        print('Opção escolhida não existe')
