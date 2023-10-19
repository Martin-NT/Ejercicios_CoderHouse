#14) Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta 
# ese número separados por comas.
numero = int(input("Ingrese un número entero positivo: "))

if numero > 0:
    impares = []
    for i in range(1, numero):
        if i % 2 != 0:
            impares.append(str(i))
    resultado = ", ".join(impares)
    print("Números impares:", resultado)
else:
    print("El número ingresado no es válido.")
