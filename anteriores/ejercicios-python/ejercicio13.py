#13
print('Digitar longitud lado A')
a= int(input())
print('Digitar longitud lado B')
b= int(input())
print('Digitar longitud lado C')
c= int(input())

if (a == b) and (a == c) and (b == c):
    print('El triangulo es de tipo Equilátero')
else:
    if (a != b) and (a != c) and (b != c):
        print('El triangulo es de tipo Escaleno')
    else:
        print('El triangulo es de tipo Isósceles')