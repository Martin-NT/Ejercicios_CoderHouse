#Calcular la suma de una cantidad de números enteros ingresados por el usuario directamente utilizando la función input (). 
#Para finalizar la ejecución del programa, el usuario debe escribir la palabra exit(). El programa debe validar dicha acción. 
#Finalmente, el algoritmo debe mostrar la suma parcial y total obtenida.
lista_num = []
while True:
    num = input("Ingresa un numero ('exit' termina el ingreso): ")
    if num == "exit":
        break
    lista_num.append(int(num))
    
print(f"La suma de los numeros dan {sum(lista_num)}")


#n = 0
#while True:
  #numero = input("Ingrese un número: ")
  #if numero == "exit()":
    #break
  #n += int(numero)

#print(f"La suma de los numeros ingresados es {n}")