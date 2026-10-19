class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(self.nome, "diz: Au au!")

    def info(self):
        print(self.nome)
        print(self.raca)
        print(self.idade)

cachorro1 = Cachorro("Rex", "Vira-Lata", 6)
cachorro2 = Cachorro("Princesa", "Pinscher", 3)

cachorro1.latir()
cachorro1.info()

cachorro2.latir()
cachorro2.info()
