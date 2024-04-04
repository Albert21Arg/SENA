#9
print('Pertenece al sistema de pension')
pension = str(input())
print('Eres Jubilado')
jubilado = str(input())
print('Digitar Año de nacimiento')
año_nacimiento = int(input())
año_actual = 2024
edad = año_actual-año_nacimiento

if edad > 17 or jubilado == 'si' or jubilado == 'Si' or pension == 'si' or pension == 'Si':
    print('Debe sacar su CUIL')
    print(f'La edad es: {edad}')
else:
     print('No Debe sacar su CUIL')
     print(f'La edad es: {edad}')