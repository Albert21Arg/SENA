#Encontrar Elementos Comunes
#Escribe un algoritmo que encuentre los elementos comunes entre dos listas y los muestre.
lista1 = [1,2,3,4,5]
lista2 = [4,5,6,7,8]
comunes = list(set(lista1)& set(lista2))
print(f"Elementos Comunes: {comunes}")