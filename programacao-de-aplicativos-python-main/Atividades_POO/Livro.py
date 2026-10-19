class Livro:
    def __init__(self, titulo, autor, total_pg):
        self.titulo = titulo
        self.autor = autor
        self.total_pg = total_pg



    def pg_lidas(self):

        pg = input("Digite a quantidade de páginas lidas: ")
        total = self.total_pg
        if pg > total:
            print("Digite um número de páginas menor que o total do livro.")

        else:
            total = total - pg
            return total

    def porcentagem_lida(self):

        porcentagem = total / 100
        return porcentagem

    def pg_restantes(self):

        restante = self.total_pg - total
        return restante

    def terminou(self):

        if restante == 0:

            acabou = bool
            acabou = True
            return acabou

        else:

            acabou = False
            return acabou

livro1 = Livro("Os três Porquinhos", "Irmãos Grim", 150)
livro2 = Livro("Guia de Redstone", "Minecraft", 100)

livro1.pg_lidas()
livro1.porcentagem_lida()
livro1.pg_restantes()
livro1.terminou()

livro2.pg_lidas()
livro2.porcentagem_lida()
livro2.pg_restantes()
livro2.terminou()




