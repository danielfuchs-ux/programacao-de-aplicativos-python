#Listas, Tuplas e Dicionários

#1. Listas

#São usadas para armazenar valores dentro de uma única variável.

nomes = ["Ana", "Benjamim", "Corinteas", "Danone"]
print(nomes)

#2. Acessando elementos individualmente na lista.

print(nomes[0])

# Podemos acessar o último elemento usando o -1

print(nomes[-1])

#3. Alterando elementos - Listas são mutáveis, ou seja, é possível alterar seus elementos.

nomes[0] = "Araújo"
print(nomes)

#4. Adicionando elementos. - append() = Adiciona um elemento no fim da lista.

nomes.append("Euclaudiomar")
print(nomes)

# insert() adiciona um item numa posição escolhida pelo programador.

nomes.insert(1, "Joelsiosmar")
print(nomes)

#5. Removendo Elementos - remove() retira um elemento pelo seu nome

nomes.remove("Joelsiosmar")
print(nomes)

#pop() = remove o eçemento pelo índice.

nomes.pop(4)
print(nomes)

#6. Tamanho da lista: len() informa a quantidade de elementos.

print(len(nomes))

#7. Percorrendo uma lista:

for nome in nomes:
    print(nome)

#8. Verificando a existência de um elemento.

if "" in nomes:
    print("Ana está na lista")

else:
    print("Ana não está na lista")


#9. Lista com diferentes tipos de dados.

dados = ["Claudiomar", 18, 1.76, True]
print(dados)

#10. Lista de alunos:

notas = 7.5, 8.0, 6.5, 9.0
soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)
print(f"Media: {media:.1f}")

#11. Tuplas: São semelhantes as listas, mas Tuplas não podem ser alteradas depois de criadasd.

cordenadas = (10, 20)
print(cordenadas)

#Acessando elementos
print(cordenadas[0])
print(cordenadas[1])

#12. Dicionários: Armazenam informações no formato chave: valor

aluno = {

"nome": "Claudiomar",
"idade": 18,
"nota": 7.5
}
print(aluno)

#13. Acessando valores no dicionário

print(aluno["nome"])
print(aluno["idade"])
print(aluno["nota"])

#14. Alterando valores:

aluno["nota"] = 8.5
print(aluno)
