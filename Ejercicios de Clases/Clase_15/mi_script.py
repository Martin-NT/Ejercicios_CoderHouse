#Importar una libreria 
import sys 

#Recibir argumentos (argv [lista])
#print(sys.argv) #Imprime los argumentos que le paso

for persona in sys.argv[1:]:
    print(f"Hola {persona}! Bienvenido al curso de Python")

## EN LA TERMINAL (powershell)
#LE PASO ARGUMENTOS
# (Con el print(sys.argv))
#python .\mi_script.py MARTIN VALE MARTI
#python .\mi_script.py 1 2 3 4 Hola Chau
# (Con el for)
#python .\mi_script.py MARTIN MARTI VALE DELFI JUANCHI LAUTY FACU

#DEVUELVE (una lista)
#['.\\mi_script.py', 'MARTIN', 'VALE', 'MARTI']
#['.\\mi_script.py', '1', '2', '3', '4', 'Hola', 'Chau']

#Hola MARTIN! Bienvenido al curso de Python
#Hola MARTI! Bienvenido al curso de Python
#Hola VALE! Bienvenido al curso de Python
#Hola DELFI! Bienvenido al curso de Python
#Hola JUANCHI! Bienvenido al curso de Python
#Hola LAUTY! Bienvenido al curso de Python
#Hola FACU! Bienvenido al curso de Python