import math
def soma(x, y):
    som = x + y
    print('\n{:^15}'.format('SOMA'))
    print('{} + {} = {}\n'.format(x, y, som))


def substracao(x, y):
    sub = x - y
    print('\n{:^15}'.format('SUBTRAÇÃO'))
    print('{} - {} = {}\n'.format(x, y, sub))


def divisao (x, y):
    try:
        div = x / y
        print('\n{:^15}'.format('DIVISÃO'))
        print('{} / {} = {:.2f}\n'.format(x, y, div))
    except Exception:
        print('Divisor igual ou menor que zero impossivel dividir')


def multiplicacao (x, y):
    mult = x * y
    print('\n{:^15}'.format('MULTIPLICAÇÃO'))
    print('{} * {} = {}'.format(x, y, mult))


def raiz(x, y):
    try:
        n1 = math.sqrt(x)
    except Exception:
        print('Não pode ser feita a raiz de {} um numero negativo'.format(x))
    else:
        print('\n{:^15}'.format('RAIZ QUADRADA'))
        print('Raiz de {} é {:.2f}'.format(x, n1))
    try:
        n2 = math.sqrt(y)
    except Exception:
        print('Não pode ser feita a raiz de {} um numero negativo'.format(y))
    else:
        print('Raiz de {} é {:.2f}\n'.format(y, n2))


def new():
    while True:
        try:
            n1 = float(input('Numero 1: '))
            break
        except Exception:
            print('String inserida insira somente numeros')
    while True:
        try:
            n2 = float(input('Numero 2: '))
        except Exception:
            print('String inserida insira somente numeros')
        else:
            return n1, n2


numeros = new()
num1 = numeros[0]
num2 = numeros[1]
while True:
    try:
        escolha = int(input('''CALCULADORA
1.Soma
2.Subtração
3.Divisão
4.Multiplicação
5.Raiz Quadrada
6.Digitar outros numeros
0.Sair
Opção:'''))
        if 0 <= escolha <= 6:
            if escolha == 1:
                soma(num1, num2)
                input('Pressione <ENTER> para continuar')
            elif escolha == 2:
                substracao(num1, num2)
                input('Pressione <ENTER> para continuar')
            elif escolha == 3:
                divisao(num1, num2)
                input('Pressione <ENTER> para continuar')
            elif escolha == 4:
                multiplicacao(num1, num2)
                input('Pressione <ENTER> para continuar')
            elif escolha == 5:
                raiz(num1, num2)
                input('Pressione <ENTER> para continuar')
            elif escolha == 6:
                numeros = new()
                num1 = numeros[0]
                num2 = numeros[1]
                input('Pressione <ENTER> para continuar')
            elif escolha == 0:
                print('Saindo do programa, Obrigado por usar')
                break
        else:
            print('Valor invalido, tente novamente')
    except Exception:
        print('String Inserida, Insira somente numeros')
