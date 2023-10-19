partidos_ganados = int(input("¿Cuantos partidos ganaron?: "))
partidos_perdidos = int(input("¿Cuantos partidos perdieron?: "))
partidos_empatados = int(input("¿Cuantos partidos empataron?: "))

partidos_totales = (partidos_ganados + partidos_empatados + partidos_perdidos)

puntosPorGanar = partidos_ganados * 3
puntosPorEmpatar = partidos_empatados * 1
puntosPorPerder = partidos_perdidos * 0

puntos_totales = (puntosPorGanar + puntosPorEmpatar + puntosPorPerder)

promedio_final = puntos_totales / partidos_totales

print("Obtuvieron en total " , puntos_totales , " puntos") 
print(" De los cuales " , puntosPorGanar , " puntos por ganar, " , puntosPorEmpatar , " puntos por empatar y " , puntosPorPerder , " por perder")
print("El promedio final es de: " , promedio_final)