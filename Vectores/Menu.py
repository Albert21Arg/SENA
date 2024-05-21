import os
os.system("clear")
i = True
producto = []
cantidad = []
valor = []
while i == True :
    os.system("clear")
    print("Menu \n Ingresar \n 1- Crear Producto")
    opc = int(input("Ingrese una opcion: "))
    if opc == 1 :
        print('Crear Producto')
        apro = input("Ingresa nombre de producto: ").capitalize()
        acan = int(input('Ingresa Cantidad del producto: '))
        avalor = float(input('Ingresar precio del producto: '))

        producto.append(apro)
        cantidad.append(acan)
        valor.append(avalor)
        print("---------------Producto almacenado correctamente---------------")
    elif opc == 3 :
        i= False  
print(f'{producto}{cantidad}{valor}')