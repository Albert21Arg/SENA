#Escribe un algoritmo que elimine las palabras de menos de 4 caracteres de una lista de strings.
palabras = ["python", "es", "genial", "muy", "bueno"]
palabras_largas = [palabra for palabra in palabras if len(palabra) >= 4]
print("Palabras con 4 o más caracteres:", palabras_largas)