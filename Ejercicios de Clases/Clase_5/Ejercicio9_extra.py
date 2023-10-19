#9) Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
# y muestre por pantalla la lista resultante.
abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
abc_sin_m3 = []
indice = 3
n = 1
for n, abecedario in enumerate(abecedario):
    print(n, "-", abecedario)
print(enumerate(abecedario))

for n, letra in enumerate(abecedario):
    if n % 3 != 0:
        abc_sin_m3.append(letra)

print(abc_sin_m3)
#TERMINAR