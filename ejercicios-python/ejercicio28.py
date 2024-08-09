vocales = 0
consonante = 0
i = 1 
while i < 11:
    letra = str(input(f'Digitar letra: #{i}'))
    
    if letra in ('a,e,i,o,u,A,E,I,O,U'):
        vocales = vocales + 1
        i = i + 1
    else:
        consonante = consonante + 1
        i = i + 1
print(f'total de vocales: {vocales}')
print(f'total de consonantes: {consonante}')
