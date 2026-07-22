livros = []
usuarios = []
emprestimos = []


def menu():
    while True:
        print("\n========== SISTEMA DE BIBLIOTECA ==========")
        print("1 - Cadastrar livro")
        print("2 - Cadastrar usuário")
        print("3 - Consultar livros")
        print("4 - Emprestar livro")
        print("5 - Devolver livro")
        print("6 - Relatório de empréstimos")
        print("7 - Buscar livro")
        print("8 - Editar livro")
        print("9 - Excluir livro")
        print("10 - Estatísticas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            cadastrar_usuario()
        elif opcao == "3":
            consultar_livros()
        elif opcao == "4":
            emprestar_livro()
        elif opcao == "5":
            devolver_livro()
        elif opcao == "6":
            relatorio_emprestimos()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        elif opcao == "7":
                    buscar_livro()
        elif opcao == "8":
            editar_livro()

        elif opcao == "9":
            excluir_livro()

        elif opcao == "10":
            estatisticas()
        elif opcao == "0":
            print("programa encerrado.")
        else:
            print("Opção inválida!")
        


def cadastrar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    codigo = input("Código: ")

    for livro in livros:
        if livro["codigo"] == codigo:
            print("Já existe um livro com esse código!")
            return

    while True:
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade >= 0:
                break
            print("Digite um número maior ou igual a zero.")
        except ValueError:
            print("Digite apenas números.")

    livro = {
        "titulo": titulo,
        "autor": autor,
        "codigo": codigo,
        "quantidade": quantidade,
        "emprestimos": 0
    }

    livros.append(livro)
    print("Livro cadastrado com sucesso!")

def cadastrar_usuario():
    nome = input("Nome: ")
    matricula = input("Matrícula: ")

    for usuario in usuarios:
        if usuario["matricula"] == matricula:
            print("Essa matrícula já está cadastrada.")
            return

    usuarios.append({
        "nome": nome,
        "matricula": matricula
    })

    print("Usuário cadastrado com sucesso!")

def consultar_livros():
    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    print("\n===== LIVROS DISPONÍVEIS =====")

    for livro in livros:
        print("----------------------------")
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Código:", livro["codigo"])
        print("Quantidade:", livro["quantidade"])


def emprestar_livro():
    if len(livros) == 0:
        print("Não há livros cadastrados.")
        return

    if len(usuarios) == 0:
        print("Não há usuários cadastrados.")
        return

    codigo = input("Código do livro: ")
    matricula = input("Matrícula do usuário: ")

    livro_encontrado = None
    usuario_encontrado = None

    for livro in livros:
        if livro["codigo"] == codigo:
            livro_encontrado = livro
            break

    for usuario in usuarios:
        if usuario["matricula"] == matricula:
            usuario_encontrado = usuario
            break

    if livro_encontrado is None:
        print("Livro não encontrado.")
        return

    if usuario_encontrado is None:
        print("Usuário não encontrado.")
        return

    if livro_encontrado["quantidade"] <= 0:
        print("Livro indisponível.")
        return

    livro_encontrado["quantidade"] -= 1
    livro_encontrado["emprestimo"] += 1 

    emprestimos.append({
        "usuario": usuario_encontrado["nome"],
        "matricula": matricula,
        "titulo": livro_encontrado["titulo"],
        "codigo": codigo
    })

    print("Empréstimo realizado com sucesso!")


def devolver_livro():
    matricula = input("Matrícula do usuário: ")
    codigo = input("Código do livro: ")

    for emprestimo in emprestimos:
        if emprestimo["matricula"] == matricula and emprestimo["codigo"] == codigo:

            for livro in livros:
                if livro["codigo"] == codigo:
                    livro["quantidade"] += 1
                    break

            emprestimos.remove(emprestimo)
            print("Livro devolvido com sucesso!")
            return

    print("Empréstimo não encontrado.")


def relatorio_emprestimos():
    if len(emprestimos) == 0:
        print("Nenhum empréstimo realizado.")
        return

    print("\n======= RELATÓRIO =======")

    for emprestimo in emprestimos:
        print("------------------------")
        print("Usuário:", emprestimo["usuario"])
        print("Matrícula:", emprestimo["matricula"])
        print("Livro:", emprestimo["titulo"])
        print("Código:", emprestimo["codigo"])


def buscar_livro():
    nome = input("Digite o título do livro: ").lower()

    encontrado = False

    for livro in livros:
        if nome in livro["titulo"].lower():
            print("-------------------------")
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Código:", livro["codigo"])
            print("Quantidade:", livro["quantidade"])
            encontrado = True

    if not encontrado:
        print("Livro não encontrado.")

def editar_livro():
    codigo = input("Digite o código do livro: ")

    for livro in livros:
        if livro["codigo"] == codigo:
            print("\nDeixe em branco caso não queira alterar.\n")

            titulo = input("Novo título: ")
            autor = input("Novo autor: ")

            if titulo != "":
                livro["titulo"] = titulo

            if autor != "":
                livro["autor"] = autor

            print("Livro atualizado com sucesso!")
            return

    print("Livro não encontrado.")


def excluir_livro():
    codigo = input("Código do livro: ")

    for livro in livros:
        if livro["codigo"] == codigo:
            livros.remove(livro)
            print("Livro removido com sucesso!")
            return

    print("Livro não encontrado.")


def estatisticas():
    print("\n===== ESTATÍSTICAS =====")

    print("Total de livros cadastrados:", len(livros))
    print("Total de usuários:", len(usuarios))
    print("Empréstimos ativos:", len(emprestimos))

    if len(livros) > 0:
        maior = livros[0]

        for livro in livros:
            if livro["emprestimos"] > maior["emprestimos"]:
                maior = livro

        print("Livro mais emprestado:", maior["titulo"])
        print("Quantidade de empréstimos:", maior["emprestimos"])




menu()