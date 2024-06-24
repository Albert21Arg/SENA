#Escribe un algoritmo que genere una lista de factoriales de los números del 1 al 5.
import math
factoriales = [math.factorial(num) for num in range(1,6)]
print(f"Lista de Factoriales: {factoriales}")