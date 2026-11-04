#1. Encapsulamento: Proteger o salário para que ele só mude seguindo regras

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario #Privado: Dois Underlines (__)

    def apresentar(self):
        print(f"Sou {self.nome} e ganho {self.salario} reais")

    @property
    def salario(self):
        return self.__salario

    def dar_aumento(self, porcentagem):

        if porcentagem <= 0:
            print(f"Aumento inválido para {self.nome}")
            return
        self.__salario = self.__salario * (1 + porcentagem / 100)
        print(f"{self.nome} recebeu {porcentagem}% de aumento.")

class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)
        self.equipe = equipe

    def mostrar_equipe(self):
        print(f"{self.nome} é responsável por {self.equipe} pessoas em sua equipe.")

class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super(). __init__(nome, salario)
        self.curso = curso

###################################################################

Fulano = Gerente("Fulano", 8000, 5)
Fulano.apresentar()
Fulano.mostrar_equipe()

Jair = Funcionario("Jair", 3000)
Jair.apresentar()

Jubiscrevaldo = Estagiario("Jubiscrevaldo", 1500, "Desenvolvimento de Sistemas")
Jubiscrevaldo.apresentar()
