#5
print('digitar numero de planilla')
planilla = int(input())
print('digitar nombre empleado:')
nombre_emp = input()
print('digitar horas laboradas a la semana:')
horas_laboradas = int(input())
print('valor pagado por hora:')
valor_hora = int(input())
total_pagar = (horas_laboradas*5)*valor_hora
print(planilla)
print(nombre_emp)
print(f'El Total a pagar al mes es : {total_pagar}')