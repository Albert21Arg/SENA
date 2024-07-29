notas=[]

for i in range (10): 

    nota = float (input (f" Nota {i+1}: ")) 

    notas.append(nota) 

 

 #Solicitar al usuario la nota a buscar en el vector 

nota_buscar = float (input ("Ingrese la nota que desea buscar: ")) 

posiciones = []  #Inicializar lista para guardar las posiciones donde se encuentra la nota 

 

for i, n in enumerate (notas):  #Buscar la nota y su posición en el vector 

    if n == nota_buscar:  #si es la nota buscada guarda su posición en posiciones. 

        posiciones.append(i+1) 

 

if posiciones:  #si existe posición mostrar la posición 

    print (f" La nota {nota_buscar} se encontró en la(s) posición(es): {posiciones}") 

else: 

    print ("La nota no se encontró en el vector.")