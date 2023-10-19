#3) Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la entre da un cociente y un resto donde y 
# son los números introducidos por el usuario, y y son el cociente y el resto de la división entera respectivamente.
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