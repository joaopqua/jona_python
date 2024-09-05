lista = [1,2,3,4,5,6,7,8,9,10]

print(lista[-1])
#indice negativo le a lista ao contrario

lista1 = [10,20,21,32,11,9,6,3,16,1,33]
print(lista1)
lista1.sort()
print(lista1)
lista1.sort(reverse=True)

print(lista1)

#remove, pop, del 

lista1.remove(1)

nomes = ['joao', 'kaua', ' kayros', 'tiago', 'juan ', 'belo', 'bruno']
nomes.pop(1)
nomes.pop(-2)
print(nomes)
del nomes[2:4] #remove mais de um elemento da lista
print(nomes)

nomes1 = []
novo_nome = input('digite um novo nome: ')
nomes1.append(novo_nome)
print(nomes1)

