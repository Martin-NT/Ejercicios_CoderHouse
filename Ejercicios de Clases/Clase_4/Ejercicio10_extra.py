#Dos equipos de futbol están disputando el saque inicial del juego.
#Los capitanes de cada equipo deciden jugar el clásico juego “Piedra, papel o tijera” para definir quien hace el saque.
#Las reglas son las usuales: Piedra vence a Tijera, Tijera vence a Papel y Papel vence a Piedra.
#Juegan una sola vez.
print("Hola yo soy el Arbitro y para ver quien hace el saque final, haremos un Piedra, Papel o Tijera...")
equipo1 = input("Ingrese el nombre del primer equipo: ")
equipo2 = input("Ingrese el nombre del segundo equipo: ")
respuesta1 = (input(f"{equipo1} Piedra, Papel o Tijera?: ")).lower()
respuesta2 = (input(f"{equipo2} Piedra, Papel o Tijera?: ")).lower()


if respuesta1 == respuesta2:
    print("Hubo un empate, no hay ganador en el saque inicial")
elif respuesta1 == "piedra":
    if respuesta2 == "tijera":
        print(f"{equipo1} gana, hace el saque inicial")
    else: 
        print(f"{equipo2} gana, hace el saque inicial")
elif respuesta1 == "tijera":
    if respuesta2 == "papel":
        print(f"{equipo1} gana, hace el saque inicial")
    else:
        print(f"{equipo2} gana, hace el saque inicial")
elif respuesta1 == "papel":
    if respuesta2 == "piedra":
        print(f"{equipo1} gana, hace el saque inicial")
    else:
        print(f"{equipo2} gana, hace el saque inicial")
else: 
    print("Elección inválida. Por favor, elijan entre piedra, papel o tijera.")
    
