#27
n1 = int(input('Digitar numero #1:'))
n2 = int(input('Digitar numero #2:'))
operador = str(input('DIgitar operador (+ , - , * , / , ^:)'))
operadores = {
    '+': n1+n2,
    '-': n1-n2,
    '*': n1*n2,
    '/': n1/n2,
    '^': n1^n2
}
if operador in operadores:
    total = operadores[operador]
    print(f'Total de operacion es: {total}')
else:
    print('Operecion fuera de rango.')
