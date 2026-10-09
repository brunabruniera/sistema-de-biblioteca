class Livro:
    def __init__(self, titulo: str, autor: str, codigo: str, quantidade: int):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.quantidade = quantidade
        self.emprestimos = 0

    def consultar(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Código:", self.codigo)
        print("Quantidade:", self.quantidade)

    def editar(self, titulo: str, autor: str):
        if titulo != "":
            self.titulo = titulo
        if autor != "":
            self.autor = autor

    def excluir(self):
        print("Livro removido:", self.titulo)


class Usuario:
    def __init__(self, nome: str, matricula: str):
        self.nome = nome
        self.matricula = matricula


class Emprestimo:
    def __init__(self, usuario: Usuario, livro: Livro):
        self.usuario = usuario
        self.livro = livro


class Biblioteca:
    def __init__(self):
        self.livros: list[Livro] = []
        self.usuarios: list[Usuario] = []
        self.emprestimos: list[Emprestimo] = []

    def cadastrar_livro(self):
        titulo = input("Título: ")
        autor = input("Autor: ")
        codigo = input("Código: ")

        for livro in self.livros:
            if livro.codigo == codigo:
                print("Código já cadastrado!")
                return

        while True:
            try:
                quantidade = int(input("Quantidade: "))
                if quantidade >= 0:
                    break
                print("Digite um número maior ou igual a zero.")
            except ValueError:
                print("Digite apenas números.")

        livro = Livro(titulo, autor, codigo, quantidade)
        self.livros.append(livro)
        print("Livro cadastrado com sucesso!")

    def cadastrar_usuario(self):
        nome = input("Nome: ")

        matricula = str(len(self.usuarios) + 1)

        usuario = Usuario(nome, matricula)
     self.usuarios.append(usuario)

    print("Usuário cadastrado com sucesso!")
    print("Sua matrícula é:", matricula)

    def consultar_livros(self):
        if len(self.livros) == 0:
            print("Nenhum livro cadastrado.")
            return

        for livro in self.livros:
            print("--------------------")
            livro.consultar()

    def emprestar_livro(self):
        codigo = input("Código do livro: ")
        matricula = input("Matrícula do usuário: ")

        livro_encontrado = None
        usuario_encontrado = None

        for livro in self.livros:
            if livro.codigo == codigo:
                livro_encontrado = livro
                break

        for usuario in self.usuarios:
            if usuario.matricula == matricula:
                usuario_encontrado = usuario
                break

        if livro_encontrado is None:
            print("Livro não encontrado.")
            return

        if usuario_encontrado is None:
            print("Usuário não encontrado.")
            return

        if livro_encontrado.quantidade <= 0:
            print("Livro indisponível.")
            return

        livro_encontrado.quantidade -= 1
        livro_encontrado.emprestimos += 1

        emprestimo = Emprestimo(usuario_encontrado, livro_encontrado)
        self.emprestimos.append(emprestimo)

        print("Empréstimo realizado com sucesso!")

    def devolver_livro(self):
        matricula = input("Matrícula do usuário: ")
        codigo = input("Código do livro: ")

        for emprestimo in self.emprestimos:
            if (emprestimo.usuario.matricula == matricula
                    and emprestimo.livro.codigo == codigo):

                emprestimo.livro.quantidade += 1
                self.emprestimos.remove(emprestimo)
                print("Livro devolvido com sucesso!")
                return

        print("Empréstimo não encontrado.")

    def relatorio_emprestimos(self):
        if len(self.emprestimos) == 0:
            print("Nenhum empréstimo realizado.")
            return

        for emprestimo in self.emprestimos:
            print("--------------------")
            print("Usuário:", emprestimo.usuario.nome)
            print("Matrícula:", emprestimo.usuario.matricula)
            print("Livro:", emprestimo.livro.titulo)
            print("Código:", emprestimo.livro.codigo)

    def buscar_livro(self):
        nome = input("Título do livro: ").lower()
        encontrado = False

        for livro in self.livros:
            if nome in livro.titulo.lower():
                livro.consultar()
                encontrado = True

        if not encontrado:
            print("Livro não encontrado.")

    def editar_livro(self):
        codigo = input("Código do livro: ")

        for livro in self.livros:
            if livro.codigo == codigo:
                titulo = input("Novo título (Enter para manter): ")
                autor = input("Novo autor (Enter para manter): ")
                livro.editar(titulo, autor)
                print("Livro atualizado!")
                return

        print("Livro não encontrado.")

    def excluir_livro(self):
        codigo = input("Código do livro: ")

        for livro in self.livros:
            if livro.codigo == codigo:
                for emprestimo in self.emprestimos:
                    if emprestimo.livro == livro:
                        print("Não é possível excluir: livro emprestado.")
                        return

                livro.excluir()
                self.livros.remove(livro)
                return

        print("Livro não encontrado.")

    def estatisticas(self):
        print("Total de livros:", len(self.livros))
        print("Total de usuários:", len(self.usuarios))
        print("Empréstimos ativos:", len(self.emprestimos))

        if len(self.livros) > 0:
            maior = self.livros[0]

            for livro in self.livros:
                if livro.emprestimos > maior.emprestimos:
                    maior = livro

            print("Livro mais emprestado:", maior.titulo)
            print("Quantidade de empréstimos:", maior.emprestimos)

    def menu(self):
        while True:
            print("\n--- SISTEMA DE BIBLIOTECA ---")
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
                self.cadastrar_livro()
            elif opcao == "2":
                self.cadastrar_usuario()
            elif opcao == "3":
                self.consultar_livros()
            elif opcao == "4":
                self.emprestar_livro()
            elif opcao == "5":
                self.devolver_livro()
            elif opcao == "6":
                self.relatorio_emprestimos()
            elif opcao == "7":
                self.buscar_livro()
            elif opcao == "8":
                self.editar_livro()
            elif opcao == "9":
                self.excluir_livro()
            elif opcao == "10":
                self.estatisticas()
            elif opcao == "0":
                print("Programa encerrado.")
                break
            else:
                print("Opção inválida!")


biblioteca = Biblioteca()
biblioteca.menu()