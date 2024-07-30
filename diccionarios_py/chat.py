"""# Crear en el diccionario empleado los siguientes registros Cedula, Nombres, Apellidos, Departamento y Salario, debes hacer un crud, que te permita crearEmpleado, LeerEmpleado (cedula), ActualizarEmpleado (cedula) y EliminarEmpleado (cedula).
# Guiate del siguiente codigo y hazlo similar.
#productos[nombre] = {'precio': precio, 'cantidad': cantidad}
#empleado[cedula] ={'nombres':nombre, ...}"""
import os as os
empleados={}
def crearEmpleado():
    nombre =input("Ingrese nombre: ")
    cedula =int(input("Ingrese cedula: "))
    apellido =input("Ingrese apellido: ")
    departamento =input("Ingrese departamento: ")
    salario =int(input("Ingrese salario: "))
 
    if nombre not in empleados:
        empleados[nombre]={
            "cedula":cedula,
            "apellido":apellido,
            "departamento":departamento,
            "salario": salario
        }
 
def leerEmpleado():
    if empleados:
        for nombre, detalles in empleados.items():
            print("\n","Nombre:", nombre, "Cedula:", detalles['cedula'], ", Apellido: ", detalles['apellido'], ", Departamento: ", detalles['departamento'],
                  ", Salario: ", detalles['salario'])
 
def actualizarEmpleado():
    nombre = input("Ingrese nombre a actualizar: ")
    if nombre in empleados:
        cedula =input("Ingrese nueva cedula o deje en blaco sino va actualizar: ")
        apellido =input("Ingrese nuevo apellido deje en blaco sino va actualizar: ")
        departamento =input("Ingrese nuevo departamento deje en blaco sino va actualizar: ")
        salario =input("Ingrese nuevo salario deje en blaco sino va actualizar: ")
 
        if cedula:
            cedula = int(cedula)
            empleados[nombre]["cedula"] = cedula
        
        if apellido:
            empleados[nombre]["apellido"] = apellido
        
        if departamento:
            empleados[nombre]["departamento"] = departamento
        
        if salario:
            salario = int(salario)
            empleados[nombre]["salario"] = salario
        
        print(empleados)
    else:
        print("\nEl empleado no existe")
 
def eliminarEmpleado():
    nombre = input("Ingrese nombre a eliminar: ")
    if nombre in empleados:
        del empleados[nombre]
        print("\nEmpleado eliminado exitosamente")
    else:
        print("\nEl empleado no existe")
 
def mostrarMenu():
    print("\n1. Crear empleado")
    print("\n2. Leer empleados")
    print("\n3. Actualizar empleado")
    print("\n4. Eliminar empleado")
    print("\n5. Salir\n")
 
if __name__=="__main__":
    while True:
        
        mostrarMenu()
        
        opcion=int(input("Ingrese opcion del 1 al 5: "))
 
        if opcion in range(1,6):
            os.system("clear")
            if opcion == 1:
                crearEmpleado()
            if opcion == 2:
                leerEmpleado()
            if opcion == 3:
                actualizarEmpleado()
            if opcion == 4:
                eliminarEmpleado()
            if opcion == 5:
                break
        else:
            print("Opcion no valida")