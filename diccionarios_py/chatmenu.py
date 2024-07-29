def fun_nombres(nombres):
    # Pedimos al usuario cuántos nombres va a ingresar
    cantidad_nombres = int(input("¿Cuántos nombres va a ingresar? "))
    # Recorremos la cantidad de nombres que el usuario va a ingresar
    for i in range(cantidad_nombres):
        # Pedimos el nombre y lo agregamos a la lista
        nombre = input(f'Ingresar nombre {i + 1}: ')
        nombres.append(nombre)
    return nombres

def mostrar_nombres(nombres):
    # Mostramos cada nombre en la lista
    for nombre in nombres:
        print(nombre)
    # Mostramos la lista completa
    print(nombres)

if __name__ == '__main__':
    nombres = []
    x = True
    while x:
        print(' 1: Agregar nombre \n 2: Ver nombres \n 3: Salir')
        opc = input('Seleccione una de las opciones: ')
        if opc == '1' or opc.lower() == "agregar nombre":
            fun_nombres(nombres)
        elif opc == '2' or opc.lower() == "ver lista":
            mostrar_nombres(nombres)
        elif opc == '3' or opc.lower() == "salir":
            x = False
        else:
            print("Opción no válida. Inténtelo de nuevo.")
