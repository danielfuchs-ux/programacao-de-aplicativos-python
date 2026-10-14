#1. Classe: o modelo (planta).

class Celular:
    def __init__(self, marca, modelo, cor, bateria = 100):
        # Atributos são as características de um objeto.
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

#4. Métodos: São os comportamentos do Objeto.
    def ligar(self):
        #O metodo consulta um atributo do próprio objeto
       if self.bateria == 0:
           print("Sem bateria! Coloque para carregar.")

       else:
           self.ligado = True
           print("Ligado")

    def desligar(self):
        self.ligado = False
        print("Desligado")
        

#5. Objetos: Criados a partir da classe (as casas).

celular1 = Celular("Samsung", "Galaxy s23", "Preto")
celular2 = Celular("Motorola", "Moto g54", "Azul", 50)

#6. Acessando e alterando atributos: usamos objeto.atributo

print(celular1.marca)
print (celular1.modelo)
print (celular2.bateria)

#7. Chamando métodos: usamos objeto.metodo() para pedir que o objeto faça algo.

celular2.ligar()
