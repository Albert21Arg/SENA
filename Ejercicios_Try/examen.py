'''que solicite al usuario ingresar tres números y luego imprima el mayor de los tres, el menor de los 3, si son iguales, si al menos hay dos iguales.
Asegúrate de que tu código maneje correctamente cualquier tipo de números (positivos, negativos y decimales).
Después de completar tu algoritmo, muestra tu código al profesor para su revisión.
Una vez que tu solución haya sido revisada y aprobada, copia y pega tu código en word y conviertelo en pdf y subelo en el espacio a continuación.'''
try: 
    primerNumero = float(input('Digitar primer numero: '))
    segundoNumero = float(input('Digitar segundo numero: '))
    tercerNumero = float(input('Digitar tercer numero: '))

    if primerNumero > segundoNumero and primerNumero > tercerNumero and segundoNumero < primerNumero and tercerNumero < primerNumero:
        print(f'numero 1 {primerNumero} es mayor')         
    
    elif segundoNumero > primerNumero and segundoNumero > tercerNumero and primerNumero < segundoNumero and tercerNumero < segundoNumero:
            print(f'numero 2 {segundoNumero} es mayor')

    elif tercerNumero > primerNumero and tercerNumero > segundoNumero and segundoNumero < tercerNumero and primerNumero < tercerNumero:
         print(f'numero 3 {tercerNumero} es mayor')

    elif primerNumero == segundoNumero and primerNumero == tercerNumero and segundoNumero == primerNumero and tercerNumero == primerNumero and segundoNumero == tercerNumero  and tercerNumero == segundoNumero:
        print(f'los numeros son iguales')
    
    elif primerNumero == segundoNumero or primerNumero == tercerNumero or segundoNumero == primerNumero or tercerNumero == primerNumero or segundoNumero == tercerNumero  or tercerNumero == segundoNumero:
        print(f'hay al menos 2 numeros iguales') 
    
    
    if primerNumero < segundoNumero and primerNumero < tercerNumero or segundoNumero > primerNumero and tercerNumero > primerNumero:
              print(f'Numero menor es {primerNumero}')
    else :
        if segundoNumero < primerNumero and segundoNumero < tercerNumero or primerNumero > segundoNumero and tercerNumero > segundoNumero:
            print(f'Numero menor es {segundoNumero}')
        else:
            if tercerNumero < primerNumero and tercerNumero < segundoNumero or primerNumero > tercerNumero and segundoNumero > tercerNumero:
                print(f'Numero menor es {tercerNumero}')
            else:
                 print(f'hay numeros iguales')        
    
except:
    print(f'debe ingresar un numero')