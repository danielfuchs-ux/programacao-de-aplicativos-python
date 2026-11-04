class Personagem:
    def __init__(self, nome, vida = 100):
        self.nome = nome
        self.__vida = vida
        self.vida_player = vida

    def receber_dano(self):

        dano = input("Digite o valor do dano: ")
        dano_int = int(dano)
        if dano_int < 0:
            print("Dano menor do que zero, inválido.")

        if self.vida_player - dano_int < 0:
            print("O Player não tem vida suficiente para tomar tanto dano, portanto a vida ficará no mínimo possível.")
            self.vida_player = 0
            print(f"{self.nome}: {self.vida_player} hp")

        else:
            self.vida_player = self. vida_player - dano_int
            print(f"{self.nome}: {self.vida_player} hp")

    def curar(self):

        cura = input("Digite o valor da cura: ")
        cura_int = int(cura)
        if cura_int < 0:
            print("Cura menor do que zero, inválida.")

        if self.vida_player + cura_int > 100:
            print("O Player não tem vida suficiente para receber tanta cura, portanto ela voltou ao status máximo.")
            self.vida_player = 100
            print(f"{self.nome}: {self.vida_player} hp")

        else:
            self.vida_player = self.vida_player + cura_int
            print(f"{self.nome}: {self.vida_player} hp")

    def  status(self):
        print(self.nome)
        print(self.vida_player)

    def atacar(self):
        ataque = 10
        print(f"{self.nome} causou {ataque} pontos de dano!")

##############################################

class Guerreiro(Personagem):
    def __init__(self, nome, vida=100, forca = 15):
            super().__init__(nome, vida)
            self.forca = forca

    def atacar(self):
        ataque = 10 + self.forca
        print(f"{self.nome} causou {ataque} pontos de dano!")

##############################################

class Mago(Personagem):
    def __init__(self, nome, vida=100, mana = 50):
        super().__init__(nome, vida)
        self.mana = mana

    def magia(self):
        print(self.mana)

    def atacar(self):

        ataque = 10

        if self.mana >= 10:
            ataque = ataque + 25
            self.mana = self.mana - 10
            print(f"{self.nome} causou {ataque} pontos de dano!")

        else:
            ataque = 5
            print(f"{self.nome} causou {ataque} pontos de dano!")

##############################################

Mesa = [

    Personagem("Joelson", 100),
    Guerreiro("Jair do Cavalo", 100),
    Mago("Jubiscrevaldo", 100),

]

for Personagem in Mesa:
    print(f"{Personagem.nome}: {Personagem.vida_player} hp")
    Personagem.receber_dano()
    Personagem.curar()
    Personagem.atacar()
    print("\n")