def fun_nombres(nombres):
    i = 0
    catidad_nombres = int(input("Cuantos nombres va a ingresar? "))
    nombres =  []
    for i in range(catidad_nombres):
        nombre = input(f'ingresar nombre {i + 1}: ')
        nombres.append(nombre)
    return nombres

if __name__ == '__main__':
    print(fun_nombres())