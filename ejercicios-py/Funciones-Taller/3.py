'''Ejercicio 1: Elabore un algoritmo que permita ingresar un número entero (1 a
10), y muestre su equivalente en romano.'''
def entero_a_romano (numero):
 romanos = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X'}
 if numero in romanos:
    return romanos[numero]
 else:
    return "Número fuera de rango"
numero_entero = int (input ("Ingrese un número entero del 1 al 10: "))
print ("El equivalente en romano es:", entero_a_romano (numero_entero))