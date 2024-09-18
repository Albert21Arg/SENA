telefono = {}
def crear():
    numero = int(input('numero: '))
    if numero in telefono:
        print(f'{numero} ya existe.')
    else: 
        telefono[numero]={

        }

def ver():
    if telefono:
        for numero,x in telefono.items():
            print('Telefono',numero)

def actualizar():
    numero = int(input('ingresar numero: '))
    if numero in telefono :
        numeroN = int(input('Ingresar nuevo numero: '))
        
        if numero:
            telefono[numeroN]=telefono.pop(numero)
    else:
        print('Numero no existe.')
    
    print(telefono)

def eliminar():
    numero = int(input('Ingresar numero a eliminar: '))
    if numero in telefono:
        del telefono[numero]

if __name__ == '__main__':
    x = True
    while x == True:
        print(' 1: \n 2: \n 3 \n 4: \n 5:')
        opc = int(input('seleciona una opcion: '))
        if opc <= 5 :
            if opc == 1 :
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
            print('fuera de rango.')

        print('Saliste del programa.')