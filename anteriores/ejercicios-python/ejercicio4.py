pg = 3
pp = 0
pe = 1
print('digitar cantidad partidos ganados:')
total_pg = int(input())
print('digitar cantidad partidos empatados:')
total_pe = int(input())
print('digitar cantidad partidos perdidos:')
total_pp = int(input())
total_partidos = total_pg+total_pe+total_pp
print(f'Total de partidos es: {total_partidos} ')
print(f'total puntos por partidos ganados: {pg * total_pg} ' )
print(f'total puntos por partidos empatados: {pe * total_pe} ' )
print(f'total puntos: {pg * total_pg + pe * total_pe} ' )
