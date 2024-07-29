import os
import diccionario
i = True
while i == True:
    print('Opciones \n 1: Promedio \n 2: Salir')
    res = str(input('Ingresar Una de las opciones. ').capitalize())
    #os.system("clear")
    if res == "1" or res == "Promedio".capitalize():
        print(diccionario.fun_promedio())
    elif res == "2" or res == "Salir":
        i == False
        print('Salio del programa.')
    