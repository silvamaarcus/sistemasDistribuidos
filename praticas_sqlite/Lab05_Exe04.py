import sqlite3

conn = sqlite3.connect('D:/UNA/sistemas/praticas_sqlite/bdpessoas.db')
cursor = conn.cursor()

# lendo os dados
cursor.execute("""SELECT * FROM pessoas;""")

for linha in cursor.fetchall():
    print(linha)

opcao = input('Deseja acrescentar mais um item a tabela? (sim/nao) ').lower()

if opcao == 's' or opcao == 'sim':
    nome = input('Informe o nome: ')
    idade = input('Informe a idade: ')

    cursor.execute("insert into pessoas (nome, idade) values('" + nome + "', " + idade + ")")
    conn.commit()

    cursor.execute('select * from pessoas')

    for linha in cursor.fetchall():
        print(linha)

else:
    print('Aperte ENTER para continuar...')

conn.close()