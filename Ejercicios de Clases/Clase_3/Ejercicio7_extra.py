#Ejercicio 7
# Usted trabaja en el área de sistemas de la empresa "Cambalache". Ahi tienen guardados en su base de datos todos los productos que venden, 
# en orden decreciente de ventas:
#productos = ["Smart TV", "Celular 8Gb", "Microondas 220V", "Camara de seguridad", "Lavarropa automatico", "Almohada inteligente", "Silla Gamer", "Heladera 200Litros", "Monitor PC 24 pulgadas", "Impresora 3D con autonivelacion", "Mouse y teclado"]
# El área de marketing le solicita que por favor le pasen los tres productos más vendidos porque quieren hacer una campaña con los mismos.
# A su vez el área de producción quiere saber cuales son los 3 menos vendidos, así frenan la compra de los mismos.
# El presidente de la empresa quiere saber en qué posición de venta está la silla gamer. ¿Por qué? Porque sí.
productos = ["Smart TV", "Celular 8Gb", "Microondas 220V", "Camara de seguridad", "Lavarropa automatico", "Almohada inteligente", "Silla Gamer", "Heladera 200Litros", "Monitor PC 24 pulgadas", "Impresora 3D con autonivelacion", "Mouse y teclado"]

productos_mas_vendidos = productos[0:3:1]
print("Los 3 productos mas vendidos son: " , productos_mas_vendidos)

productos_menos_vendidos = productos[8:11:1]
print("Los 3 productos menos vendidos son: " , productos_menos_vendidos)

posicion_de_venta = productos.index("Silla Gamer")
print("La Silla Gamer esta en la posicion de venta numero: " , posicion_de_venta)