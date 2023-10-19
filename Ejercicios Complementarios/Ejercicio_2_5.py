#5) La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila el cuarto elemento siempre debe ser 
# el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?
#Ayuda: La función llamada sum(lista) devuelve una suma de todos los elementos de la lista
#Partirás de: 
#matriz = [ 
 #[1, 5, 1],
 #[2, 1, 2],
 #[3, 0, 1],
 #[1, 4, 4]
#]
#Debes llegar a: 
#matriz = [ 
 #[1, 5, 1, 7],
 #[2, 1, 2, 5],
 #[3, 0, 1, 4],
 #[1, 4, 4, 9]
#]
matriz = [ 
 [1, 5, 1],
 [2, 1, 2],
 [3, 0, 1],
 [1, 4, 4]
]
elemento1 = [sum(matriz[0])]
suma1 = (matriz[0] + elemento1)


elemento2 = [sum(matriz[1])]
suma2 = (matriz[1] + elemento2)

elemento3 = [sum(matriz[2])]
suma3 = (matriz[2] + elemento3)

elemento4 = [sum(matriz[3])]
suma4 = (matriz[3] + elemento4)

matriz = [
    suma1,
    suma2,
    suma3,
    suma4
]
print(matriz)