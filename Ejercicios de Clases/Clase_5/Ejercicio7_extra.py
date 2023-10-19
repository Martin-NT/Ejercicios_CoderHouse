#7) Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
# Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácte
while True:
    nacimiento = input("Ingrese la fecha de su nacimiento en formato dd/mm/aaaa (o 'fin' para terminar): ")
    if nacimiento.lower() == "fin":
        break 
    partes = nacimiento.split("/")
    print(partes)
    dia = partes[0]
    mes = partes[1]
    year = partes[2]
    if len(dia) == 1:
        dia = "0" + dia
        print(f"El dia es: {dia}")
    else:
        print(f"El dia es: {dia}")
    if len(mes) == 1:
        mes = "0" + mes
        print(f"El mes es: {mes}")
    else:
        print(f"El mes es: {mes}")
    print(f"El año es: {year}")