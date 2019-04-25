import mysql as my
a = 1

def selecionar():
    i = 0
    b = ''
    print('----SELECIONAR----')
    a = my.select('*', 'alunos')
    a = a[0]
    for j in a:
        i += 1
        print(f'({i}) - {j}')
    i += 1
    print(f'({i}) - Todos os campos use o "*"')
    b = str(input('Insira o nome do campo desejado: ').strip())
    print('Se desejar inserir um WHERE, insira o campo e a condição caso contrario pressione enter somente')
    c = str(input(''))

    d = my.select(b, 'alunos', c)
    for h in d:
        for k in h:
            print(h[k], end=' // ')
        print()
    input('Pressione <<ENTER>> para continuar')


def inserir():
    print('-----INSERIR-----')
    a = my.select('*', 'alunos')
    a = a[0]
    l = []
    i = 0
    b = ''
    tamlist = 0
    for j in a:
        i += 1
        if 'id_' in j:
            l.append('DEFAULT')

        else:
            while b == '':
                print(f'Campo a ser inserido: {j}', end=' ')
                b = (input(''))
            l.append(b)
            b = ''
    tam = len(l)
    for itens in l:
        if itens == 'DEFAULT':
            b = b + '"'+itens+', '
            tamlist += 1
        elif tam-1 == tamlist:
            b = b + "'"+itens+"'"+'"'
            tamlist += 1
        else:
            b = b + "'" + itens + "', "
            tamlist += 1







def atualizar():
    print('-----ATUALIZAR-----')
    i = 0
    print('Campos que podem ser atualizados')
    a = my.select('*', 'alunos')
    a = a[0]
    for j in a:
        i += 1
        if 'id_' in j:
            i = i - 1
            continue
        else:
            print(f'({i}) - {j}')


while a != 0:
    a = 0
    print('-'*7+'MENU'+'-'*7)
    print('(1) Selecionar ')
    print('(2) Inserir ')
    print('(3) Atualizar ')
    print('(4) Deletar ')
    print('(0) Sair ')
    a = int(input('Opção: '))
    if a == 1:
        selecionar()
    elif a == 2:
        inserir()
    elif a == 3:
        atualizar()

