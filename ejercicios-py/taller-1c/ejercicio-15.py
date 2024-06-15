def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primos = [num for num in range(2, 20) if es_primo(num)]
print("Lista de números primos menores a 20:", primos)