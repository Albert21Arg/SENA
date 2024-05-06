1
'''Elabore un algoritmo que permita 
ingresar un número entero (1 a 10), y muestre su equivalente en romano'''
try:
    numero = int(input('Digitar numero'))
    if numero == 1 :
        print(f'el numero {numero} = I')
    elif numero == 2 :
        print(f'el numero {numero} = II')
    elif numero == 3 :
        print(f'el numero {numero} = III')
    elif numero == 4 :
        print(f'el numero {numero} = IV')
    elif numero == 5 :
        print(f'el numero {numero} = V')
    elif numero == 6 :
        print(f'el numero {numero} = VI')  
    elif numero == 7 :
        print(f'el numero {numero} = VII')
    elif numero == 8 :
        print(f'el numero {numero} = VIII')
    elif numero == 9 :
        print(f'el numero {numero} = IX')
    elif numero == 10 :
        print(f'el numero {numero} = X')
    else:
        print('Numero fuera de rango')
except:
    print('Debes ingresar un numero')
