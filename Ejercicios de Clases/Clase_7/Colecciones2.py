#Ejecuta el código para analizar cada una de las salidas!

#Ejemplo 1:
my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.union(my_set_2)
print(my_new_set) #{1, 2, 3, 4, 5}

#Ejemplo 2:
my_set_3 = set([1, 2, 3])
my_set_4 = set([3, 4, 5])
my_new_set = my_set_3.intersection(my_set_4)
print(my_new_set) #{3}

#Ejemplo 3:
my_set_5 = set([1, 2, 3])
my_set_6 = set[3, 4, 5]
my_new_set = my_set_5.difference(my_set_6)
print(my_new_set) #{1, 2, 3}