#Encontrar el Segundo Mayor Número
#Escribe un algoritmo que encuentre el segundo mayor número en una lista de números.
lista = [1, 2, 3, 4, 5]
mayor = max(lista)
lista_sin_mayor = [num for num in lista if num != mayor]
segundo_mayor = max(lista_sin_mayor)
print("El segundo mayor número es:", segundo_mayor)