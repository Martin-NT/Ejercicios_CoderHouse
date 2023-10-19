# Utilizando todo lo que sabes sobre cadenas, listas y sus métodos internos, transforma este texto:
# gordon lanzó su curva&strawberry ha fallado por un pie! 
# -gritó Joe Castiglione&dos pies -le corrigió 
# Troop&strawberry menea la cabeza como disgustado… 
# -agrega el comentarista

# Transforma el texto en:
# Gordon lanzó su curva...
# - Strawberry ha fallado por un pie! -gritó Joe Castiglione.
# - Dos pies le corrigió Troop.
# - Strawberry menea la cabeza como disgustado… -agrega el comentarista.
#Lo único prohibido es modificar directamente el texto

texto = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"

texto = texto.replace("&", "\n- ")
texto = texto.replace("gordon", "Gordon")

texto = texto.replace("lanzó su curva", "lanzó su curva...")
texto = texto.replace("Grito Joe Castiglione", "Grito Joe Castiglione.")

texto = texto.replace("dos pies ", "Dos pies ")
texto = texto.replace("-le corrigió Troop", "le corrigió Troop.")
texto = texto.replace("menea la cabeza como disgustado…", "menea la cabeza como disgustado...")
texto = texto.replace("strawberry", "Strawberry")
print(texto)