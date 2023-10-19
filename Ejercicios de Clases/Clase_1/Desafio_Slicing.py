cadena = "I olucláC , 01 , orravaN nitraM"
cadena_volteada = cadena[::-1]

nombre_alumno = cadena_volteada[0:14:1]
nota = cadena_volteada[17:19:1]
materia = cadena_volteada[22:31:1]

print(cadena_volteada)
print("Nombre Alumno: " , nombre_alumno)
print("Nota: " , nota)
print("Materia: " , materia)
print(nombre_alumno , "ha sacado un" , nota , "en" , materia)

del cadena
cadena = "acitametaM ,5.8 ,otipeP ordeP"
cadena_formateada = cadena[::-1]

nombre_alumno = cadena_formateada[0:12:1]
nota = cadena_formateada[14:17:1]
materia = cadena_formateada[19:29:1]
print(cadena_formateada)
print("Nombre Alumno: " , nombre_alumno)
print("Nota: " , nota)
print("Materia: " , materia)
print(nombre_alumno , "ha sacado un" , nota , "en" , materia)
