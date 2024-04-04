#6
import math
print('Digitar longitud lado A')
lado_a = float(input())
print('Digitar longitud lado B')
lado_b = float(input())
print('Digitar longitud lado C')
lado_c = float(input())
perimetro = float((lado_a + lado_b + lado_c)/2)
#area = sqrt(perimetro * (perimetro - lado_a) * (perimetro - lado_b) * (perimetro - lado_c))
area = math.sqrt(perimetro * (perimetro - lado_a) * (perimetro - lado_b) * (perimetro - lado_c))
print(f'El Area del triangulo es : {area}')