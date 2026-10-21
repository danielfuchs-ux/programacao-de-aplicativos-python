class Player:
    def __init__(self, username, classe, vida = 100, nivel = 1):
        self.username = username
        self.classe = classe
        self.vida = vida
        self.nivel = nivel

    def dano(self):

        dano = input("Quanto de dano foi tomado?")

        if self.vida < dano:

            print("Player derrotado.")

        else:

            self.vida = self.vida - dano

    def curar(self):

        cura = input("Quanto cura foi recebido?")

        self.vida = self.vida + cura

        if self.vida > 100:

            self.vida = 100

    def level_up(self):

        self.nivel = self.nivel + 1
        self.vida = 100

    def status(self):
        print(self.username)
        print(self.classe)
        print(self.vida)
        print(self.nivel)


player1 = Player("Nome", "Mago", 100, 1)
player1.dano()
player1.curar()
player1.level_up()
player1.status()

player2 = Player("User", "Bárbaro", 100, 1)
player2.dano()
player2.curar()
player2.level_up()
player2.status()