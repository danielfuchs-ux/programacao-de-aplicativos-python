# O que é uma função:

#Uma função é um bloco do código criado para realizar uma determinada tarefa.
#Ela permite organizar e reutilizar código.

#1. Criando uma função: Utilizar a palavra def para criar uma função.

def saudacao():
    print("Olá, seja bem vindo! \n")

#Para executar a função, chamamos seu nome.

saudacao()

#2. Função com parâmetro

def saudacao2(nome):
    print(f"olá, {nome}")

saudacao2("Daniel")

#3. Mais de um parâmetro

def apresentar(nome, idade):
    print(f"nome: {nome}")
    print(f"idade: {idade}")

apresentar("Daniel", 17)

#4. Função com cálculo:

def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"resultado: {resultado}")

somar(10,20)

#5. Retornando um valor: O return devolve um valor para o local onde a função foi chamada.

def somar(numero1, numero2):
    return numero1 + numero2

resultado = somar(10,20)
print(resultado)

#6. Função com condição:

def verificarIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

resultado = verificarIdade(20)
print(resultado)

resultado = verificarIdade(17)
print(resultado)

#7. Parâmetro com valor padrão: Podemos definir um valor padrão para um parâmetro.

def saudacao(nome = "Aluno"):
    print(f"Olá, {nome}")

saudacao()
saudacao("Joelson")

#8. Varios parâmetros

def calcularMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

calcularMedia(8,7,9)
print(calcularMedia(8,7,9))

#9. Funções para organizar um programa:

def cadastraProdutos():

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço:"))
    return nome, preco

def exibirProduto(nome, preco):
    print("\n ===== Produto =====")
    print(f"Nome: {nome}")
    print(f"Preço: R${preco}")

nome, preco = cadastraProdutos()

exibirProduto(nome, preco)
