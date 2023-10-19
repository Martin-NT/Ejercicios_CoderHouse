import random as rn #Librerias de Python

lista = ["Martin Navarro", "Vale Rosales", "Marti Rizzotti", "Delfi Gomez", "Juanchi Narvaez", "Lauty Saniga", "Facu San Roman"]
aleatorio_lista = rn.choices(lista, k=1)

dado = [1,2,3,4,5,6]
aleatorio_dado = rn.choices(dado, k=1)

print(f"El ganador es {aleatorio_lista}")
print(f"Se tiro el dado y salio el {aleatorio_dado}")