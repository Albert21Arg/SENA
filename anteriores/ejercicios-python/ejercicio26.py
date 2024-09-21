#26
n1 = int(input('Digitar numero #1'))
n2 = int(input('Digitar numero #2'))
n3 = n1 + n2 
while n3 <= 1000:
    print(n3)
    n1 = n2
    n2 = n3
    n3 = n1 + n2
