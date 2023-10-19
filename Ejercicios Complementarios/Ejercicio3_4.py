#4) Escribe un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.

cantidad = int(input("Ingrese cuántos números desea introducir: "))

numeros = []
for num in range(cantidad):
    numero = float(input("Ingrese un número: "))
    numeros.append(numero)

media = sum(numeros) / cantidad
print("La media aritmética de los números ingresados es:", media)
