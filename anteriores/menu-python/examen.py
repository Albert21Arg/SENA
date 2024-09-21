'''# Crear en el diccionario empleado los siguientes registros Cedula, Nombres,
Apellidos, Departamento y Salario, debes hacer un crud, que te permita
crearEmpleado, LeerEmpleado (cedula), ActualizarEmpleado (cedula) y
EliminarEmpleado (cedula).
# Guiate del siguiente codigo y hazlo similar.
#productos[nombre] = {'precio': precio, 'cantidad': cantidad'''
Empleado = {}
def agregar_empleado(Empleado):
    empleadoCedula = int(input('ingresar Cedula Empleado: '))
    if empleadoCedula in Empleado :
        print(f'La cedula {empleadoCedula} ya esta registrada')
    else:
        empleadoNombre = input('ingresar Nombre: ')
        empleadoApellidos = input('ingresar Apellidos: ')
        Departamento = input('ingresar Departamento: ')
        Salario = input('ingresar Salario: ')
        Empleado = {"Cedula":empleadoCedula,"Nombre":empleadoNombre, "Apellido":empleadoApellidos, "Departamento":Departamento, "Salario":Salario}
        #print(Empleado)

def leer_empleado():
    if Empleado:
        for empleadoCedula,detalles in Empleado.items():
            print("Cedula:", empleadoCedula, "Nombre:", detalles['empleadoNombre'], ", Apellido: ", detalles['empleadoApellidos'], ", Departamento: ", detalles['Departamento'],
                  ", Salario: ", detalles['Salario'])
        else:
            print('documento no encontrado.')

x = True
if __name__ == '__main__':
    while x == True:

        opc = input('INGRESE UNA DE LAS OPCIONES: ')
        if opc == "1":
            print(agregar_empleado(Empleado))
        elif opc == "2":
            print(leer_empleado())
            
        else:
            print('Error: opcion fuera de rango.')
        