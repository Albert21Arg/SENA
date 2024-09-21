# Inicializar el diccionario de productos
productos = {}

def crear_producto():
    id_producto = input("Ingrese el ID del producto: ")
    if id_producto in productos:
        print(f"El producto con ID {id_producto} ya existe.")
    else:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        productos[id_producto] = {'id': id_producto, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        print(f"Producto {nombre} creado exitosamente con ID {id_producto}.")

def leer_productos():
    if productos:
        for id_producto, detalles in productos.items():
            print(f"ID: {id_producto}, Producto: {detalles['nombre']}, Precio: {detalles['precio']}, Cantidad: {detalles['cantidad']}")
    else:
        print("No hay productos en el inventario.")

def leer_productos_por_id():
    id_producto = input("Ingrese el ID del producto a buscar: ")
    if id_producto in productos:
        detalles = productos[id_producto]
        print(f"ID: {id_producto}, Producto: {detalles['nombre']}, Precio: {detalles['precio']}, Cantidad: {detalles['cantidad']}")
    else:
        print(f"No se encontró ningún producto con ID {id_producto}.")

def actualizar_producto():
    id_producto = input("Ingrese el ID del producto a actualizar: ")
    if id_producto in productos:
        nombre = input("Ingrese el nuevo nombre del producto (dejar en blanco para no cambiar): ")
        precio = input("Ingrese el nuevo precio del producto (dejar en blanco para no cambiar): ")
        cantidad = input("Ingrese la nueva cantidad del producto (dejar en blanco para no cambiar): ")
        if nombre:
            productos[id_producto]['nombre'] = nombre
        if precio:
            productos[id_producto]['precio'] = float(precio)
        if cantidad:
            productos[id_producto]['cantidad'] = int(cantidad)
        print(f"Producto con ID {id_producto} actualizado exitosamente.")
    else:
        print(f"El producto con ID {id_producto} no existe.")

def eliminar_producto_por_id():
    id_producto = input("Ingrese el ID del producto a eliminar: ")
    if id_producto in productos:
        del productos[id_producto]
        print(f"Producto con ID {id_producto} eliminado exitosamente.")
    else:
        print(f"El producto con ID {id_producto} no existe.")

def eliminar_producto_por_nombre():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    id_producto_a_eliminar = None
    for id_producto, detalles in productos.items():
        if detalles['nombre'] == nombre:
            id_producto_a_eliminar = id_producto
            break
    if id_producto_a_eliminar:
        del productos[id_producto_a_eliminar]
        print(f"Producto {nombre} eliminado exitosamente.")
    else:
        print(f"El producto con nombre {nombre} no existe.")

def eliminar_todos_los_productos():
    productos.clear()
    print("Todos los productos han sido eliminados del inventario.")

def ordenar_por_nombre():
    productos_ordenados = sorted(productos.items(), key=lambda x: x[1]['nombre'])
    for id_producto, detalles in productos_ordenados:
        print(f"ID: {id_producto}, Producto: {detalles['nombre']}, Precio: {detalles['precio']}, Cantidad: {detalles['cantidad']}")

def ordenar_por_id_desc():
    productos_ordenados = sorted(productos.items(), key=lambda x: x[0], reverse=True)
    for id_producto, detalles in productos_ordenados:
        print(f"ID: {id_producto}, Producto: {detalles['nombre']}, Precio: {detalles['precio']}, Cantidad: {detalles['cantidad']}")

def mostrar_menu():
    print("\n--- Menú CRUD ---")
    print("1. Crear producto")
    print("2. Leer productos")
    print("3. Leer producto por ID")
    print("4. Actualizar producto")
    print("5. Eliminar producto por ID")
    print("6. Eliminar producto por nombre")
    print("7. Eliminar todos los productos")
    print("8. Ordenar productos por nombre")
    print("9. Ordenar productos por ID (descendente)")
    print("10. Salir")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            crear_producto()
        elif opcion == '2':
            leer_productos()
        elif opcion == '3':
            leer_productos_por_id()
        elif opcion == '4':
            actualizar_producto()
        elif opcion == '5':
            eliminar_producto_por_id()
        elif opcion == '6':
            eliminar_producto_por_nombre()
        elif opcion == '7':
            eliminar_todos_los_productos()
        elif opcion == '8':
            ordenar_por_nombre()
        elif opcion == '9':
            ordenar_por_id_desc()
        elif opcion == '10':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
