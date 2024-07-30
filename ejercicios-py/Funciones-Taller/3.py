"""# Crear en el diccionario empleado los siguientes registros Cedula, Nombres, Apellidos, Departamento y Salario, debes hacer un crud, que te permita crearEmpleado, LeerEmpleado (cedula), ActualizarEmpleado (cedula) y EliminarEmpleado (cedula).
# Guiate del siguiente codigo y hazlo similar.
#productos[nombre] = {'precio': precio, 'cantidad': cantidad}
#empleado[cedula] ={'nombres':nombre, ...}"""
import os as os
empleados={}
def crearEmpleado():
    cedula =int(input("Ingrese cedula: "))
    nombre =input("Ingrese nombre: ")    
    apellido =input("Ingrese apellido: ")
    departamento =input("Ingrese departamento: ")
    salario =int(input("Ingrese salario: "))
 
    if cedula not in empleados:
        empleados[cedula]={
            "nombre":nombre,
            "apellido":apellido,
            "departamento":departamento,
            "salario": salario
        }
 
def leerEmpleado():
    if empleados:
        for cedula, detalles in empleados.items():
            print("\n","Cedula:", cedula, "Nombre:", detalles['nombre'], ", Apellido: ", detalles['apellido'], ", Departamento: ", detalles['departamento'],
                  ", Salario: ", detalles['salario'])
 
def actualizarEmpleado():
    cedula = input("Ingrese cedula a actualizar: ")
    if cedula in empleados:
        nombre =input("Ingrese nueva nombre o deje en blaco sino va actualizar: ")
        apellido =input("Ingrese nuevo apellido deje en blaco sino va actualizar: ")
        departamento =input("Ingrese nuevo departamento deje en blaco sino va actualizar: ")
        salario =input("Ingrese nuevo salario deje en blaco sino va actualizar: ")
 
        if nombre:
            nombre = int(nombre)
            empleados[cedula]["nombre"] = nombre
        
        if apellido:
            empleados[cedula]["apellido"] = apellido
        
        if departamento:
            empleados[cedula]["departamento"] = departamento
        
        if salario:
            salario = int(salario)
            empleados[cedula]["salario"] = salario
        
        print(empleados)
    else:
        print("\nEl empleado no existe")
 
def eliminarEmpleado():
    cedula = input("Ingrese nombre a eliminar: ")
    if cedula in empleados:
        del empleados[cedula]
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