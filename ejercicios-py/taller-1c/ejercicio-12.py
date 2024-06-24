#Escribe un algoritmo que filtre una lista de palabras y devuelva 
#solo las palabras que contienen una subcadena específica.
palabras = ["hola", "mundo", "holanda" , "python" , "holistico"]

subcadena = input('Ingresar palabra:')
filtro_palabras = [palabra for palabra in palabras if subcadena in palabra]
print(f"Palabras que contienen {subcadena}: {filtro_palabras} ")