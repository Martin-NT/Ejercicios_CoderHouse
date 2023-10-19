#Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo
variable_numerica = float(input("Ingrese un numero: "))
if variable_numerica >= 0 and variable_numerica <= 10:
    print(f"El numero ingresado ({variable_numerica}) esta entre 0 y 10")
elif variable_numerica <= 0:
    print(f"El numero ingresado ({variable_numerica}) es un numero negativo")
else: 
    print(f"El numero ingresado ({variable_numerica}) es mayor a 10")