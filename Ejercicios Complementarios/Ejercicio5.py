#Colecciones práctica extra
#Consigna
#A partir de una lista realizar las siguientes tareas sin modificar la lista original:
#1. Borrar los elementos duplicados
#2. Ordenar la lista de mayor a menor
#3. Eliminar todos los números impares ( for ---- if (%2==1) ---- pop, remove )
#4. Realizar una suma de todos los números que quedan (sum(lista))
#5. Añadir como primer elemento de la lista la suma realizada insert(0, suma)
#6. Devolver la lista modificada
#7. Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, 
# concuerda con el primer número de la lista
#lista = [29,-5,-12,17,5,24,5,12,23,16,12,5,-12,17]
#Nota: Recuerda que para sumar todos los números de una lista puedes usar sum

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

print("1. Borrar los elementos duplicados")
lista = list(set(lista))
print(lista)

print("2. Ordenar la lista de mayor a menor")
lista.sort(reverse=True)
print(lista)

print("3. Eliminar todos los números impares")
lista = [num for num in lista if num % 2 == 0]
print(lista)

print("4. Realizar una suma de todos los números que quedan")
suma = sum(lista)
print(suma)

print("5. Añadir como primer elemento de la lista la suma realizada")
lista.insert(0, suma) #lista.insert(posición, ítem)
print(lista)

print("6. Devolver la lista modificada")
print(lista)

print("7. Comprobar si la suma de todos los números a partir del segundo coincide con el primer número de la lista ")
if suma == sum(lista[1:]):
    print("Rta: La suma de los números a partir del segundo coincide con el primer número de la lista.")
else:
    print("Rta: La suma de los números a partir del segundo NO coincide con el primer número de la lista.")

