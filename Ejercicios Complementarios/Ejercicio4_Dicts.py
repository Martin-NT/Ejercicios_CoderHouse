#Consigna Dicts / Diccionarios
#Escribir un programa que le solicite al usuario su nombre, edad, dirección y que, posteriormente, lo muestre por pantalla:
#Ejemplo del output solicitado: 
# ✓ Juan tiene 25 años, y vive en Carrera 7 - Bogotá

info_usuario = {}

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
direccion = input("Ingrese su direccion: ")

info_usuario["nombre"] = nombre
info_usuario["edad"] = edad
info_usuario["direccion"] = direccion

print(f"{nombre} tiene {edad} años, y vive en {direccion} ")
