#Ejercicio 3
#Escribir un algoritmo que pregunte al usuario por el número de horas trabajadas y el valor de la hora.
#Después debe mostrar por pantalla el pago que le corresponde.

horas_trabajadas = float(input("Ingrese el numero de horas trabajadas: "))
valor_hora = float(input("Ingrese el valor de la hora: "))

pago = horas_trabajadas * valor_hora

print("El pago correspondiente es de: $" , pago)