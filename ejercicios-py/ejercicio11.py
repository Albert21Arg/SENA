#11.	Se tiene registrado la producción (unidades) logradas por un operario a lo largo
#de la semana (lunes a sábado). Elabore un algoritmo
#que nos muestre o nos diga si el operario recibirá incentivos sabiendo que el promedio de producción mínima es de 100 unidades.

minimo_unidades = 100
print('Digitar cantidad unidades dia')
print('Lunes')
l= int(input())
print('Martes')
m= int(input())
print('Miercoles')
mr= int(input())
print('Jueves')
j= int(input())
print('Viernes')
v= int(input())
print('Sabado')
s= int(input())
producion = l+m+mr+j+v+s

if producion > minimo_unidades :
    print('El Operario merece incentivos')
    print(f'la producion del usuario es de {producion} Unidades')
else:
    print('El Operario no merece incentivos')
    print(f'la producion del usuario es de {producion} Unidades')