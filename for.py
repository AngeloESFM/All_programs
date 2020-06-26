# 39 BÚCLE FOR
# Sirve como un búcle y recorre toda una colección de datos

# la variable "letra" puede ser cualquier variable y sirve para recorrer la cadena
"""
for letra in  "AcademiaCoder":
    print(letra, id(letra))

# Si imprimimos "letra" fuera del for, nos da el último valor de la colección, en este caso la r
print(letra)
print(id(letra))

# También la podemos usar en listas

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

for dia in dias:
    print(dia)

print(dia)

# Si lo úsamos para un diccionario, se hace de la siguiente forma, junto con comando ITEMS

dias = {"lu": "Lunes","ma": "Martes","mi": "Miércoles","ju": "Jueves","vi": "Viernes"}

for clave,valor in dias.items():        # ITEMS recibe dos datos para los diccionarios
    print(clave)
    print(valor)
    print(clave, valor)
"""
# Si usamos RANGE(algun_rango) nos va a elegir el rango que indiquemos de nuestra colección
"""
for indice in range(5):       # Así muestra los rangos del 0 al 4
    print(indice)

for indice in range(2,5):     # Así muestra los rangos del 2 al 4
    print(indice)

for indice in range(1, 11, 2):      # Así muestra los rangos del 1 al 10, pero de dos en dos
    print(indice)
"""
# De la forma que a continuación viene puedes elegir el rango de lo que quieres recorrer

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# Así eliges el número de rango pero imprimiendo los días
for indice in range(5):
    print(dias[indice])

# y también con el comando len, para decir la longitud de la lista
for indice in range(len(dias)):
    print(dias[indice])

print(len(dias))

# Para elegir un ganador podemos hacerlo de la siguiente forma

for indice in range(10):
    if indice == 4:
        print("Ganaste")
    else:
        print("No eres ganador")

# También se pueden anidar los FOR, dónde recorre los de adentro primero y después los de afuera

for indice in range(5):
    for indice2 in range(3):
        print(indice, indice2)