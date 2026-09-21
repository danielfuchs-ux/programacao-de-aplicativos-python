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



