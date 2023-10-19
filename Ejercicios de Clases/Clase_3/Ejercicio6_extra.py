#Ejercicio 6
#En nuestro trabajo alguien por error ha invertido todos los nombre de usuarios de la base de datos:
#base_de_datos = ["77ordep", "727alimay", "solrac_nauj", "zerimaroticlos", "nimdaesuohredoc", "samot_zemog", "setag_llib", "ecalevol-ada"]
#Nos solicitaron que accedamos a cada uno de esos datos, los acomodemos y los volvamos a ingresar a la base de datos

base_de_datos = ["77ordep", "727alimay", "solrac_nauj", "zerimaroticlos", "nimdaesuohredoc", "samot_zemog", "setag_llib", "ecalevol-ada"]

elemento1 = (base_de_datos[0])[::-1]
print(elemento1)
elemento2 = (base_de_datos[1])[::-1]
print(elemento2)
elemento3 = (base_de_datos[2])[::-1]
print(elemento3)
elemento4 = (base_de_datos[3])[::-1]
print(elemento4)
elemento5 = (base_de_datos[4])[::-1]
print(elemento5)
elemento6 = (base_de_datos[5])[::-1]
print(elemento6)
elemento7 = (base_de_datos[6])[::-1]
print(elemento7)
elemento8 = (base_de_datos[7])[::-1]
print(elemento8)

base_de_datos_actualizada = [elemento1, elemento2, elemento3, elemento4, elemento5, elemento6, elemento7, elemento8]
print("-----------------------------------------------------------------------------------------------------------------------------------------")
print("La base de datos ha sido actualizada...")
print(base_de_datos_actualizada)