import MySQLdb

#onde o banco esta hosteado
host = 'localhost'
#usuario para acessar o banco
user = 'aplicacao'
#senha do usuario
password = '123456'
#DB é para inserir o nome do banco que desejo acessar usando esse usuario e senha
db = 'banco_alunos'
#porta padrão do MySQL
port = 3306

ida = 0

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor(MySQLdb.cursors.DictCursor)

def select(fields, tables, where=None):

    query = 'SELECT ' + fields + ' FROM ' + tables
    if(where):
        query = query + ' WHERE ' + where

    c.execute(query)

    return c.fetchall()

#
#print(select('*','alunos'))
#

def insert(values, table, fields = None):

    query = 'INSERT INTO ' + table
    if (fields):
        query = query + '(' + fields + ') '
    query = query + ' VALUES ' + ','.join(['(' + v + ')' for v in values])
    print(query)

    c.execute(query)
    con.commit()
    print('Insercao concluida com sucesso')

#
#values = ["DEFAULT, 'João Pedro', '12345678912', '2000-01-01', 'Av. das Pedras, 123', 'Betim', 'MG'",
#         "DEFAULT, 'Maria Carolina', '98765432198', '2000-01-01', 'Av. das Pedras, 123', 'Betim', 'MG'"]


def update(sets, table, where):

    query = 'UPDATE ' + table
    query = query +' SET ' + ','.join([field + " = '" + value + "'" for field, value in sets.items()])
    query = query + ' WHERE ' + where

    c.execute(query)
    con.commit()

#
#update({'al_nome':'Jorome', 'al_cpf':'45678912321'}, "alunos", 'al_id_aluno = 7' )
#

def delete(table, where):
    query = 'DELETE FROM ' + table + ' WHERE ' + where

    c.execute(query)
    con.commit()


