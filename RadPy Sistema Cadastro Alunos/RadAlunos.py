import sqlite3

def criar_tabela_alunos():
    conexao = sqlite3.connect('alunos.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            curso TEXT NOT NULL
        )
    ''')

    conexao.commit()
    conexao.close()


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    curso = input("Digite o curso do aluno: ")

    conexao = sqlite3.connect('alunos.db')
    cursor = conexao.cursor()

    cursor.execute('INSERT INTO alunos (nome, email, curso) VALUES (?, ?, ?)', (nome, email, curso))

    conexao.commit()
    conexao.close()

    print("Aluno cadastrado com sucesso.")

def listar_alunos():
    conexao = sqlite3.connect('alunos.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM alunos')
    alunos = cursor.fetchall()

    conexao.close()

    if alunos:
        print("Lista de alunos cadastrados:")
        for aluno in alunos:
            print(f"ID: {aluno[0]}")
            print(f"Nome: {aluno[1]}")
            print(f"Email: {aluno[2]}")
            print(f"Curso: {aluno[3]}")
            print("-" * 30)
    else:
        print("Nenhum aluno cadastrado ainda.")


def buscar_aluno_por_nome():
    nome_busca = input("Digite o nome do aluno que deseja buscar: ")

    conexao = sqlite3.connect('alunos.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM alunos WHERE nome LIKE ?', (f'%{nome_busca}%',))
    alunos = cursor.fetchall()

    conexao.close()

    if alunos:
        print("Alunos encontrados:")
        for aluno in alunos:
            print(f"ID: {aluno[0]}")
            print(f"Nome: {aluno[1]}")
            print(f"Email: {aluno[2]}")
            print(f"Curso: {aluno[3]}")
            print("-" * 30)
    else:
        print(f"Nenhum aluno com o nome '{nome_busca}' encontrado.")

def menu():
    criar_tabela_alunos()
    while True:
        print("\nMenu:")
        print("1. Cadastrar um novo aluno")
        print("2. Listar os alunos cadastrados")
        print("3. Buscar um aluno pelo nome")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            buscar_aluno_por_nome()
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu()
