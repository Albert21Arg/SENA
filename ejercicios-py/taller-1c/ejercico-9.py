#Intercalar Elementos de dos Listas
#Escribe un algoritmo que intercale los elementos de dos listas de igual longitud.
lista1 = [1,3,5]
lista2 = [2,4,6]
lista_intercalada = [None]*(len(lista1)+len(lista2))
lista_intercalada[::2] = lista1
lista_intercalada[1::2] = lista2
print(f"lista intercalada: {lista_intercalada}")