import os
empleados = {}
def crear():
    cedula = input('ingrese documento empleado: ')
    if cedula in empleados:
        print('usuario ya existe.')
    else:
        nombre = input('nombre: ')
        apellido = input('apellido: ')
        telefono = int(input('telefono: '))

        empleados[cedula]={
            'nombre':nombre,
            'apellido':apellido,
            'telefono':telefono
        }
        print(empleados)

def ver():
    if empleados:
        for cedula,valor in empleados.items():
            print('cedula:',cedula,'nombre:',valor['nombre'],'apellido:',valor['apellido'],'telefono:',valor['telefono'])
    else:
        print('NO HAY DATOS.')

def actualizar():
    cedula = input('ingresar documentos: ')
    if cedula in empleados:
        nombre = input('Ingresar nombre: ')
        apellido = input('Ingresar apellido: ')
        telefono = int(input('Ingresar telefono: '))

        if nombre:
            empleados[cedula]['nombre']=nombre
        if apellido:
            empleados[cedula]['apellido']=apellido
        if telefono:
            empleados[cedula]['telefono']=telefono
        print(empleados)
    else:
        print('Usuario no existe.')
def eliminar():
    cedula = input('Ingresar cedula: ')
    if cedula in empleados:
        del empleados[cedula]
        print(empleados)
    else:
        print('no existe.')    

if __name__ == '__main__':
    x = True
    os.system('clear')
    while x == True:

        print('1: crear \n2: ver \n3: actualizar \n4: eliminar \n5: salir')
        opc = int(input('ingresar una opcion: '))
        os.system('clear')

        if opc == 1:
            crear()
        elif opc == 2:
            ver()
        elif opc == 3:
            actualizar()
        elif opc == 4:
            eliminar()
        elif opc == 5:
            x = False
        else:
            print('Fuera de Rango.')