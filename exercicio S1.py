import sqlite3

con = sqlite3.connect('carros.db')

cursor = con.cursor()

cursor.execute('''
CREATE TABLE carros(
    id INTEGER PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    cor VARCHAR(20) NOT NULL
);
''')

con.commit()

con.close()