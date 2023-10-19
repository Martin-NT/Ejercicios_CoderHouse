#2) Escribe un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, 
# debe repetirse el proceso hasta que lo introduzca correctamente

while True:
    impar = int(input("Ingrese un número impar: "))
    
    if impar % 2 == 0:
        print(f"El número {impar} no es impar. Intente nuevamente.")
    else:
        print("CORRECTO")
        print(f"El número {impar} es impar.")
        break
