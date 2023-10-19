#Escribí un programa que solicite al usuario el ingreso de dos números diferentes y muestre en pantalla al mayor de los dos.
num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))
if num1 > num2:
    print(f"El número {num1} es mayor al número {num2}")
elif num2 > num1:
    print(f"El número {num2} es mayor al número {num1}")
else: 
    print(f"Los numeros ingresados {num1} y {num2} son iguales")