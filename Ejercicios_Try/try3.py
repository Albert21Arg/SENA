3
'''Elabore un algoritmo que solicite un número entero y muestre un mensaje indicando 
la vocal correspondiente, considerando que la vocal (A=1 )'''
try:
    vocal = int(input('Ingresar un numero de uno a 5.'))
    if vocal == 1 :
        print(f'El numero ingresado ({vocal}) = A')
    elif vocal == 2:
        print(f'El numero ingresado ({vocal}) = E')
    elif vocal == 3:
        print(f'El numero ingresado ({vocal}) = I')
    elif vocal == 4:
        print(f'El numero ingresado ({vocal}) = O')
    elif vocal == 5:
        print(f'El numero ingresado ({vocal}) = U') 
    else:
        print(f'El numero ingresado ({vocal}) Esta fuera de rango')    
except:
    print('Error: ingrese un valor valido.')
