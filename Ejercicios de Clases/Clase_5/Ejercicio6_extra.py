#6) Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +54, y 
# la extensión tiene dos dígitos (por ejemplo +54-2804-56). Escribir un programa que pregunte por un número de teléfono con este formato y 
# muestre por pantalla el número de teléfono sin el prefijo y la extensión.
while True:
    telefono = input("Ingrese un número de teléfono con el formato +54-xxxx-xx (o 'fin' para terminar): ")
    if telefono.lower() == "fin":
        break 
    prefijo = telefono[0:3]
    numero = telefono[4:8]
    extension = telefono[9:]
    print(f"Su numero de numero de telefono es: {telefono}")
    print(f"El prefijo de su numero de telefono es: {prefijo}")
    print(f"El numero de su numero de telefono es: {numero}")
    print(f"La extension de su telefono es: {extension}")