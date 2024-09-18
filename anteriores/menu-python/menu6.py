import os
productos = {}

def crear():
    nombre = input('Nombre producto: ').capitalize()
    if nombre in productos:
        print('Producto ya existe.')
    else:
        cantidad = (input('Ingrese la cantidad: '))
        precio = (input('ingrese el precio: '))
        
        productos[nombre] = {
            'cantidad' : [cantidad],
            'precio' : [precio]
        }
        print(productos)

def ver():
    if productos:
        for nombre,x in productos.items():
            print('nombre:',nombre,'cantidad:',x['cantidad'],'precio:',x['precio'])
    else:
        print('Lista vacia.')

def actualizar():
    nombre = input('ingresar nombre a actualizar: ').capitalize()
    if nombre in productos:
        #nombren = input('nuevo nombre: ').capitalize()
        cantidad = (input('ingresar nueva cantidad: '))
        precio = (input('ingresar nuevo precio: '))
        
        ''' if nombren != " ":
            productos[nombren]= productos.pop(nombre)
            productos[nombren]['nombren']=nombren'''
        
        if cantidad :
            productos[nombre]['cantidad']=cantidad
        
        if precio :
            productos[nombre]['precio']=precio
    else:
        print('el producto no existe.')

def eliminar():
    nombre = input('ingresar nombre a eliminar: ') 
    if nombre in productos:
        del productos[nombre]
    else:
        print('el producto no existe.')      

if __name__ == '__main__': 
    x = True
    while x == True:
        print('1: crear \n2: ver \n3: actualizar \n4: eliminar \n5: salir')      
        
        opc = int(input('Elige una de las opciones: '))
        os.system('cls')
        #os.system('clear')
        if opc in range(1,5):
            if opc == 1:
                crear()
            if opc == 2:
                ver()
            if opc == 3:
                actualizar()
            if opc == 4:
                eliminar()
            if opc == 5:
                x = False
        else:
            print('Opcion fuera de rango.')
            

                
        