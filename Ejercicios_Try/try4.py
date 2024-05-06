4
'''Escribe un programa que reciba una edad como entrada y clasifique a la persona en las siguientes categorías:
niño (menos de 11 años),adolescente (12-17 años), adulto (18-64 años) o mayor (65 años o más).'''
try:
    edad = int(input('Digite la edad.'))
    if edad <= 11 :
        print(f'Pertenece a la categoría niño y tiene {edad} Años')
    elif edad > 11 and edad <= 17 :
        print(f'Pertenece a la categoría adolescente y tiene {edad} Años')
    elif edad > 18 and edad <= 64 :
        print(f'Pertenece a la categoría adulto y tiene {edad} Años')
    else:
        print(f'Pertenece a la categoría adulto mayor y tiene {edad} Años')
except:
    print('Error: debe ingresar una edad Valida')
