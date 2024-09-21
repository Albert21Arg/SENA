#17
numero = int(input('Ingresar numero entero de dos cifras: '))
if 10 <= numero <=99:
    unidad = numero % 10
    decena = numero // 10
    print("El número", numero, "está compuesto por:")
    print("Unidades:", unidad)
    print("Decenas:", decena)
else:
    print("El número ingresado no tiene dos cifras.")
    