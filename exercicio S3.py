import io
import sqlite3

con = sqlite3.connect('carros.db')

with io.open('carros_dumb.sql', 'w') as f:
    for linha in con.iterdump():
        f.write('%s\n' % linha)


con.close()

con = sqlite3.connect('carros_recuperados.db')
cursor = con.cursor()

f = io.open('carros_dumb.sql', 'r')
sql = f.read()
cursor.executescript(sql)

con.close()
