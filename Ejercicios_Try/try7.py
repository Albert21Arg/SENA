7
'''Escribe un programa que reciba el Índice de Masa Corporal (IMC) de una persona y lo clasifique en:
bajo peso (menos de 18.5), normal (18.5-24.9), sobrepeso (25-29.9) u obeso (30 o más).'''
try:
    peso = float(input('Ingrese peso Kilos '))
    estatura = float(input('Ingrese estatura en Metros '))
    imc = peso //(estatura * 2)
    print(imc)
    if imc < 18.5 :
        print(f'bajo peso ({imc})')
    elif imc >= 18.5 and imc < 24.9:
        print(f'normal ({imc})')
    elif imc >= 25 and imc < 29.9:
        print(f'sobrepeso ({imc})')
    else:
        print(f'Obeso ({imc})')
except:
    print('Error: ingreso un dato erroneo en uno de los campos.')
