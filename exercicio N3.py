telefone = {}
op = 0
h = 0
def listar():
    for a, b in telefone.items():
        print('''Codigo....: {}
Nome......: {}
Telefone..: {}\n'''.format(a, b[0], b[1]))
    if len(telefone) == 0:
        print('Sua lista está vazia')
        input('Pressione <ENTER> para continuar')
def exibir():
    h = int(input('Codigo: '))
    if h in telefone.keys():
        print('Codigo....: {}'.format(h))
        print('Nome......: {}'.format(telefone[h][0]))
        print('Telefone..: {}\n'.format(telefone[h][1]))
        input('Pressione <ENTER> para continuar\n')
    else:
        print('Codigo inexistente')
        input('Pressione <ENTER> para continuar')

def incluir():
    codigo = int(input('Codigo....: '))
    nome = str(input('Nome......: '))
    tel = str(input('Telefone..: '))
    if codigo in telefone.keys():
        print('Codigo ja existente, voltando ao menu')
    else:
        telefone[codigo] = [nome, tel]
        print(telefone)
        print('Usuario inserido com sucesso')
def apagar():
    codigo = int(input('Insira o codigo que deseja remover: '))
    if codigo in telefone.keys():
        telefone.pop(codigo)
        print('Removido com Sucesso')
    else:
        print('Codigo não inserido')

while True:
    print('''----LISTA TELEFONICA----
1. Listar Informações 
2. Exibir informações de um contato
3. Incluir um contato 
4. Apagar um contato 
5. Sair
    ''')
    op = int(input('Seleciona a opção [1/2/3/4/5]? '))
    if op == 1:
        listar()
    elif op == 2:
        exibir()
    elif op == 3:
        incluir()
    elif op == 4:
        apagar()
    else:
        if op == 5:
            print('Saindo do programa')
            break
        else:
            print('Opção inexistente tente novamente')
            continue