5
'''Escribe un programa que reciba una nota (0-100) y la clasifique en:
deficiente (menos de 50), aprobado (50-64), notable (65-84), sobresaliente (85-100).'''
try:
    nota = int(input('Ingrese nota 0 - 100:'))
    if nota >=0 and nota <= 50:
        print(f' ({nota}) - deficiente')
    elif nota > 50 and nota <= 64 :
        print(f' ({nota}) - Aprobado')
    elif nota > 64 and nota <= 84 :
        print(f' ({nota}) - Notable')
    elif nota > 84 and nota < 100:
        print(f' ({nota}) - sobresaliente ')
    else:
        print('Ingrese una nota entre 0 y 100.')
except:
    print('Error: Valor ingresado no es un numero entrero.')
