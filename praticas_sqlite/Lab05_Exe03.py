import sqlite3

# Conexão com banco de dados criado, apotando o seu diretorio;
conn = sqlite3.connect('D:/UNA/sistemas/praticas_sqlite/bdpessoas.db')

nome = input('Informe o nome: ')
idade = input('Informe a idade: ')

# Manipular o banco de dados criado;
cursor = conn.cursor()

cursor.execute("insert into pessoas (nome, idade) values('Marcus', '28')")
cursor.execute("insert into pessoas (nome, idade) values('"+ nome + "', " + idade + ")")
conn.commit()


cursor.execute('select * from pessoas')

for linha in cursor.fetchall():
    print(linha)

conn.close()
