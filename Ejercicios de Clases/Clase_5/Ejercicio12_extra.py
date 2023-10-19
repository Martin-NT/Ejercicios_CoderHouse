#12) Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.
print("División de Números")
while True:
    dividendo = input("Ingrese el dividendo (o 'fin' para terminar): ")
    if dividendo.lower() == "fin":
        break
    divisor = input("Ingrese el divisor (o 'fin' para terminar): ")
    if divisor.lower() == "fin":
        break
    
    dividendo = float(dividendo)
    divisor = float(divisor)
    
    if divisor == 0:
        print("El divisor no puede ser cero, vuelva a intentarlo")
    else:
        cociente = dividendo // divisor
        resto = dividendo % divisor
        print(f"El cociente de la division entre {dividendo} y {divisor} es de {cociente} y su resto es de {resto}" )