#8) Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla el mensaje Yo estudio , donde es cada una de las asignaturas de la lista.
asignaturas = []
while True:
    estudio = input("Ingrese la asignatura que estudia (o 'fin' para terminar): ")
    if estudio.lower() == "fin":
        break
    asignaturas.append(estudio)

print("Lista de asignaturas:")
for asignatura in asignaturas:
    print(f"Yo estudio {asignatura}")

