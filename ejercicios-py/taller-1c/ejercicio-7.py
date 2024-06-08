#Remover Elementos Negativos
#Escribe un algoritmo que elimine todos los elementos negativos de una lista de números.
lista = [1,-2,3,-4,5,-6]
lista_positiva = [num for num in lista if num >= 0]
print(f"lista sin elementos negativos: {lista_positiva}")