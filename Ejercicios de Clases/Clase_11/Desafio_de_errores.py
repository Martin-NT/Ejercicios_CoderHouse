# Retorna None cuando sucede el fallo
# Descripción de la actividad. 
# En la función de nuestro ejercicio hay un fallo potencial, averigua cuándo sucede y retorna el valor None en ese caso especial, 
# en cualquier otro caso devuelve el resultado normal de la función.
# >>> def dividir(a, b):
# return a/b
# Pista: Valor indeterminado

# Sin excepcion
def dividir(num1,num2):
    if num2 != 0:
        return num1 / num2
    return None

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
resultado = dividir(num1,num2)
print(resultado)
