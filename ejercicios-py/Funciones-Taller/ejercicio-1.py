#Ejercicio 1.-Crear un array unidimensional de 20 elementos con nombres de personas.
#Visualizar los elementos de la lista debiendo ir cada uno en una fila distinta.
def creacionUsuarios():
    for i in range(n):
        nombre = input (f" Nombre {i + 1}: ")
        nombres.append(nombre)

def nombreIngresados():
    print ("\nLista de nombres introducidos:")
    for nombre in nombres:
        print(nombre)

if __name__ == '__main__':
    nombres = []
    n = int (input ("¿Cuántos nombres deseas introducir? "))
    usuarios = creacionUsuarios()
    #resultados = nombreIngresados()
    print(f"{nombreIngresados()}")