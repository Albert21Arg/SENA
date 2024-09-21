import os
frutas = {}
def crear_producto():
    nombre = input('Ingresar nombre: ')
    if nombre in frutas:
        print('Esta fruta ya existe.')
    else:
        cantidad = input('catidad: ')
        precio = input('precio: ')

        frutas[nombre]={
            'cantidad':cantidad,
            'precio': precio
        
        }
        print(frutas)

def ver_lista():
    if frutas:
        for nombre,valor in frutas.items():
            print('nombre:', nombre,'cantidad:',valor['cantidad'],'precio:',valor['precio'])

def actualizar():
    nombre = input('Ingresar nombre: ')
    if nombre in frutas:
        nombreNuevo= input('Nuevo nombre: ')
        cantidad = input('Nueva cantidad: ')
        precio = input('Nuevo precio: ')

        if nombre:
            frutas[nombreNuevo]= frutas.pop(nombre)
            frutas[nombreNuevo]['nombre']= nombreNuevo
        if cantidad:
            frutas[nombreNuevo]['cantidad'] = cantidad
        if precio:
            frutas[nombreNuevo]['precio']= precio
    else:
        print(f'fruta {nombre} no existe.')

def eliminar():
    nombre = input('ingrese nombre a eliminar: ')
    if nombre in frutas:
        del frutas[nombre]
    else:
        print('nombre no existe.')
        print(ver_lista())
if __name__== '__main__':
    x  = True
    os.system('clear')
    
    while x == True :        
        print('1: Crear \n2: Ver listas \n3: Actualizar \n4: Eliminar \n5: Salir')
        opc = int(input('-Seleccione una opcion: '))
        os.system('clear')
        if opc in range(1,5) :
            if opc == 1:
                crear_producto()
            elif opc == 2 :
                ver_lista()
            elif opc == 3:
                actualizar()
            elif opc == 4:
                eliminar()
            elif opc == 5:
                x = False
        else:
            print('opcion fuera de rango.')
    print('salio correctamente.')