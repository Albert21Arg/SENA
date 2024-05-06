6
'''Escribe un programa que reciba una temperatura (en grados Celsius) y la clasifique en: 
frío (menos de 10°C), templado (10-20°C), cálido (21-30°C) o caluroso (más de 30°C).'''
try:
    temperatura = int(input('Ingresar la temperatura grados Celsius'))
    if temperatura < 10:
        print(f'{temperatura}° -Frio')
    elif temperatura >= 10 and temperatura <= 20:
        print(f'{temperatura}° -Templado')
    elif temperatura > 20 and temperatura <= 30:
        print(f'{temperatura}° -Calido')
    else:
        print(f'{temperatura}° -Caluroso')
except:
    print('Error: ingrese una temperatura correcta.')
