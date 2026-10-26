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

##################################################################

Jair = Funcionario("Jair", 3000)
Jair.apresentar()