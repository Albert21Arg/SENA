#21
total_mayor = 0
total_menor = 0
total_edad = 0
for i in range(1,201):
    edad = int(input('Digitar edad:'))
    if edad > 17 :
        mayor = 1
        total_mayor = total_mayor+mayor
    else:
        menor = 1
        total_menor = total_menor+menor
print(f'El total de personas mayores de edad son: {total_mayor}')
print(f'El total de personas menores de edad son: {total_menor}')
print(f'El total de personas es: {i}')