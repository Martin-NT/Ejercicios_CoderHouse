#Descripción de la actividad. 
#Realiza una función que, dependiendo de los parámetros que reciba, convierta a milímetros o a metros. 
#1- Si recibe un argumento, supone que son milímetros y convierte a metros, centímetros y milímetros.
#2- Si recibe 3 argumentos, supone que son metros, centímetros y milímetros y los convierte a milímetros.

def conversion_medidas(*args):
    if len(args) == 1:
        milimetros = args[0]
        print("milimetros", milimetros)
        metros = milimetros / 1000
        centimetros = milimetros / 10
        return metros, "metros", centimetros, "centimetros", milimetros, "milimetros"
    elif len(args) == 3:
        metros, centimetros, milimetros = args
        total_milimetros = metros * 1000 + centimetros * 10 + milimetros
        return total_milimetros, "milimetros"
    else:
        return "Error: La función debe recibir 1 o 3 argumentos."

print(conversion_medidas(1,2,3))