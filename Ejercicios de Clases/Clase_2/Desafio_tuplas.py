tupla = (8,15,4,39,5,89,87,19,7,-755,88,123,2,11,15,9,355)
print("tupla =" , tupla)

print("El último ítem de tupla:")
print(tupla[-1:])

print("El número de ítems de tupla:")
print(len(tupla))

print("La posición donde se encuentra el ítem 87 de tupla:")
print(tupla.index(87))

print("Una lista con los últimos tres ítems de tupla:")
lista = list(tupla)
print(lista[-3::])

print("Un ítem que haya en la posición 8 de tupla:")
print(tupla[8])

print("El número de veces que el ítem 7 aparece en tupla:")
print(tupla.count(7))