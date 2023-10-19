lista1 = [456789]
lista1.append("Hola Mundo")
print(lista1)

lista2 = ["Hola y Adios"]
lista2.append(5555)
print(lista2)

lista3 = [lista1.pop()] #lista1[:-1]
print(lista3)

lista4 = lista2[1:-1]
print(lista4)

lista5 = lista4 + lista3
print(lista5)