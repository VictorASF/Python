import sqlite3

con = sqlite3.connect('carros.db')

cursor = con.cursor()

lista = [(1, 'HRV', 'Verde'), (2, 'Fox', 'Preto'), (3, 'Corola', 'Cinza'), (4, 'HB20', 'Vermelho'), (5, 'Gol', 'Azul')]

cursor.executemany('''
INSERT INTO carros (id, nome, cor)
VALUES (?, ?, ?)
''', lista)

print('Carros inseridos com sucesso\n')

con.commit()

car = cursor.execute('''
SELECT * FROM carros''')

for a in car:
    print('ID..: {}'.format(a[0]))
    print('Nome: {}'.format(a[1]))
    print('Cor.: {}'.format(a[2]))
    print('-'*15)

id_del = 4

cursor.execute('''
DELETE FROM carros WHERE id = ?''', (id_del,))

print('\nCarro deletado com sucesso\n')

id_mud = 2
nova_cor = 'Amarelo'

cursor.execute('''
UPDATE carros
SET cor = ?
WHERE id = ?''', (nova_cor, id_mud))

print('Carro atualizado com sucesso\n')
con.commit()

car = cursor.execute('''
SELECT * FROM carros''')

for a in car:
    print('Id...: {}'.format(a[0]))
    print('Carro: {}'.format(a[1]))
    print('Cor..: {}'.format(a[2]))
    print('-'*15)

con.close()