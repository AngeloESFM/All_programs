# COMPROBAR SI ES UN PALINDROMO

"""cadena = "Allí por la tropa portado, traído a ese paraje\
de maniobras, una tipa como capitán usar boina\
me dejara, pese a odiar toda tropa por tal ropilla."
"""
cadena = input("escribe la frase")

#PASAMOS LAS LETRAS A MINUSCULAS
minusculas = cadena.lower()
palabras = minusculas.split()

print(palabras)

#QUITAR COMAS Y PUNTOS

lista_plana = []
for s in palabras:
    q = s.strip('.').strip(',')
    lista_plana.append(q)

print(lista_plana)

cadena_plana = "".join(lista_plana)

#QUITAR LAS TÍLDES

cadena_plana = cadena_plana.replace("á","a").replace("é","e")\
                .replace("í","i").replace("ó","o").replace("ú","u")
print(cadena_plana)

#REVERTIMOS LA CADENA
palindromo = cadena_plana[::-1]
print(palindromo)

#comparamos la cadena con su reverso
if cadena_plana == palindromo:
   print("Son palíndromos.")
else:
   print("No son palíndromos.")


#tambien se puede hacer con la palabra ISALPHA

"""
#PASAMOS LAS LETRAS A MINUSCULAS
minusculas = cadena.lower()


# QUITAR COMAS Y PUNTOS

cadena_plana = ""

for letra in minusculas:
   if letra.isalpha():
       cadena_plana += letra

# QUITAR LAS TÍLDES

cadena_plana = cadena_plana.replace("á","a").replace("é","e")\
                .replace("í","i").replace("ó","o").replace("ú","u")
print(cadena_plana)

#REVERTIMOS LA CADENA
palindromo = cadena_plana[::-1]
print(palindromo)

#comparamos la cadena con su reverso
if cadena_plana == palindromo:
   print("Son palíndromos.")
else:
   print("No son palíndromos.")
"""


import statistics
datos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
algo = statistics.stdev(datos)

print(algo)