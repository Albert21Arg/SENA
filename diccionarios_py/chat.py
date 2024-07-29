import ejecicios
if __name__ == '__main__':
    nombres = []
    x = True
    while x:
        print(' 1: Agregar nombre \n 2: Ver nombres \n 3: Salir')
        opc = input('Seleccione una de las opciones: ')
        if opc == '1' or opc.lower() == "agregar nombre":
            ejecicios.fun_nombres()
        elif opc == '2' or opc.lower() == "ver lista":
            ejecicios.mostrar_nombres(nombres)
        elif opc == '3' or opc.lower() == "salir":
            x = False
        else:
            print("Opción no válida. Inténtelo de nuevo.")