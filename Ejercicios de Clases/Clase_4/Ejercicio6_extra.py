#Escribir un programa que pida al usuario dos números y devuelva su división. Si el usuario introduce el divisor cero debera 
# imprimir un mensaje de error.
#Nota: Este es un poquito mas complicado, pero con lo que vimos hasta la fecha, lo pueden resolver.
print("División de Números")
dividendo = float(input("Ingrese el dividendo: "))
divisor = float(input("Ingrese el divisor: "))

if divisor == 0:
    print("El divisor no puede ser cero, vuelva a intentarlo")
else:
    cociente = dividendo / divisor
    resto = dividendo % divisor
    print(f"El cociente de la division entre {dividendo} y {divisor} es de {cociente} y su resto es de {resto}" )