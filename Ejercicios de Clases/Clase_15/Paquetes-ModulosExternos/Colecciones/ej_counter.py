from collections import Counter

lista = [1,2,3,4,1,2,3,1,2,1]
print(Counter(lista)) #Counter({1: 4, 2: 3, 3: 2, 4: 1})
#Si fuera texto
estudiantes = "Martin Vale Delfi Martin Delfi Marti"
print(Counter(estudiantes)) #Counter({'i': 5, ' ': 5, 'a': 4, 'M': 3, 'r': 3, 't': 3, 'l': 3, 'e': 3, 'n': 2, 'D': 2, 'f': 2, 'V': 1})
print(Counter(estudiantes.split())) #Counter({'Martin': 2, 'Delfi': 2, 'Vale': 1, 'Marti': 1})


