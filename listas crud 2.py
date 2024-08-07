print("Bienvenido al Sistema de Inventario")

idProducto = []
producto = []
cantidad = []
precio = []

i = True

while i:
    print("\nMenú de Opciones:")
    x = int(input("1--Crear Producto\n2--Buscar Producto\n3--Actualizar Producto\n4--Eliminar Producto\n5--Listar Productos\n6--Ordenar Productos por Nombre\n7--Invertir Orden de Productos\n8--Eliminar Todos los Productos\n9--Salir\nSelecciona una opción: "))

    if x == 1:
        aId = input("Ingresa el id del producto: ")
        aPro = input("Ingresa nombre producto: ").capitalize()
        aCan = int(input("Ingresa cantidad del producto: "))
        aPre = float(input("Ingresa precio del producto: "))
        idProducto.append(aId)
        producto.append(aPro)
        cantidad.append(aCan)
        precio.append(aPre)
        print("------ Producto almacenado correctamente :)---------")

    elif x == 2:
        busPro = input("Ingresa producto a buscar: ").capitalize()
        if busPro in producto:
            print("---- Producto Encontrado :)--------")
            elemento = producto.index(busPro)
            print("Nombre Producto: ", producto[elemento])
            print("Cantidad del Producto: ", cantidad[elemento])
            print("Precio del Producto: ", precio[elemento])
        else:
            print("Producto no encontrado.")

    elif x == 3:
        busPro = input("Ingresa producto a Actualizar: ").capitalize()
        if busPro in producto:
            elemento = producto.index(busPro)
            print("----Producto encontrado----")
            npro = input("Ingresa nombre nuevo producto: ").capitalize()
            ncan = int(input("Ingresa nueva cantidad del Producto: "))
            npre = float(input("Ingresa nuevo precio producto: "))
            producto[elemento] = npro
            cantidad[elemento] = ncan
            precio[elemento] = npre
            print("----Producto Actualizado Correctamente------")
        else:
            print("Producto no encontrado.")

    elif x == 4:
        busPro = input("Ingresa producto a Eliminar: ").capitalize()
        if busPro in producto:
            print("----Producto encontrado y se procede a eliminar----")
            elemento = producto.index(busPro)
            idProducto.pop(elemento)
            producto.pop(elemento)
            cantidad.pop(elemento)
            precio.pop(elemento)
            print("Producto eliminado Correctamente")
        else:
            print("Producto no encontrado.")

    elif x == 5:
        if producto:
            for ip, p, c, pr in zip(idProducto, producto, cantidad, precio):
                print(f"id: {ip}, Producto: {p}, Cantidad: {c}, Precio: {pr}")
        else:
            print("No hay productos en el inventario.")

    elif x == 6:
        # Ordena los productos alfabéticamente y mantiene la relación entre los productos, sus cantidades y precios.
        idProducto, producto, cantidad, precio = zip(*sorted(zip(idProducto, producto, cantidad, precio), key=lambda x: x[1]))
        # Convierte de nuevo las tuplas en listas
        idProducto, producto, cantidad, precio = list(idProducto), list(producto), list(cantidad), list(precio)
        print("Productos ordenados alfabéticamente.")

    elif x == 7:
        idProducto.reverse()
        producto.reverse()
        cantidad.reverse()
        precio.reverse()
        print("Orden de productos invertido.")

    elif x == 8:
        idProducto.clear()
        producto.clear()
        cantidad.clear()
        precio.clear()
        print("Todos los productos han sido eliminados.")

    elif x == 9:
        print("Hasta Pronto")
        i = False
