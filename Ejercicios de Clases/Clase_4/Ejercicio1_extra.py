#Escribir un programa que almacene la cadena de caracteres "coderpython" en una variable, pregunte al usuario por la contraseña 
# e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable

password_correcta = "coderpython"
password = input("Ingrese la contraseña: ")

if password == password_correcta:
    print("La contraseña es correcta")
else:
    print("La contraseña no es correcta, intente nuevamente.")