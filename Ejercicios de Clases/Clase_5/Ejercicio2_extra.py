#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable,
# y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales

while True:
    nombre = input("Ingrese su nombre (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    
    peso = input("Ingrese su peso en kg (o 'fin' para terminar): ")
    if peso.lower() == "fin":
        break
    
    estatura = input("Ingrese su estatura en metros (o 'fin' para terminar): ")
    if estatura.lower() == "fin":
        break

    peso = float(peso)
    estatura = float(estatura)

    indice_masa_corporal = peso / (estatura ** 2)
    indice_masa_corporal = round(indice_masa_corporal, 2)

    print(f"{nombre}, tu índice de masa corporal es {indice_masa_corporal}")
