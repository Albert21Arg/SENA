def fun_nombres(nombres):
    i = 0
    catidad_nombres = int(input("Cuantos nombres va a ingresar? "))
    nombres =  []
    for i in range(catidad_nombres):
        nombre = input(f'ingresar nombre {i + 1}: ')
        nombres.append(nombre)
    return nombres

def mostrar_nombres(nombres):
    for nombre in nombres:
        print(nombre)
    print(nombres)


if __name__ == '__main__':
    while x == True:
        print(' 1: Agregar nombre \n 2: Ver nombres \n 3: Salir')
        opc = input('Seleccione una de las opciones: ')
        if opc == '1' or opc == "Agregar nombre":
            fun_nombres()
        elif opc == '2' or opc.lower() == "ver lista":
            mostrar_nombres()
        elif opc == '3' or opc == "Salir":
            x = False
    
