def primer_elemento(lista):
    if not lista:
        return 
    return lista[0]

resultado = primer_elemento([])
print("El resultado es:", resultado)

resultado = primer_elemento([1, 2, 3])
print("El primer elemento es:", resultado)