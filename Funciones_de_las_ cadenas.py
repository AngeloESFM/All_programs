#TRABAJAMOS CON CADENAS DE TEXTO

# Las cadenas pueden ser tratadas como listas
cadena = "Hola AcademiaCoder"

# H o l a   A c a d e  m  i  a  C  o  d  e  r
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
#                               ... -3  -2  -1

# Se escoge la posición que queremos mostrar entre corchetes
# nombre_de_la_cadena [número de la posición a mostar]
letra = cadena[5]
print(letra)
# Para ir de adelante hacía atrás se empieza en -1 y se ponen números negativos
letra = cadena[-18]
print(letra)

# Para darle un intervalo de posiciones es
# nombre de la cadena[número de la posición inicial:número de la posición final obtendra una posición anterior]
letras = cadena[2:13]
print(letras)
# Si no se le indica el rango, regresa todos los datos siguientes o anteriores
letras = cadena[5:]
print(letras)
letras = cadena[:13]
print(letras)

#no pueden ser modificadas como las listas, osea no son mutables

#FUNCIONES DE LAS CADENAS DE TEXTO
# Todas las funciones están en https://docs.python.org/3/library/stdtypes.html#string-methods
# nombre de la cadena.nombre de la función a utilizar. otra función ----> puede concatenar las funciones
modificada = cadena.capitalize()
print(modificada)
modificada = cadena.upper().isupper()
print(modificada)
modificada = cadena.split()
print(modificada)
cadena_comas = "Marcos,Natalia,Rosa"
lista_nombres = cadena_comas.split(',')
print(lista_nombres)
