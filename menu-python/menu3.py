import os
productos = {}

def crear():
    nombre = input('ingresar nombre: ')
    if nombre in productos:
        print('ya existe.')
    else:
        cantidad = input('cantidad: ')
        precio = input('precio: ')

        productos[nombre]={
            'cantidad':cantidad,
            'precio':precio
        }
        print(productos)

def ver():
    if productos:
        for nombre,x in productos.items():
            print('-nombre:',nombre,'-cantidad:',x['cantidad'],'-precio:',x['precio'])
    else:
        print('NO HAY DATOS.')

def actualizar():
    nombre = input('nombre: ')
    if nombre in productos:
        nombreN = input('Nuevo nombre: ').capitalize()
        cantidad = input('Nueva cantidad: ')
        precio = input('Nuevo precio: ')

        if nombre:
            productos[nombreN]= productos.pop(nombre)
            productos[nombreN]['nombreN']=nombreN
        
        if cantidad:
            productos[nombreN]['cantidad']=cantidad

        if precio:
            productos[nombreN]['precio']=precio

        print(productos)
    else:
        print('no existe.')

def eliminar():
    nombre = input('Ingresar nombre: ')
    if nombre in productos:
        del productos[nombre]
    else:
        print('nombre no existe.')
        print(ver())

if __name__ == '__main__':
    x = True
    os.system('clear')
    while x == True:
        print('1: crear \n2: ver \n3: actualizar \n4: eliminar \n5: salir')
        r = int(input('ingresar una opcion: '))
        os.system('clear')
        
        if r <= 5 :
            if r == 1:
                crear()
            if r == 2:
                ver()
            if r == 3:
                actualizar()
            if r == 4:
                eliminar()
            if r == 5:
                x = False
        else:
            print('fuera de rango.')    