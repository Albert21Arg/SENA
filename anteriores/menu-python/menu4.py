import os
numeros = {}
def crear():
    numero = int(input('numero: '))
    if numero in numeros:
        print('numero ya existe.')
    else:
        print(numero)

        numeros[numero]={

        }
def ver():
    if numeros:
        for numero,x in numeros.items():     
            print('numero:',numero)   
def actualizar():
    numero = int(input('ingresar numero.'))
    if numero in numeros:
        numerov = int(input('nuevo valor: '))

        if numero :
            numeros[numerov] = numeros.pop(numero)
            
def eliminar():
    numero = int(input('Numero a eliminar: '))
    if numero in numeros:
        del numeros[numero]

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