#20
total_salario = 0
for i in range(1, 4):
    id_empleado = int(input('digitar numero empleado'))
    salario = int(input('digitar salario empleado:'))
    total_salario = total_salario + salario
    promedio = total_salario / i
print(f'el salario promedio de los {i} empleados es: {promedio}')
