def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    curso = input("Digite o curso do aluno: ")

    aluno_info = f"Nome: {nome}\nEmail: {email}\nCurso: {curso}\n"

    with open('alunos.txt', 'a') as arquivo:
        arquivo.write(aluno_info)
        arquivo.write('-' * 30 + '\n')

    print("Aluno cadastrado com sucesso.")

def listar_alunos():
    arquivo = open('alunos.txt', 'r')
    conteudo = arquivo.read()
    arquivo.close()
    
    if conteudo.strip():  # verificador de arquivo vazio
        print("Lista de alunos cadastrados:")
        print("-" * 30)
        print(conteudo)
        print("-" * 30)
    else:
        print("Nenhum aluno cadastrado ainda.")

def buscar_aluno_por_nome():
    nome_busca = input("Digite o nome do aluno que deseja buscar: ")
    encontrado = False
    
    arquivo = open('alunos.txt', 'r')
    
    for linha in arquivo:
        if nome_busca in linha:
            print("Aluno encontrado:")
            print("-" * 30)
            print(linha.strip())
            print("-" * 30)
            encontrado = True
    
    arquivo.close()

    if not encontrado:
        print(f"Nenhum aluno com o nome '{nome_busca}' encontrado.")


def menu():
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
