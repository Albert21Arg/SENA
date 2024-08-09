#7
import math
print('Digite la cantidad de Gigabyte que va a copiar')
gb = int(input())
mg = gb * 1024
cd = math.trunc((mg/700)+1)
print(f'la cantidad de CDs necesaria es de: {cd} ')