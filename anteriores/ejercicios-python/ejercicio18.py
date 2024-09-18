#18
numero = int(input('Digitar numero entero '))
if numero > 0 :
    if (numero % 2) == 0 :
        print('El numero digitado es Par')
    else:
        print('El numero digitado es Impar')
else:
    print('El numero es 0 o no es un numero entero.')