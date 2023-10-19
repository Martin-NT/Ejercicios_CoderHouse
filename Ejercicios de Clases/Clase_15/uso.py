#Si esta en otra carpeta -> from carpeta.archivo import <lo que se quiera importar>
from paquete.modulo1 import *
# Si modulo1.py estuviese en la misma carpeta que uso.py (* = todo )
#from modulo1 import *
#from modulo1 import Persona, potencia, saludar, paises

print(paises["Arg"]) #Argentina
persona1 = Persona("Martin", "Navarro", "Calle Lavalle 640", 19) 
print(f"El objeto persona1 es {persona1}") #El objeto persona1 es Navarro, Martin
print(potencia(3,3)) #27
print(saludar("Martin")) #Hola Martin!

from paquete.modulo2 import solicitar_numero

mi_numero = solicitar_numero("Ingrese un numero: ")
