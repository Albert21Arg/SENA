# 3
res_correcta = 4
res_incorrecta = 1
print('ingresar el numero de respuestas correctas')
respuesta_c = int(input())
print('ingresar el numero de respuestas correctas')
respuesta_i = int(input())
total_res_correcta = respuesta_c *res_correcta
total_res_incorrecta = respuesta_i *res_incorrecta
print(f'puntaje por respuestas correctas: {total_res_correcta}')
print(f'puntaje por respuestas incorrectas: -{total_res_incorrecta}')
total_res = respuesta_c + respuesta_i
print(f'Total de preguntas es: {total_res} ')
total_puntos = total_res_correcta - total_res_incorrecta
print(f'puntaje total es: {total_puntos}')
