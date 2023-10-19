#Ejercicio 5
# Una casa de electrodomesticos esta teniendo mucho exito en dos de sus productos: parlantes y microfonos. 
# Realiza los envios por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de 
# los parlantes y microfonos que saldran en cada paquete. Cada parlante pesa 500 gramos y cada microfono pesa 150 gramos. 
# Escribir un algoritmo que lea el número de parlantes y microfonos vendidos en el último pedido y calcule el peso total del paquete que será enviado.

peso_parlante = 500
peso_microfono = 150

pedido_parlante = int(input("Ingrese cuantos parlantes vendio: "))
pedido_microfono = int(input("Ingrese cuantos microfonos vendio: "))

peso_parlante_pedido = peso_parlante * pedido_parlante
peso_microfono_pedido = peso_microfono * peso_microfono

peso_total_pedido = peso_parlante_pedido + peso_microfono_pedido

print("El peso total del pedido es de: " , peso_total_pedido , "gramos")

