#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que 
# debe cobrar a sus clientes por entrar.
#El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
#Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 80 ARS y si es mayor de 18 años, 150 ARS.
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad < 4:
    precio = 0
elif edad >= 4 and edad < 18:
    precio = 80
elif edad >= 18:
    precio = 150
else:
    print("Usted no tiene permitido jugar")
    
print(f"Hola {nombre}, Bienvenido a Play House, por tener {edad} años el precio de entrada es de ${precio}")