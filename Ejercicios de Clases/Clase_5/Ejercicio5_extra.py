#5) Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla 
# tiene letras, donde es el nombre de usuario en mayúsculas y es el número de letras que tienen el nombre.
while True:
    nombre = input("Ingrese su nombre(o 'fin' para terminar): ")
    nombre_mayusculas = nombre.upper()
    cantidad_letras = len(nombre)
    if nombre.lower() == "fin":
        break
    if nombre.isnumeric():
        print("Porfavor ingrese su nombre, no numeros")
        continue
    print(f"{nombre_mayusculas} tiene {cantidad_letras} letras.")
