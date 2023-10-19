#3) Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100:

suma_impares = 0

for num in range(1, 101, 2):
    suma_impares += num
    print(num)

print("La suma de los números impares desde 0 hasta 100 es:", suma_impares)
