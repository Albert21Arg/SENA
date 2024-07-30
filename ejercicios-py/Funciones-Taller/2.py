'''Ejercicio 2: Función para Filtrar Palabras que Contengan una Subcadena
Escribe una función que filtre una lista de palabras y devuelva solo las palabras que contienen
una subcadena específica.'''
def filtrar_palabras_subcadena(palabras, subcadena):
 return [palabra for palabra in palabras if subcadena in palabra]
if __name__ == '__main__':
 palabras = ["hola", "mundo", "holanda", "python", "holístico"]
 subcadena = "hol"
 palabras_filtradas = filtrar_palabras_subcadena (palabras, subcadena)
 print (f"Palabras que contienen '{subcadena}': {palabras_filtradas}")