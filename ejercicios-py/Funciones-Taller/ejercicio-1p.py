def crear_lista_nombres():
    return [
        "Ana", "Carlos", "María", "Luis", "Pedro", "Sofía", "Marta", "José",
        "Lucía", "Juan", "Elena", "Diego", "Laura", "Javier", "Carmen", "Alberto",
        "Isabel", "Andrés", "Victoria", "Ricardo"
    ]

def mostrar_nombres(lista):
    i = 1
    for nombre in lista :
        print(f"{i}:  {nombre}")
        i = i + 1

if __name__ == '__main__':
# Crear la lista de nombres
    nombres = crear_lista_nombres()

# Mostrar los nombres
    mostrar_nombres(nombres)