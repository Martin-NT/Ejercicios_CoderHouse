#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística 
# les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y 
# calcule el peso total del paquete que será enviado.
while True:
    payasos = input("Ingrese el número de payasos vendidos(o 'fin' para terminar): ")
    if payasos.lower() == "fin":
        break
    munecas = input("Ingrese el número de muñecas vendidas(o 'fin' para terminar): ")
    if munecas.lower() == "fin":
        break
    if not payasos.isnumeric() or not munecas.isnumeric():
        print("Ingrese valores numéricos válidos.")
        continue
    payasos = int(payasos)
    munecas = int(munecas)
    peso_payasos = payasos * 112
    peso_munecas = munecas * 75
    peso_total = peso_payasos + peso_munecas
    print(f"El peso total del paquete a enviar es de {peso_total} gramos.")
