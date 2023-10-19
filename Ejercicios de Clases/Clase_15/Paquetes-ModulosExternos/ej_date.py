#Librerias de Python
from datetime import datetime, timedelta

hoy = datetime.now()
# año, mes, dia, hora, minuto
fecha_nacimiento = datetime(2003,10,15,0,0)
naciste_hace = hoy - fecha_nacimiento

print(f"Hoy es {hoy}") #Hoy es 2023-08-01 15:12:31.681061
print(f"Naciste el {fecha_nacimiento} ") #Naciste el 2003-10-15 00:00:00 
print(f"Naciste hace {naciste_hace}") #Naciste hace 7230 days, 15:12:31.681061

#Para Personalizar la forma en la que se muestra datetime
hoy_personalizado = hoy.strftime("%A %d %B %Y %I:%M")
nacimiento_personalizado = fecha_nacimiento.strftime("%A %d %B %Y %I:%M")
print(f"Hoy es {hoy_personalizado}") #Hoy es Tuesday 01 August 2023 03:12
print(f"Naciste el {nacimiento_personalizado} ") #Naciste el Wednesday 15 October 2003 12:00 

#Con la función timedelta() también puedes sumar o restar tiempos
#Generamos 14 dias con 6 horas y 1000 segundos de tiempo
t = timedelta(days=14, hours=6, seconds=1000) 
# Lo operamos con el datetime de la fecha y hora actual
dentro_de_2_semanas = hoy + t
print(f"Dentro de 2 Semanas: {dentro_de_2_semanas}") #Dentro de 2 Semanas: 2023-08-15 21:29:11.681061

