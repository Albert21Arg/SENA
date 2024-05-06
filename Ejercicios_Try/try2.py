2
'''Elabore un algoritmo que permita ingresar el monto de venta alcanzado por un vendedor durante 
el mes, luego de calcular la bonificación que le corresponde sabiendo:'''
try:
    monto = int(input('Ingresar el monto venedido:'))
    if monto <= 1000 : 
        print('No obtiene bonificación')
    elif monto > 1000 and monto <=5000 :
        print(f'obtiene una bonificación del 3% = {(monto  * 3 // 100)}')
    elif monto > 5000 and monto <=20000 :
        print(f'obtiene una bonificación del 5% = {(monto  * 5 // 100)}')
    else:
        print(f'obtiene una bonificación del 8% = {(monto  * 8 // 100)}')
except:
    print('Error: el valor ingresado contiene letras.')
