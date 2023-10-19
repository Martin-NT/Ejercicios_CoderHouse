nombre = input("Ingrese su nombre: ")
preferencia = input("¿Cuál es tu preferencia (M o C)?: ")

# grupo_A = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
# grupo_B = ["n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#Use el metodo .lower() que convierte las mayusculas a minusculas (todavia no lo vemos)
if (nombre[0].lower() >= "a") and (nombre[0].lower() <= "m"):
    if (preferencia.lower() == "m"):
        print("Usted prefiere a Marvel y pertenece al Grupo A.")
    else:
        print("No se puede determinar tu preferencia o grupo.1")
elif (nombre[0].lower() >= "n") and (nombre[0].lower() <= "z"):
    if (preferencia.lower() == "c"):
        print("Usted prefiere a CapCom y pertenece al Grupo B.")
    else:
        print("No se puede determinar tu preferencia o grupo.2")
else:
    print("Usted no pertenece a ningun Grupo")
    