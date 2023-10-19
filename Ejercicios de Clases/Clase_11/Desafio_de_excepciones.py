#Descripción de la actividad. 
#Tomando la solución del ejercicio anterior, en lugar de devolver None al dividir entre cero, tienes 
# que capturar una excepción que muestre por pantalla EXACTAMENTE el mensaje: “No se puede dividir entre cero”; si falla el código
#>>> def dividir(a, b):
#if b == 0:
# return None
#return a/b

# Con excepcion 
def dividir(num1,num2):
    try:
        return num1 / num2 
    except:
        return None

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
resultado = dividir(num1,num2)
print(resultado)