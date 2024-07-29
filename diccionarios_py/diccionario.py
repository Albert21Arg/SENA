import os
def fun_promedio():
    cantida_notas = int(input('Cual es la cantidad de notas? '))
    k = 0
    suma_nota = 0
    if k < cantida_notas :
        for i in range(cantida_notas):
            notas = float(input(f'VALOR NOTA {i+1}: '))
            suma_nota = suma_nota + notas
            #print(suma_nota)
            promedio = suma_nota/cantida_notas
    print (f'Promedio de notas es: {promedio}')
    
if __name__ == '__main__':
    print(fun_promedio())