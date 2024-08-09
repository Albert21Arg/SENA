#16
i=1
while i <= 5 :
    numero = int(input('Digitar numero de 1 a 5: '))
    vocales = {
    1: "A",
    2: "E",
    3: "I",
    4: "O",
    5: "U"
    }
    if numero in vocales :
        vocal = vocales[numero]
        print(f'El numero pertenece a la vocal {vocal}')
    else:
        print("Número fuera de rango.")
        i=i+1