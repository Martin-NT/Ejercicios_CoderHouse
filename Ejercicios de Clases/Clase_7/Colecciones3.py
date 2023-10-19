
#Escribir un programa que guarde en una variable en un diccionario 
#{'Dolar':'$','Euro':'€', 'Libra':'£'}. 
#Luego se le deberá solicitar al usuario que ingrese la divisa que desea visualizar. 
#En el caso de ingresar una divisa no existente en nuestro diccionario, 
#deberemos indicarle con un mensaje de notificación que la divisa no se encuentra disponible.
   
divisas = {'Dolar': '$', 'Euro': '€', 'Libra': '£'}
divisa_ingresada = input("Ingrese la divisa que desea visualizar: ").capitalize()

if divisa_ingresada in divisas.keys():
    simbolo = divisas.get(divisa_ingresada)
    print(f"Usted ha elegido {divisa_ingresada} {simbolo}")
elif divisa_ingresada in divisas.values():
    for key, value in divisas.items():
        if value == divisa_ingresada:
            print(f"Usted ha elegido {key} {divisa_ingresada}")
            break
else:
    print("La divisa no se encuentra disponible.")
