n1 = int(input('Digitar numero:'))
print(f'los divisores de {n1} Son:')
for i in range(1, n1 + 1):
    if n1 % i == 0:
        print(i)
