class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self):

        adicionar = input("Quanto será adicionado para a conta?")

        self.saldo = self.saldo + adicionar

    def sacar(self):

        valor = input("Quanto deseja sacar?")

        if valor > self.saldo:

            print("Saldo insuficiente")

        else:

            self.saldo = self.saldo - valor

    def extrato(self):
        print(self.titular)
        print(self.saldo)


titular1 = ContaBancaria("Afonso", 0)
titular2 = ContaBancaria("Jeremias", 500)

titular1.depositar()
titular1.sacar()
titular1.extrato()

titular2.depositar()
titular2.sacar()
titular2.extrato()