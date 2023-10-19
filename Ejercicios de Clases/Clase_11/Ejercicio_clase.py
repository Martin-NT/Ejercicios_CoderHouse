#Realizar una funcion que reciba como argumento un texto que debera ser mostrado al usuario (p.e. Ingrese su edad), 
# la funcion debera solictar un numero, validar que sea un numero y devolverlo por return En caso que el usuario no ingrese un numero, 
# debera volver a pedir el numero

# Manera 1
def solicitar_numero(mensaje):
  while True:
    try:
      n = int(input(mensaje))
      return n
    except:
      print("Por favor ingrese un número")


dni = solicitar_numero("Por favor ingresa tu DNI:")
edad = solicitar_numero("Por favor ingresa tu Edad:")
cuenta = solicitar_numero("Por favor ingresa tu Saldo de CA:")

print(f"Uds tiene DNI {dni}, su edad es {edad} y su Caja de Ahorro es {cuenta}")

# Manera 2
def solicitar_numero(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            return num
        except:
            print("Por favor ingresa un numero")
           
while True:    
    mensaje = input("Ingrese un texto (fin para salir): ")
    if mensaje.lower() == "fin":
        break
    else:
        a = solicitar_numero(mensaje)
        print(a)
        