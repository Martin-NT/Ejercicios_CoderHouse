import math #Librerias de Python
print("----Calculadora----")

numero = 4
num_decimal = 1.4

x = math.sqrt(numero)
factorial = math.factorial(numero)
redondeo1 = math.ceil(num_decimal)
redondeo2 = math.floor(num_decimal)

print(f"La raiz cuadrada de {numero} es {x}") #La raiz cuadrada de 4 es 2.0
print(f"El factorial de {numero} es {factorial}") #El factorial de 4 es 24
print(f"Redondea para arriba {num_decimal} --> {redondeo1}") #Redondea para arriba 1.4 --> 2
print(f"Redondea para abajo {num_decimal} --> {redondeo2}") #Redondea para abajo 1.4 --> 1


