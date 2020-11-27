import sqlite3

conn = sqlite3.connect('D:/UNA/sistemas/praticas_sqlite/bdpessoas.db')
cursor = conn.cursor()

opcao = int(input('|1| Novo Cadastro \n|2| Ler Cadastro \n|3| Atualizaar Cadastro \n|4| Deletar Cadastro \nSelecione uma opcao. '))

if opcao == 1:
    nome = input('Informe o nome: ')
    idade = input('Informe a idade: ')

    cursor.execute("insert into pessoas (nome, idade) values('" + nome + "', " + idade + ")")
    conn.commit()

elif opcao == 2:
    cursor.execute('select * from pessoas')

    for linha in cursor.fetchall():
        print(linha)

elif opcao == 3:
    cursor.execute('select * from pessoas')

    for linha in cursor.fetchall():
        print(linha)

    id_pessoa = input('Digite o codigo do cadastro escolhido: ')
    novo_nome = input('Informe o novo nome: ')
    nova_idade = input('Informe a nova idade: ')

    cursor.execute("""UPDATE pessoas SET nome = ?, idade = ? WHERE cod = ?""", (novo_nome, nova_idade, id_pessoa))

    conn.commit()

    print('Dados atualizados com sucesso.')

elif opcao == 4:
    cursor.execute('select * from pessoas')

    for linha in cursor.fetchall():
        print(linha)

    id_pessoa = input('Digite o codigo do cadastro escolhido: ')

    cursor.execute("""DELETE FROM pessoas WHERE cod = ?""", (id_pessoa,))

    conn.commit()

    print('Registro excluido com sucesso.')

else:
    print('ERRO NA OPCAO DE ESCOLHA DO MENU!!!')


conn.close()

