#12
print('digitar numero #1')
n1= int(input())
print('digitar numero #2')
n2= int(input())
print('digitar numero #3')
n3= int(input())

if (n1 == n2) or (n1 == n3) or (n2 == n3) :
    print('Error ingresaste numeros iguales')
else:
    if n1 > n2 and n1 > n3 :
        print(f'El numero mayor es #1 y su valor era de: {n1}')
    else:
        if n2 > n1 and n2 > n3:
            print(f'El numero mayor es #2 y su valor era de: {n2}')
        else:
            print(f'El numero mayor es #3 y su valor era de: {n3}')