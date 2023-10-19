#Consigna
#✓ Trabajas en Coderhouse y te piden crear un programa que calcule la nota final de estudiantes del curso de Python.
# La nota final se calcula basándonos en tres notas previas de las cuales, cada una corresponde un porcentaje distinto de la nota final.
#Los porcentajes asociados que debemos considerar de cada nota se detallan a continuación: 
#✓ nota_1 cuenta como el 20% de la nota final
#✓ nota_2 cuenta como el 30% de la nota final
#✓ nota_3 cuenta como el 50% de la nota final
#Aspectos a incluir
#✓ Tener en cuenta los temas vistos en la clase 1: números, print, input, variables, operaciones matemáticas, cadena de texto. 
#✓ Los datos deben guardarse en variables y deben ser dinámicos por medio de input.

print("Bienvenido a CoderHouse")
alumno = input("Ingrese nombre del estudiante: ")
nota_1 = int(input("Ingrese la primer nota: "))
nota_2 = int(input("Ingrese la segunda nota: "))
nota_3 = int(input("Ingrese la tercer nota: "))

porcentaje_nota1 = (nota_1 * 0.20)
porcentaje_nota2 = (nota_2 * 0.30)
porcentaje_nota3 = (nota_3 * 0.50)

print("El Porcentaje de la primer nota es: " , porcentaje_nota1)
print("El Porcentaje de la segunda nota es: " , porcentaje_nota2)
print("El Porcentaje de la tercer nota es: " , porcentaje_nota3)

promedio_final = (porcentaje_nota1 + porcentaje_nota2 + porcentaje_nota3)
print("El Promedio Final de " , alumno , " es de: " , promedio_final)