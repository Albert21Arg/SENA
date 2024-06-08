#lista = [1,2,3,4,5]
#suma = sum(lista)
#print(suma)
#producto = 1

#for numero in lista :
#    producto = producto * numero

#print(producto)
#maximo = max(lista)
#minimo = min(lista)

print(maximo)
print(minimo) 
#-----------------------------
#lista = [1, 2, 3, 4, 5, 3, 3]
#listaOrden = list(set(lista))
#print(listaOrden)

#lista[0], lista[-1] = lista[-1], lista[0]

#sublista = lista[1:4]
#sublista.reverse()
#lista[1:4]= sublista

#print(sublista)
#pares = len([num for num in lista if num % 2 == 0])
#impares = len([num for num in lista if num % 2 != 0])

#print(pares)
#print(impares)
#frutas = ["manzana", "banana", "cereza", "dátil", "fresa"]
#"".join(frutas)
#print(frutas)
#lista = [num for num in lista if num > 3]
#lista = [-num for num in range(1, 11)]
#lista1 = [1, 2, 3] 
#lista2 = [4, 5, 6]
#print(lista1 + lista2)

#lista1 = [1, 2, 3]
#lista2 = ['a', 'b', 'c']
#lista = list(zip(lista1, lista2))
#
# lista = list(range(1, 6))
palabras = ["HoLa", "MUNDO", "pYThon"]
lista = [palabra.upper() for palabra in palabras]
print(lista)


        elif x > 21 or x <= 0 :
             print('Error: Ingresar Valor de la lista. ')
        
except:
    print('Error: Ingresar Valor de la lista. ')