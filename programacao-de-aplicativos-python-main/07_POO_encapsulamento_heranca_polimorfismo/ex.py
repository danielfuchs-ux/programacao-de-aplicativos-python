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

    def bonus(self):
        return self.salario * 0.10

#####################################################################################################

class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)
        self.equipe = equipe

    def mostrar_equipe(self):
        print(f"{self.nome} é responsável por {self.equipe} pessoas em sua equipe.")

    def bonus(self):
        return self.salario * 0.20 + self.equipe * 100

######################################################################################################

class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super(). __init__(nome, salario)
        self.curso = curso

    def bonus(self):
        return 200

#####################################################################################################

print("\n ===== Polimorfismo =====")

#Criando funcionarios de diferentes classes:

equipe = [

    Funcionario("Jair", 3000),
    Gerente("Fulano", 8000, 5),
    Estagiario("Jubiscrevaldo", 1500, "Desenvolvimento de Sistemas")

]

#Percorrendo a lista funcionários:

for funcionario in equipe:
    print(f"{funcionario.nome}: R$ {funcionario.bonus()} ")

#####################################################################################################

#3. Polimorfismo:
#O mesmo metodo pode existir em várias classes, mas apresentar comportamentos diferentes, dependendo do objeto que esta executando esse metodo.

#####################################################################################################

