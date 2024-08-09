cantidad_votantes = int(input('Digitar cantidad de votantes:'))
i = 0 
c1 = 0
c2 = 0
c3 = 0
blanco = 0
nuv = 0
while i < cantidad_votantes:
    voto = str(input('Digitar numero de candidato por el que va a votar:'))
    if voto == '1' :
        c1 += 1
    else:
        if voto == '2':
            c2 += 1
        else:
            if voto == '3':
                c3 += 1
            else:
                if voto in ('b','B','Blanco','blanco'):
                    blanco += 1
                else:
                    nuv += 1
    i = i + 1 
if c1 > c2 and c1 > c3:
    ganador = 'candidato #1'
    print(f'votos candidato ganador {c1}')
else:
    if c2 > c1 and c2 > c3:
        ganador = 'candidato #2'
        print(f'votos candidato ganador {c2}')
    else:
        if c3 > c1 and c3 > c2 :
            ganador = 'candidato #3'
            print(f'votos candidato ganador {c3}')
        else:
            ganador = 'voto en blanco'
            print(f'votos candidato ganador {blanco}')
total_votos = c1 + c2 + c3 + blanco + nuv
print(f'ganador es :{ganador}')
print(f'votos blanco :{blanco}') 
print(f'votos nulos :{nuv}')
print(f'total de votos es: {total_votos}')
