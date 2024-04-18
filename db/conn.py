import sqlite3

conexao = sqlite3.connect('sreo.db')

iterator = conexao.cursor()

iterator.execute('CREATE TABLE IF NOT EXISTS clientes('
                 'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                 'nome TEXT,'
                 'idade INTEGER'
                 ''
                 ')')

iterator.execute('INSERT INTO clientes(nome,idade) values ("vugnaes", 123)')

iterator.execute('SELECT * FROM clientes')
conexao.commit()

for i in iterator.fetchall():
    print(i)


iterator.close()
conexao.close()