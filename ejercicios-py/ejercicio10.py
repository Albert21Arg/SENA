#10
print('Digitar Edad de Hermano #1')
edad_1 = int(input())
print('Digitar Edad de Hermano #2')
edad_2 = int(input())

if edad_1 > edad_2:
    diferencia = edad_1 - edad_2
    print(f'El Hermano mayor es #1 con {edad_1} Años la diferencia es de {diferencia} Años con el segundo')
else:
    diferencia = edad_2 - edad_1
    print(f'El Hermano mayor es #2 con {edad_2} Años la diferencia es de {diferencia} Años con el primero')