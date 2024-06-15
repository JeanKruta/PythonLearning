#Tipod de listas

lista = [1, 2, 3, 4, 5]

lista2 = [] #lista vazia
lista2 = list() #lista vazia

lista_de_listas = [True, "Jean",[10, "JeanK", 7.5, False], 10, 50]

#append (Adiciona um elemento no final)
print("Lista antes do append: ", lista)

lista.append(7)
print("Lista depois do Append: ", lista)

#insert (adiciona um elemento em qualquer posição)

lista.insert(3, 21)
print("Lista após o insert: ", lista)

#extend (junta duas listas)

lista3 = [80, 77, 66]

lista.extend(lista3)
print("Lista após o extend", lista)

#pop (remove o últim elemento por padrão)

lista.pop()
print("Lista com pop padrão: ", lista)

lista.pop(0)
print("Lista após remoção do primeiro elemento: ", lista)

#remove (remove o elemento que você citou)

lista.remove(21)
print("Lista após remove: ", lista)

#count serve para contar quantas vezes um elemento aparece

print(lista.count(5))

#index mosta o índice de um elemento(posição da lista do elemento)

print(lista.index(4))

#sort (ordena a lista de forma crescente)

lista.sort()
print(lista)

lista.sort(reverse=True) #ordenação decrescente
print(lista)

#sum (soma todos os elementos dentro de uma lista)
print(sum(lista))

#max (retorna o maior valor)
print(max(lista))

#min (retorna o menor valor da lista)
print(min(lista))