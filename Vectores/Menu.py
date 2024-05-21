import os
os.system("clear")
i = True
producto = []
cantidad = []
valor = []
while i == True :
    print("Menu \n Ingresar \n 1- Crear Producto \n 2--Buscar Producto \n 3--Actualizar Producto \n 4--Eliminar Producto \n 5--Salir")
    opc = int(input("Ingrese una opcion: "))
    os.system("clear")
    if opc == 1 :
        print('Crear Producto')
        apro = input("Ingresa nombre de producto: ").capitalize()
        acan = int(input('Ingresa Cantidad del producto: '))
        avalor = float(input('Ingresar precio del producto: '))

        producto.append(apro)
        cantidad.append(acan)
        valor.append(avalor)
        print("--------------Producto almacenado correctamente---------------")
    elif opc == 2:
        print('Buscar Producto')
        busPro = input("Nombre de producto a buscar: ").capitalize()
        resultado = busPro in producto
        if resultado == True:
            print('---------Producto Encontrado----------')
            elemento = producto.index(busPro)
            print("Nombre Producto: ", producto[elemento])
            print(f'Cantidad del producto: {cantidad[elemento]}')
            print(f'Precio del Producto: {valor[elemento]}')
    elif opc == 3:
        print('Actualizar Datos de producto')
        busPro = input('Ingresar producto a Actualizar: ').capitalize()
        resultado= busPro in producto

        cpro = input("Ingresa nombre de producto: ").capitalize()
        ccan = int(input('Ingresa Cantidad del producto: '))
        cvalor = float(input('Ingresar precio del producto: '))
        elemento = producto.index(busPro)
        producto[elemento] = cpro
        cantidad[elemento] = ccan
        valor[elemento] = cvalor
        print("---------- Producto Actualizado Correctamente -------")
    elif opc == 4 :
        busPro = input("Ingresa producto a Eliminar: ").capitalize()
        resultado = busPro in producto

        if resultado == True:
            print("----Producto encontrado----")
            elemento = producto.index(busPro)

            del producto[elemento]
            del cantidad[elemento]
            del valor[elemento]

            print("Producto eliminado Correctamente")

    elif opc == 5 :
        i= False  
        
    elif opc == 6:
        print(f'{producto}{cantidad}{valor}')    
print('-Salio Correctamente-')