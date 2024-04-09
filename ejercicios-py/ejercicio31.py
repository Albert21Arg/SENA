#31
numero = int(input('Digitar Numero:'))
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
