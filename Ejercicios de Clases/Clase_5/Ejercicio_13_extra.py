#13) La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.
#Ingredientes vegetarianos: Pimiento y tofu. 
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón. 
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú 
# con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están 
# en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
print("Bienvenido a la Pizzeria Bella Napoli")
print("Tenemos Pizzas Vegetarias y No Vegetarias")
pizza = (input("Que Pizza desea pedir?: ")).capitalize()
if pizza.lower() == "vegetariana":
    ingredientes = ["Mozarella", "Tomate"]
    ingredientes_elegir = ["Pimiento", "Tofu"]
    for i in ingredientes_elegir:
        print(f"Ingredientes disponibles para elegir: {i}")
       
    print("Solo puede elegir un solo ingrediente adicional")
    respuesta = (input("Que ingrediente elije?: ")).capitalize()
    
    if respuesta.lower() == "pimiento":
        pizza_elegida = [str(ingredientes) + " y " + str(respuesta)]
        print(f"Usted ha seleccionado la Pizza {pizza} con los ingredientes: {pizza_elegida}")
        
    elif respuesta.lower() == "tofu":
        pizza_elegida = [str(ingredientes) + " y " + str(respuesta)]
        print(f"Usted ha seleccionado la Pizza {pizza} con los ingredientes: {pizza_elegida}") 
   
    else: 
        print("Ese ingrediente no esta disponible, porfavor elija uno nuevamente")
        while True:
            print("Recuerde solo puede elegir un solo ingrediente adicional")
            respuesta = (input("Que ingrediente elije?: ")).capitalize()
            if respuesta.lower() == "pimiento":
                pizza_elegida = [str(ingredientes) + " y " + str(respuesta)]
                print(f"Usted ha seleccionado la Pizza {pizza} con los ingredientes: {pizza_elegida}")
                break
            elif respuesta.lower() == "tofu":
                pizza_elegida = [str(ingredientes) + " y " + str(respuesta)]
                print(f"Usted ha seleccionado la Pizza {pizza} con los ingredientes: {pizza_elegida}") 
                break
            else:
                print("Ese ingrediente no esta disponible")
                continue
            
         
elif pizza.lower() == "no vegetariana":
    ingredientes = ["Mozarella", "Tomate"]
    ingredientes_elegir = ["Peperoni", "Jamon", "Salmon"]
    for i in ingredientes_elegir:
        print(f"Ingredientes disponibles para elegir: {i}")
        
    print("Solo puede elegir un solo ingrediente adicional")
    respuesta = (input("Que ingrediente elije?: ")).capitalize()
    
    if respuesta.lower() == "peperoni":
        pizza_elegida = [str(ingredientes) + " y " + str(respuesta)]
        print(f"Usted ha seleccionado la Pizza {pizza} con los ingredientes: {pizza_elegida}") 
              
    elif respuesta.lower() == "jamon":
        pizza_elegida = [str(ingredientes) + " y " + str(respuesta)]
        print(f"Usted ha seleccionado la Pizza {pizza} con los ingredientes: {pizza_elegida}") 
        
    elif respuesta.lower() == "salmon":
        pizza_elegida = [str(ingredientes) + " y " + str(respuesta)]
        print(f"Usted ha seleccionado la Pizza {pizza} con los ingredientes: {pizza_elegida}")
        
    else: 
        print("Ese ingrediente no esta disponible, porfavor elija uno nuevamente")
        while True:
            print("Recuerde solo puede elegir un solo ingrediente adicional")
            respuesta = (input("Que ingrediente elije?: ")).capitalize()
            if respuesta.lower() == "peperoni":
                pizza_elegida = [str(ingredientes) + " y " + str(respuesta)]
                print(f"Usted ha seleccionado la Pizza {pizza} con los ingredientes: {pizza_elegida}")
                break
            elif respuesta.lower() == "jamon":
                pizza_elegida = [str(ingredientes) + " y " + str(respuesta)]
                print(f"Usted ha seleccionado la Pizza {pizza} con los ingredientes: {pizza_elegida}") 
                break
            elif respuesta.lower() == "salmon":
                pizza_elegida = [str(ingredientes) + " y " + str(respuesta)]
                print(f"Usted ha seleccionado la Pizza {pizza} con los ingredientes: {pizza_elegida}") 
                break
            else:
                print("Ese ingrediente no esta disponible")
                continue
else:
    print("Esa Pizza no esta en el Menu")
    #PODRIA PONER QUE REPITA TODO
