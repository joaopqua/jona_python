lista = [1,2,34,67,21,11,16,43,55,10,21,43,56,87]
print(lista[0])
print(lista[0:5])

lista.sort(reverse=True)
print(f'Lista ordena {lista}')

lista.remove(11)#o remove vc tem q passar o valor que vc quer remover da lista, caso tenha dois iguais ele só remove 1
#o pop e o del remove por indice
lista.pop(0)
#o del sera usado o indice do elemento que vc quer eliminar, podendo ser mais de um como 0:5
del lista[0:2]

#função append, adiciona outro valor a sua lista
nome = 'gomes'
lista.append(nome)
print(lista)

#função insert, adiciona outra a sua lista em x posição
lista.insert(2, 'jonas')

#como substituir
lista[2     ] = 'kleber'

#in
print('belo' in lista)

#um dos usos do not é com o in
print('belo' not in lista)


#if else finalmente
if 'kleber' in lista:
    #esse bloco só sera executado se a condição for verdadeira
    print('sim o kleber esta na lista')
else: #esse bloco so sera executado se a condição for falsa
    print('não o kleber não esta na lista')

#função len percorre a lista e conta quantos elementos tem na lista

#função sum soma os valores que tem dentro de uma lista
lista1 = [1,2,3,4,4,7,8,34,87,21]
soma = sum(lista1)
qtdnotas = len(lista1)

media = soma/qtdnotas
