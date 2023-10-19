#6) Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:
#✓ Todos los números del 0 al 10 [0, 1, 2, ..., 10]
#✓ Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
#✓ Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
#✓ Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
#✓ Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
 #Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto))

# Todos los números del 0 al 10 [0, 1, 2, ..., 10]
lista_0_al_10 = list(range(11))
print("Todos los números del 0 al 10:", lista_0_al_10)

# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
lista_menos10_al_0 = list(range(-10, 1))
print("Todos los números del -10 al 0:", lista_menos10_al_0)

# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
lista_pares_0_al_20 = list(range(0, 21, 2))
print("Todos los números pares del 0 al 20:", lista_pares_0_al_20)

# Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
lista_impares_menos20_al_0 = list(range(-19, 0, 2))
print("Todos los números impares entre -20 y 0:", lista_impares_menos20_al_0)

# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
lista_multiplos_de_5_0_al_50 = list(range(0, 51, 5))
print("Todos los números múltiples de 5 del 0 al 50:", lista_multiplos_de_5_0_al_50)
