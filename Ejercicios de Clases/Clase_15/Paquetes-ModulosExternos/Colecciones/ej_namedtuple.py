from collections import namedtuple
#Esto crea una clase perro con los atributos publicos nombre, raza y edad
perro = namedtuple("Perro", ["nombre", "raza", "edad"])

mi_perro = perro("Tobi", "Caniche", 4)
print(mi_perro) #Perro(nombre='Tobi', raza='Caniche', edad=4)
print(type(mi_perro)) #<class '__main__.Perro'>

dic_perro = mi_perro._asdict()
print(dic_perro) #{'nombre': 'Tobi', 'raza': 'Caniche', 'edad': 4}
print(type(dic_perro)) #<class 'dict'>

