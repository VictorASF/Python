def listarcontato():
    arq = open('contatos.txt', 'r')
    linha = arq.readline()
    print('+' + '-' * 9 + '+' + '-' * 39 + '+')
    print('| Codigo  | {:<38}|'.format('Nome'))
    print('+' + '-' * 9 + '+' + '-' * 39 + '+')
    while len(linha) > 0:
        print('| {:<7} | {:<38}|'.format(linha[0:5].strip(), linha[5:45].strip()))
        linha = arq.readline()
    print('+' + '-' * 9 + '+' + '-' * 39 + '+')
    input('Pressione <ENTER>')
    arq.close()


def verdados(codigo = ''):
    arq = open('contatos.txt', 'r')
    while True:
        linha = arq.readline()
        if codigo in linha[0:5]:
            print('Codigo....: {}'.format(linha[0:5].strip()))
            print('Nome......: {}'.format(linha[5:45].strip()))
            print('Telefone..: {}'.format(linha[45:60].strip()))
            print('E-Mail....: {}'.format(linha[60:].strip()))
            input('Pressione <ENTER>')
            arq.close()
            break
        elif len(linha) == 0 :
            print('Codigo inexistente')
            input('Pressione <ENTER>')
            arq.close()
            break


def incluir():
    arq = open('contatos.txt', 'a')
    a = int(input('Codigo: ').strip())
    b = str(input('Nome: ').strip().capitalize())
    c = str(input('Telefone: ').strip())
    d = str(input('E-Mail: ').strip())
    arq.writelines('\n{:<5}{:<45}{:<15}{:<}'.format(a, b, c, d))
    print('Contato inserido com sucesso {}'.format(b))
    input('Pressione <ENTER>')
    arq.close()


def excluir():
    arq = open('contatos.txt', 'r')
    a = -1
    a = str(input('Insira o codigo que deseja remover: '))
    lista = arq.readlines()
    b = 0
    for linha in lista:
        codigo = linha[0:5].strip()
        if codigo == a:
            del(lista[int(codigo)-1])
            print('Contato removido')
            input('Pressione <ENTER>')
    arq.close()
    arq = open('contatos.txt', 'w')
    arq.writelines(list(lista))
    arq.close()


while True:
    print('='*50)
    print('{:^50}'.format('Agenda de Telefones e E-Mail'))
    print('='*50)
    print('''
1. Listar seus contatos
2. Ver dados de um contato
3. Incluir um contato
4. Apagar um contato
5. Sair
''')
    a = int(input('Qual sua opção[1/2/3/4/5]? '))
    if a == 1 :
       listarcontato()
    elif a == 2:
        codigo = int(input('Insira o codigo: '))
        verdados(str(codigo))
    elif a == 3:
        incluir()
    elif a == 4:
        excluir()
    elif a == 5:
        break

