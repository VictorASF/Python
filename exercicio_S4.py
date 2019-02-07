import os
import sqlite3

con = sqlite3.connect('carros_alemao.db')
cursor = con.cursor()

def cls():
    os.system('cls')


def menu():
    while True:
        cls()
        print('  ' + '='*25)
        print('||' + '{:^25}'.format('CARROS DO ALEMÃO') + '||')
        print('  ' + '=' * 25)
        print('''
1. Listar carros
2. Incluir um carro
3. Alterar um carro
4. Excluir um carro
0. Sair''')
        opcao = int(input('Selecione uma opção: '))
        if 0 <= opcao <= 4:
            return opcao
        else:
            print('Opção invalida, selecione numeros entre 0 e 4 somente')
            input('Pressione <ENTER> para continuar')
            cls()


def listar():
    cls()
    lista = cursor.execute('''
    SELECT * FROM carros''')
    print('{:<3}  {:<30} {:<15} {}'.format('ID', 'NOME', 'COR', 'DATA DE FABRICAÇÃO'))
    for a in lista:
        print('{:<3}  {:<30} {:<15} {}'.format(a[0], a[1], a[2], a[3]))
    input('\nPressione <ENTER> para continuar')


def incluir():
    cls()
    print('{:^25}'.format('INCLUIR VEICULO'))
    c_nome = str(input('Insira o nome do veiculo: '))
    c_cor = str(input('Insira a cor do veiculo: '))
    c_data = str(input('Insira o ano de fabricação: '))
    con.execute('''
    INSERT INTO carros(Nome, Cor, Ano_de_fabricacao)
    VALUES (?, ?, ?)
    ''',(c_nome, c_cor, c_data))
    con.commit()
    print('Carro incluido.',end='')
    input('Pressione <ENTER> para continuar')


def alterar():
    cls()
    print('{:^25}'.format('ALTERAR UM CARRO'))
    id_mudar = int(input('Inserir o Id do carro: '))

    carro = con.execute('''
    SELECT * FROM carros WHERE Id = ?''',(id_mudar,))

    print('--Dados Antigos'+'-'*25)

    print('Nome.: {}'.format(carro[1]))
    print('Cor..: {}'.format(carro[2]))
    print('Ano..: {}'.format(carro[3]))

    print('--Dados Novos'+'-'*27)

    new_nome = str(input('Nome.: '))
    new_cor = str(input('Cor..:'))
    new_ano = str(input('Ano..:'))

    con.execute('''
    UPDATE carros
    SET Nome = ?, Cor = ?, Ano_De_Fabricacao = ?
    WHERE Id = ?''',(new_nome, new_cor, new_ano, id_mudar))
    con.commit()
    print('Alterado com sucesso', end='')
    input('Pressione <ENTER> para continuar ')


def excluir():
    cls()
    print('{:^25}'.format('EXCLUIR VEICULO'))
    id_remover = int(input('Insira o ID do veiculo que deseja remover: '))
    con.execute('''
DELETE FROM carros 
WHERE Id = ?''', (id_remover,))
    con.commit()
    print('Veiculo removido com sucesso',end='')
    input('Pressione <ENTER> para continuar')


while True:

    escolhido = menu()
    if escolhido == 1:
        listar()
    elif escolhido == 2:
        incluir()
    elif escolhido == 3:
        alterar()
    elif escolhido == 4:
        excluir()
    elif escolhido == 0:
        print('Saindo do programa!')
        input('Pressione <ENTER> para continuar')
        con.close()
        break