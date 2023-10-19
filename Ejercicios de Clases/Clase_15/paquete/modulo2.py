def solicitar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
        except:
            numero = 0
        else:
            break

    return numero