def fun_vocales(vocales, numero):
    # Convertir la entrada de número a entero
    numero = int(numero)
    # Filtrar las vocales cuyo índice es mayor que el número ingresado
    return [vocal for indice, vocal in vocales.items() if indice == numero]

if __name__ == '__main__':
    # Diccionario de vocales con sus índices
    vocales = {1: "A", 2: "E", 3: "I", 4: "O", 5: "U"}
    
    # Pedir al usuario que ingrese un número
    indice = input('Ingresar un número: ')
    
    # Obtener la vocal correspondiente al número ingresado
    valor = fun_vocales(vocales, indice)
    
    # Mostrar el resultado
    print(f'El valor ingresado {indice} equivale a la vocal {vocales[int(indice)]}')
    print(f'Las vocales con índice mayor a {indice} son: {valor}')
