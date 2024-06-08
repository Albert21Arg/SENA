#Producto de Elementos Impares
#Escribe un algoritmo que calcule el producto de todos los elementos impares de una lista de números enteros.
lista = [1,2,3,4,5,6]
producto_impar = 1
for num in lista:
    if num % 2 != 0:
        producto_impar *= num
print(f"El producto de los elementos impares es: {producto_impar}")