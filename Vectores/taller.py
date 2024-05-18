#CREAR UNA LISTA
lista = [1,2,3,4,5]
print(lista)
#Acceder al Tercer Elemento
print(lista[2])
#Modificar el Segundo Elemento
lista[1]= 10
print(lista)
#Agregar un Elemento
lista.append(6)
print(lista)
#Eliminar un Elemento por Valor
lista.remove(3)
print(lista)
#Eliminar un Elemento por Índice
i=0
del lista[i]
print(lista)
#Longitud de la Lista
print(len(lista))
#Extender la Lista
lista.extend([7, 8, 9])
print(lista)
#Insertar un Elemento
lista.insert(0, 0)
print(lista)
#Limpiar la Lista
lista.clear()
print(lista)
#Revertir la Lista
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)
#Ordenar la Lista
lista_desordenada = [5, 3, 1, 4, 2]
lista_desordenada.sort()
print(lista_desordenada)
#Índice de un Elemento
indice = lista_desordenada.index(4)
print(indice)
#Último Elemento con `pop()`
ultimo = lista_desordenada.pop()
print(ultimo)
print(lista_desordenada)
#Crear Lista de Listas
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lista_de_listas)
#Acceder a Elementos de Sublistas
print(lista_de_listas[0][0])
