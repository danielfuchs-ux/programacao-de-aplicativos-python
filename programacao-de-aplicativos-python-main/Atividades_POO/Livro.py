class Livro:
    def __init__(self, titulo, autor, num_pg = 0):
        self.titulo = titulo
        self.autor = autor
        self.num_pg = num_pg

    def ler(self):
        lido = input("Quantas páginas foram lidas? ")

        if(lido > self.num_pg):
            print("Digite um número menor ou igual ao número total de páginas do livro.")

        else:
            self.num_pg = self.num_pg - lido

    def porcentagem(self):

        self.num_pg = self.num_pg / 100


