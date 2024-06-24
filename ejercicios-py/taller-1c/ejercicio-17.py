#Escribe un algoritmo que elimine los elementos en posiciones impares de una lista.
lista = [1,2,3,4,5,6,7,8]
lista_pares = [num for i, num in enumerate(lista) if i % 2 == 0]
print(f"lista sin elementos en posiciones impares:{lista_pares}")