# 27 FUNCIONES DE LAS LISTAS O VECTORES
# Se verá que cosas se puede hacer con las listas o vectores

numeros = [5, 2, 23, 55, 1, 9, 6]
frutas = ["Naranja", "Manzana", "Banana", "Kiwi", "Mandarina", "Uva", "Naranja"]

print ("LISTA ORIGINAL DE FRUTAS")
print (frutas)
print ()

# FUNCIONES DE LAS LISTAS
# LEN, APPEND, EXTEND, INSERT, REMOVE, CLEAR, POP, INDEX, COUNT, SORT, REVERSE, COPY
# Para cambiar un elemento de la lista por otro, se hace lo siguiente, cambiar piña por manzana
frutas[1] = "Piña"
print (frutas)
# LEN = Sirve para ver el tamaño de la lista
print (len(frutas))
# APPEND = Sirve para agregar un elemento al final de la lista
frutas.append("Manzana")
print(frutas)
# EXTEND = Sirve para agregarle a una lista, otra lista, pero sin modificarla
# Sin modificarla
numeros.extend(frutas)
print(numeros)
# Modificándola
numeros = numeros + frutas
print(numeros)
# INSERT = Sirve para agregar un elemento a la lista en la posición que se quiera, y las otras se recorren
# lista.INSERT(lugar_donde_se_colocará, elemento_que_se_colocará)
frutas.insert(2, "Sandía")
print (frutas)
# REMOVE = Sirve para eliminar un elemento de la lista
frutas.remove("Kiwi")
print (frutas)
# CLEAR = Sirve para eliminar todos los elementos de la lista
#frutas.clear()
#print (frutas)
# POP = Sirve para eliminar el último elemento de la lista y se pueden hacer varios, elimina el último siempre
frutas.pop()
frutas.pop()
print(frutas)
# INDEX = Sirve para saber en que índice (o posición) esta el elemento dicho
print(frutas.index("Naranja"))
# COUNT = Sirve para contar cuantos elementos hay en la lista
print(frutas.count("Naranja"))
# SORT = Sirve para ordenar los datos de mayor a menor
# (para que de aqui en adelante funcione el programa, hay que comentar las anteriores)
frutas.sort()
print(frutas)
numeros.sort()
print(numeros)
# REVERSE = Sirve para voltear los indices ( o las posiciones) en las listas
frutas.reverse()
print(frutas)
# COPY = Sirve para dar una copia exacta de una lista y almacenarla en otra variable dándole otro lugar en la memoria la hace mutable
# si modificamos frutas2 no se modifica la original y viceversa
frutas2 = frutas.copy()
print (frutas2)
# LIST = Convierte cada letra de una palabra en un elemento de una lista
palabra = "palabra"
palabra = list(palabra)
print(palabra)
# SPLIT = Convierte cada palabra separada por espacios o se puede especificar el tipo de separación en elementos de una lista
sample = "Así,  separa por comas, en elementos, de, una, lista"
sample = sample.split(',')
print(sample)
esp = "Asi separa por espacios en elementos de una lista"
por_espacios = esp.split()
print(por_espacios)
