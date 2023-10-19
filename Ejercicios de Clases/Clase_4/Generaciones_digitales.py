nacimiento = int(input("Ingrese año de nacimiento: "))

if nacimiento >= 1920 and nacimiento <= 1940:
    print("Usted pertenece a la Generación Silenciosa")
elif nacimiento >= 1941 and nacimiento <= 1945:
    print("Usted pertenece a la Generación NN")
elif nacimiento >= 1946 and nacimiento <= 1964:
    print("Usted pertenece a la Generación Baby Boomer")
elif nacimiento >= 1965 and nacimiento <= 1979:
    print("Usted pertenece a la Generación X")
elif nacimiento >= 1980 and nacimiento <= 2000:
    print("Usted pertenece a la Generación Y")
elif nacimiento >= 2001 and nacimiento <= 2010:
    print("Usted pertenece a la Generación Z")
elif nacimiento >= 2011:
    print("Usted pertenece a la Generación Alfa")
else: 
    print("Su Generación es anterior a la Generación Silenciosa ")