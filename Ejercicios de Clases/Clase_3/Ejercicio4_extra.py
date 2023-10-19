#Ejercicio 4
#nUna panadería vende flautitas de pan a 100 pesos cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribe un algoritmo que comience leyendo el número de flautitas vendidas que no son del día y muestre por pantalla 
# el precio habitual de una flautita de pan, el descuento que se le hace por no ser del dia y el coste final total.

precio_flautitas_pan = 100
descuento = 0.6

flautitas_vendidas_no_dia = int(input("Ingrese cuantas falutitas de pan vendio que no son del dia: "))

precio_descuento = precio_flautitas_pan * descuento
coste_final = (precio_flautitas_pan - precio_descuento) * flautitas_vendidas_no_dia

print("Precio habitual de una flautita de pan: $", precio_flautitas_pan)
print("Descuento por no ser del día:", precio_descuento)
print("Coste final total: $", coste_final)
