#1. Encapsulamento: Proteger o salário para que ele só mude seguindo regras

class Funcionario:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.__saldo = saldo #Privado: Dois Underlines (__)

    def apresentar(self):
        print(f"Sou {self.nome} e ganho {self.salario}")

##################################################################

Jair = Funcionario("Jair", 3000)
