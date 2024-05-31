import os
os.system('clear')
try:
    producto = []
    cantidad = []
    precio = []
    i = True

    while i : 
        print('\n Seleccione una opcion: ')
        x = int(input(' 1-- Salir \n 2-- suma de los elementos de la lista \n 3-- producto de todos los elementos de la lista  \n 4-- Cuántas veces aparece el número 3 en la lista \n 5-- Cuál es el valor máximo y mínimo en la lista \n 6-- Cuál es la lista sin duplicados de lista \n 7-- Cuál es la lista después de intercambiar el primer y último elemento de lista\n 8-- Cuál es la lista después de invertir la sublista lista\n 9-- Cuántos números pares e impares hay en la lista lista \n 10-- Cuál es la cadena concatenada de la lista\n 11-- Cuáles números de la lista\n 12-- Cuál es la suma de los elementos de la sublista\n 13-- Cuál es el promedio de los elementos de la lista \n 14-- Cuáles son los números pares en la lista\n 15-- Cuál es la lista de los cuadrados de los números del 1 al 5\n 16-- El número 3 existe en la lista \n 17-- Cuál es la lista resultante de concatenar lista1 = [1, 2, 3] y lista2 = [4, 5, 6]\n 18-- Cuál es la lista de pares ordenados (tuplas) a partir de lista \n 19-- Cuál es la lista con los primeros 5 números naturales \n 20--  Cuál es la lista de palabras en mayúsculas de palabras = ["HoLa", "MUNDO", "pYThon"]\n' ))
        os.system('clear')
        
        if x == 1 : 
            i=False

        elif x == 2:
            lista = [1, 2, 3, 4, 5]
            lista = sum(lista)
            print(lista)

        elif x == 3 : 
            lista = [1, 2, 3, 4, 5]
            producto = 1
            for numero in lista :
                producto = producto * numero
                print(producto)

        elif x ==  5 :
            lista = [1, 2, 3, 4, 5, 3, 3]
            lista = lista.count(3)
            print(lista)

        elif x == 4 :
            lista = [1, 2, 3, 4, 5]
            maximo = max(lista)
            minimo = min(lista)
            print(f"maximo en la lista {maximo}")
            print(f"minimo en la lista {minimo}") 

        elif x == 6 :
            lista = [1, 2, 3, 4, 5, 3, 3]  
            lista = list(set(lista))
            print(lista)

        elif x == 7 :
            lista = [1, 2, 3, 4, 5]
            lista[0], lista[-1] = lista[-1], lista[0]
            print(lista)

        elif x == 8 :
            lista = [1, 2, 3, 4, 5]
            sublista = lista[1:4]
            sublista.reverse()
            lista[1:4] = sublista
            print(lista)

        elif x == 9 :
            lista = [1, 2, 3, 4, 5]
            pares = len([num for num in lista if num % 2 == 0])
            impares = len([num for num in lista if num % 2 != 0])   
            print(f'Pares {pares}')
            print(f'Impares {impares}')

        elif x == 10:
            frutas = ["manzana", "banana", "cereza", "dátil", "fresa"]
            ''.join(frutas)
            print(frutas)

        elif x == 11 : 
            lista = [1, 2, 3, 4, 5]
            lista = [num for num in lista if num > 3]
            print(lista)

        elif x == 12:
            lista = [1, 2, 3, 4, 5]       
            lista = [num for num in lista if num > 3]
            print(lista)

        elif x == 13: 
            lista = [1, 2, 3, 4, 5]
            lista = sum(lista[1:4])
            print(lista)
        
        elif x == 14:
            lista = [1, 2, 3, 4, 5]
            lista = sum(lista) / len(lista)
            print(lista)

        elif x == 15:
            lista = [1, 2, 3, 4, 5]    
            lista = [num for num in lista if num % 2 == 0]
            print(lista)

        elif x == 16:
            lista = [num**2 for num in range(1, 6)]
            print(lista) 

        elif x == 17 : 
            lista =   [-num for num in range(1, 11)]
            print(lista) 

        elif x == 18:
            lista1 = [1, 2, 3] 
            lista2 = [4, 5, 6]
            print(lista1 + lista2)

        elif x == 19:
            lista1 = [1, 2, 3]
            lista2 = ['a', 'b', 'c']
            lista = list(zip(lista1, lista2))
            print(lista)
        elif x == 20:
            palabras = ["HoLa", "MUNDO", "pYThon"]
            lista = [palabra.upper() for palabra in palabras]
            print(lista)

except:
    print('Error: Ingresar Valor de la lista. ')