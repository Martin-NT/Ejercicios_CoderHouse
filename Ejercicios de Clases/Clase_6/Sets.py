#Descripción de la actividad. 
#Trabajaremos con el notebook de la sesión, específicamente sobre la temática de Sets. 
#Crear un conjunto en Python que posea los siguientes elementos: 
# ✔ Colores: Rojo, Blanco, Azul.
# ✔ Posteriormente, agrega nuestro set de colores, los valores de: Violeta y Dorado
# ✔ Elimina a los colores: Celeste, Blanco y Dorado
#Pregunta: ¿Qué pasa si queremos eliminar el color Celeste utilizando el método discard?

colores = {"Rojo", "Blanco", "Azul"}
colores.update(["Violeta", "Dorado"])
print(colores) # {'Violeta', 'Rojo', 'Azul', 'Dorado', 'Blanco'}

#colores.remove("Celeste") #Da error ya que no esta
colores.discard("Celeste") #No pasa nada, aunque no este el color en el conjunto
colores.discard("Blanco") # == colores.remove("Blanco")
colores.discard("Dorado") # == colores.remove("Dorado")
print(colores) # {'Violeta', 'Rojo', 'Azul'}