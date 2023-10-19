#1) Escribe un programa que lea dos números por teclado y permita elegir entre û opciones en un menú:
# ✓ Mostrar una suma de los dos números
# ✓ Mostrar una resta de los dos números (el primero menos el segundo)
# ✓ Mostrar una multiplicación de los dos números
# ✓ Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
# ✓ En caso de no introducir una opción válida, el programa informará de que no es correcta.

while True:
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))

    print("MENU DE OPCIONES")
    opcion1 = print("1. Mostrar una suma de los dos números ")
    opcion2 = print("2. Mostrar una resta de los dos números ")
    opcion3 = print("3. Mostrar una multiplicación de los dos números")
    opcion4 = print("4. Salir")
    respuesta = input("Qué opción del Menú elige?: ")

    if respuesta == "1":
        suma = num1 + num2
        print(f"La Suma del número {num1} y el número {num2} es: {suma} ")
    elif respuesta == "2":
        resta1 = num1 - num2
        resta2 = num2 - num1
        print(f"La Resta del número {num1} y el número {num2} es: {resta1} ")
        print(f"La Resta del número {num2} y el número {num1} es: {resta2} ")
    elif respuesta == "3":
        multi = num1 * num2 
        print(f"La Multiplicación del número {num1} y el número {num2} es: {multi} ")
    elif respuesta.lower() == "4" or respuesta.lower() == "salir":
        print("Usted ha salido del Programa")
        break
    else:
        print("Introduzca una opción válida ")
