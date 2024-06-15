#1 crear lista
lista = [1, 2, 3, 4, 5]
print(lista)
#2 muestra espacio en lista
print(lista[2])´
#3 modifica elemento ()
lista[1] = 10
print(lista)
#4 agrega elemento ()
lista.append(6)
print(lista)
#5 Elimina un elemento por valor ()
busca=3
lista.remove(busca)
print(lista)
#6 elimina un elemento por indice []
i=0
del lista[i]
print(lista)
#7 muestra longitud de la lista
print(len(lista))
#8 xtiende la lista  ([])
lista.extend([7, 8, 9])
print(lista)
#9 inserta un elemento (,)
lista.insert(0, 0)
print(lista)
#10 limpia la lista ()
lista.clear()
print(lista)
#11 Revertir lista 
lista = [1, 2, 3, 4, 6]
lista.reverse()
print(lista)
#12 ordenar lista
lista_desordenada = [5, 3, 1, 4, 2]
lista_desordenada.sort()
print(lista_desordenada)
#13 Encuentra y muestra el indice del numero () en la lista.
indice = lista_desordenada.index(4)
print(indice)
#14 muestra y elimina el ultimo elemento de la lista usando pop()
ultimo = lista_desordenada.pop()
print(ultimo)
print(lista_desordenada)
#15 crea una lista con mas lista 
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lista_de_listas)
#16 Buscar en la lista y sublista
print(lista_de_listas[0][0])
#17 añade una sublista append()
lista_de_listas.append([10, 11, 12])
print(lista_de_listas)
#18 fusiona dos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(lista1)
#19 ordena los string de forma alfabetica
frutas = ["manzana", "banana", "cereza", "dátil", "fresa"]
frutas.sort()
print(frutas)
#20 elimina usando pop()
elemento_eliminado = frutas.pop(1)
print(elemento_eliminado)
print(frutas)
#21 elimina usando "nombrelista".clear()
frutas.clear()
print(frutas)''



