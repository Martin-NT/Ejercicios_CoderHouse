#EJERCICIO 1:
#Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):
# -Si los dos números son iguales
# -Si los dos números son diferentes
# -Si el primero es mayor que el segundo
# -Si el segundo es mayor o igual que el primero

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

iguales = num1 == num2
diferentes = num1 != num2 
primero_mayor_segundo = num1 > num2 
segundo_mayor_igual_primero = num2 >= num1

print("Los numeros son: " , num1, num2)
print("Son iguales: " , iguales)
print("Son diferentes: " , diferentes)
print("El primero es mayor que el segundo: " , primero_mayor_segundo)
print("El segundo es mayor o igual que el primero: " , segundo_mayor_igual_primero)