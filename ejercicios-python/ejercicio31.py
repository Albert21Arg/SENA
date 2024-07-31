try:
    numero_inicial = input('Digitar Numero 1 - 12:')
    numero = int(numero_inicial)
    meses = {
       1: 'Enero',
       2: 'Febrero',
       3: 'Marzo',
       4: 'Abril',
       5: 'Mayo',
       6: 'Junio',
       7: 'Julio',
       8: 'Agosto',
       9: 'Septiembre',
       10: 'Octubre',
       11: 'Noviembre',
       12: 'Diciembre'
    }
    if numero in meses:
        mes = meses[numero]
        print(f'El numero digitado corresponde al mes de - {mes} -')
    elif numero not in range(1, 13):
        print('Numero Fuera de rango')
except ValueError:
    print('Error: El dato ingresado no es un numero')