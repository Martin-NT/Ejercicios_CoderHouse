
edad = int(input("Ingrese su edad: "))
antiguedad = int(input("Ingrese su antigüedad: "))
ingreso = int(input("Ingrese su ingreso: "))

if edad >= 18 and antiguedad >= 3 and ingreso >= 2500:
    print("Se le aprueba el crédito")
elif antiguedad < 3 and ingreso >= 4000:
    print("Se le aprueba el crédito")
else:
    print("Lo siento el credito no puede ser aprobado actualmente")

