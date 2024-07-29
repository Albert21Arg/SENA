def crear_lista_nombres():
    # Crea una lista unidimensional con nombres de personas
    return [
        "Ana", "Carlos", "María", "Luis", "Pedro", "Sofía", "Marta", "José",
        "Lucía", "Juan", "Elena", "Diego", "Laura", "Javier", "Carmen", "Alberto",
        "Isabel", "Andrés", "Victoria", "Ricardo"
    ]

def mostrar_nombres(lista):
    # Muestra cada nombre de la lista en una línea distinta
    for nombre in lista:
        print(nombre)

if __name__ == '__main__':
    # Crear la lista de nombres
    nombres = crear_lista_nombres()
    # Mostrar los nombres en una línea distinta cada uno
    mostrar_nombres(nombres)
