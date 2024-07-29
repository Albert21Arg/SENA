lista = [1,2,3,4,5,6,7]
lista[3] = "Albert"
#insertar al final
lista.append("Taborda")
#insertar en una posicion
lista.insert(3,'Gomez')
print (lista)
#eliminar por valor (nombre)
lista.remove(2)
print(lista)
#eliminar por indice 0,1...
del lista[4]
print(lista)
#len(nombre lista) para la longitud
print(len(lista))
#Las listas si se pueden modificar las tuplas no