#Escribe un algoritmo que genere una lista de los primeros 10 números de Fibonacci.
fibonacci = [0,1]
for i in range(2,10):
    secuencia = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(secuencia)
    print(f"Lista de los primeros 10 numeros de Fibonacci: {fibonacci}")