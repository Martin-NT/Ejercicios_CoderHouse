#10)Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
palabra  = input("Ingrese una palabra: ")
vocal = ["a", "e", "i", "o", "u"]
vocales_contador = {} #diccionario vacio 
print(f"En la palabra {palabra} se encuentran las vocales:")
for letra in palabra.lower():
    if letra in vocal:
        cantidad = (palabra.lower()).count(letra)
        if cantidad > 1:
            print(f"La vocal {letra} esta {cantidad} veces")
        elif cantidad == 1:
            print(f"La vocal {letra} esta {cantidad} vez")
        
#TERMINAR
            
        
