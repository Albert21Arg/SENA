#Sumar Elementos Pares
#Escribe un algoritmo que sume todos los elementos pares de una lista de números enteros.
lista = [1,2,3,4,5,6]
sumas_pares = sum(num for num in lista if num % 2 == 0)
print(f"la suma de los elemontos pares es : {sumas_pares}")