#8
import math
def calcular_distancia(x1, y1, x2, y2  ):
    delta_x = x2 - x1
    delta_y = y2 - y1
    suma_cuadrados = delta_x ** 2 + delta_y ** 2
    distancia = math.sqrt(suma_cuadrados)
    return distancia
print('Digitar coordenadas x del punto  A:')
x1 = float(input())
print('Digitar coordenadas y del punto A:')
y1 = float(input())
print('Digitar coordenadas x del punto  B:')
x2 = float(input())
print('Digitar coordenadas y del punto B:')
y2 = float(input())
distancia = calcular_distancia(x1, y1, x2, y2)
print(f'La distacia entre A y B es: {distancia}' )
