#Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”.
#Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se puede procesar el dato.
letra  = str(input("Ingrese una letra: "))
vocal = ["a", "e", "i", "o", "u"]
if len(letra) == 1:
    if letra.lower() in vocal:
        print(f"La letra {letra} es una vocal")
    else:
        print(f"La letra {letra} no es una vocal")
else:
    print("No se puede procesar el dato. Ingrese solo una letra.")