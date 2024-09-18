import os
def menu():
    print("1: Crear")
    print("2: ver")
    print("3: actualizar")
    print("4: eliminar")
    print("5: buscar")
    print ("6: Ordenar A-Z")
    print ("7: Ordenar Z-A")
    print("8: Salir")
personas = {}
def crear():
    try:
        nombre = input('Nombre: ').capitalize()
        if nombre in personas:
            print('Nombre Ya existe.')
        else:
            edad = input('Edad: ')
            ciudad = input('Ciudad: ').capitalize()
            
            personas[nombre]={
                'edad':edad,
                'ciudad':ciudad
            }
            print(f'Nombre: {nombre},{personas[nombre]} \n se creo correctamente.')
    except:
        print('caracter incorrecto.')
        
   
def ver():
    if personas:
        for nombre, x in personas.items():
            print("-Nombre:",nombre ,'-Edad:', x['edad'],'-Ciudad:',x['ciudad'] )
    else:
        print('Lista vacia.')
    
def actualizar():
    nombre = input('nombre: ').capitalize()
    if nombre in personas :
        edad = input('Ingresar nueva edad: ')
        ciudad = input('Ingresar nueva ciudad: ')
        
        if edad:
            personas[nombre]['edad']=edad
        
        if ciudad:
            personas[nombre]['ciudad']=ciudad
        print(personas[nombre])
    else:
        print('Nombre no existe.')    

def eliminar():        
    nombre = input('nombre a eliminar: ').capitalize()
    if nombre in personas:
        del personas[nombre]
        
        print('Se elimino correctamente.')
    else:
        print(f'El nombre {nombre} no existe.')

def buscar():
    nombre = input('nombre a busacar: ').capitalize()
    if nombre in personas :
        print(f"Nombre: {nombre} {personas[nombre]}")

def ordenar_az():
    if personas:
        ordenarAZ = sorted(personas.items(), key=lambda x: x[0])
        for nombre, y in ordenarAZ:
            print(f"nombre: {nombre}, Edad: {y['edad']}, Ciudad: {y['ciudad']} " )
            
def ordenar_za():
    if personas:
        ordenarZA = sorted(personas.items(), key=lambda x: x[0], reverse=True)
        for nombre, y in ordenarZA:
            print(f"nombre: {nombre}, Edad: {y['edad']}, Ciudad: {y['ciudad']} " )
if __name__ == '__main__':
    x = True
    while x == True:
        try:
            menu()
            opc = int(input('Elegir una de las opciones: '))
            os.system('cls')
            if opc in range(1,9):
                if opc == 1 :
                    crear()
                if opc == 2 :
                    ver()
                if opc == 3 :
                    actualizar()
                if opc == 4 :
                    eliminar()
                if opc == 5 :
                    buscar()
                if opc == 6 :
                    ordenar_az()
                if opc == 7 :
                    ordenar_za()
                if opc == 8 :
                    x = False
            else:
                print(f' Opcion {opc} fuera de rango.')
        except:
            print('opcion incorrecta')
            os.system('cls')
    print('Salio correctamente del programa.')
