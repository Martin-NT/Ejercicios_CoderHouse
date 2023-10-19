
nombre = input("Ingrese su Nombre: ")
edad = int(input("Ingrese su Edad: "))

condiciones = (nombre != "****" and (len(nombre) >= 4 and len(nombre) <= 8)) and ((edad > 5 and edad < 20) and (edad * 3) > 35)

#nombre != "****" and (len(nombre) >= 4 and len(nombre) <= 8)
#edad = (edad > 5 and edad < 20) and (edad * 3) > 35

# es valido 5 < edad < 20

#condicion1 = nombre != "****"
#condicion2 = edad > 5 and edad < 20
#condicion3 = len(nombre) >= 4 and len(nombre) <= 8
#condicion4 = (edad * 3) > 35

print(condiciones)


