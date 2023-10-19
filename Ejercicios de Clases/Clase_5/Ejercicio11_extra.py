#11)Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e 
# imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas 
# y minúsculas.

password = "Martin Navarro"
contra = input("Ingrese su contraseña: ")

if contra.lower() == password.lower():
    print("La contraseña ingresada coincide con la guardada")
else:
    print("La contraseña ingresada no coincide con la guardada")
    while True: 
        contra = input("Ingrese su contraseña nuevamente: ")
        if contra.lower() == password.lower():
            print("La contraseña ingresada coincide con la guardada")
            break 
        else:
            print("La contraseña ingresada no coincide con la guardada")
            continue
