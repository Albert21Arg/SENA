empleados = {}
def agregar_empleados():    
   cedula = int(input('Ingresar documento: '))

   if cedula in empleados:
       print('Ya existe.')
   else:
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        departamento = input('Departamento: ')
        salario = int(input('Salario: '))
        empleados[cedula]={
           'nombre':nombre,
           'apellido':apellido,
           'departamento':departamento,
           'salario':salario
       }
        

def ver_empleados():
    if empleados:
        for cedula, valor in empleados.items():
            print("\n"'-Cedula:',cedula, '-Nombre:', valor['nombre'], '-Apellido:', valor['apellido'],
                  '-Departamento:', valor['departamento'], '-Salario: $',valor['salario'])
            
def actualizar_empleados():
    cedula = int(input('Documento a actualizar: '))
    if cedula in empleados:
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        departamento = input('Departamento: ')
        salario = int(input('Salario: '))
        
        if nombre:
            empleados[cedula]['nombre'] = nombre
            
        if apellido:
            empleados[cedula]['apellido'] = apellido

        if departamento:
            departamento = (departamento)
            empleados[cedula]['departamento'] = departamento

        if salario:
            empleados[cedula]['salario'] = salario
            
        print(empleados)
    else:
        print("\n El empleado no existe")
        
def eliminar_empleados():
    cedula = int('digitar documento de empleado a eliminar: ')
    if cedula in empleados:
        del empleados[cedula]
    else:
        print('Empleado no Existe.')
            
if __name__ == '__main__':
    x = True
    while x == True:
        print(' 1: agregar \n 2: ver \n 3: actualizar \n 4: eliminar \n 5: salir')
        opc = int(input('selecione una opcion: '))
         
        if opc == 1:
           agregar_empleados()
        elif opc == 2:
            ver_empleados()
        elif opc == 3:
            actualizar_empleados() 
        elif opc == 4:
            eliminar_empleados()
        elif opc == 5:
            x = False
        else:
            print('No es una opcion valida.')     