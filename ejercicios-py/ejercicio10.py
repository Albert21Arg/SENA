#10
print('Digitar Año de nacimiento')
año_nacimiento = int(input())
año_actual = 2024
edad = año_actual-año_nacimiento
if edad < 17 :
    print('No Debe sacar (CUIL)')
    print(f'su edad es {edad} Años')
else:
    print('pertenece al sistema integrado de jubilacion y pension?')
    sistema_integrado = str(input())
    if sistema_integrado == 'si' or sistema_integrado == 'Si':
        print('Debe sacar (CUIL)')
        print(f'su edad es {edad} Años')
    else:
        print('Realiza alguna prestacion de servicio de la seguridad social de la republica?')
        ser_social = str(input())
        if ser_social == 'si' or ser_social == 'Si':
            print('Debe sacar (CUIL)')
            print(f'su edad es {edad} Años')
        else:
            print(f'su edad es {edad} Años')
            print('No Debe sacar (CUIL)')