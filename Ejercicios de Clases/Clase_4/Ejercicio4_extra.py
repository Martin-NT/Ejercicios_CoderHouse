#Cree un programa que calcule el IMC (Indice de masa corporal). Formula –> IMC=Peso/Altura2 (Peso sobre altura al cuadrado)
#El usuario debera ingresar su peso y su altura (su nombre si quieren y despues imprimirlo concatenado) y el programa ademas de calcular el IMC 
# debera decir en que clasificacion se encuentra.

#La clasificacion la encontraran el archivo de imagen: IMC_clasificacion.jpg (en el archivo comprimido)
nombre = input("Ingrese su nombre: ")
peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (m): "))
imc = peso / (altura)**2

print(f"Hola {nombre}")
if imc < 18.5:
    clasificacion = "Insufciencia ponderal"
    print("Se encuentra en la clasificación: Insuficiencia ponderal")
elif imc >= 18.5 and imc < 25.0:
    clasificacion = "Intervalo normal"
    print("Se encuentra en la clasificación: Intervalo normal")
elif imc >= 25.0 and imc < 30.0:
    clasificacion = "Sobrepeso"
    print("Se encuentra en la clasificación: Sobrepeso")
elif imc >= 30.0:
    clasificacion = "Obesidad"
    print("Se encuentra en la clasificación: Obesidad")
else:
    print("No se encuentra en ninguna clasificación")

print(f"Hola {nombre}, usted de encuentra en la clasificación {clasificacion}")