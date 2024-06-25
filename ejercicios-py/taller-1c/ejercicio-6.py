#Ordenar Lista de Palabras por Longitud
#Escribe un algoritmo que ordene una lista de palabras por su longitud.
palabras = ["python", "es", "un", "lenguaje", "de", "programacion"]
palabras_ordenadas = sorted(palabras, key=len)
print(f"Palabras ordenadas por longitud: {palabras_ordenadas}")