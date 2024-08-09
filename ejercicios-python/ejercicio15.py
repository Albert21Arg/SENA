#15
i = 1
b1 = 0.0
b2 = 3
b3 = 5
b4 = 8
#while i <= 10:
valor_venta = int(input('Ingresar el total de venta realiazado por el usuario:'))

if valor_venta < 1000:
    print(f'No obtiene bonificacion {b1}%')
else:
    if valor_venta >= 1000 and valor_venta < 5000:
        print(f'Se debe realizar una bonificacion del {b2}%')
    else:
        if valor_venta >= 5000 and valor_venta < 20000:
            print(f'Se debe realizar una bonificacion del {b3}%')
        else:
            print(f'Se debe realizar una bonificacion del {b4}%')