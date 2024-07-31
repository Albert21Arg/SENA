i = 1
while i <= 10:
    numero = int(input('Ingresar Numero de 1 a 10: '))
    
    romanos = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X"
    }
    if numero in romanos:
        romano = romanos[numero]
        print(f'{i} El número {numero} en romano es {romano}')
    else:
        print("Número fuera de rango.")
    i=i+1
    