import ejecicios
def mostrar_nombres(nombres):
    for nombre in nombres:
        print(nombre)
    print(nombres)


if __name__ == '__main__':
    nombres = []
    n = ejecicios.fun_nombres(nombres)
    mostrar_nombres(nombres=n)
