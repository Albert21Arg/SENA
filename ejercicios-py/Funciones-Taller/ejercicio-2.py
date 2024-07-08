def filtrar_palabras_subcadena():
    return [palabra for palabra in palabras if subcadena in palabra]

def crear_lista_nombres():
    return [
        "Ana", "Carlos", "María", "Luis", "Pedro", "Sofía", "Marta", "José",
        "Lucía", "Juan", "Elena", "Diego", "Laura", "Javier", "Carmen", "Alberto",
        "Isabel", "Andrés", "Victoria", "Ricardo"
    ]

if __name__ == '__main__':
    palabras = crear_lista_nombres()
    subcadena = input("Digitar Palabra: ")
    palabras_filtradas = filtrar_palabras_subcadena ()
    print (f"Palabras que contienen '{subcadena}': {palabras_filtradas}")