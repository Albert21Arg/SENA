#Crear una Lista con Elementos Elevados al Cubo
#Escribe un algoritmo que genere una lista donde cada elemento sea el cubo de los números del 1 al 10.
cubos = [num **3 for num in range(1,11)]
print(f"lista de cubos {cubos}")