# 37 DICCIONARIOS
# Sirven para almacenar datos no ordenados, con una asignación (llave, valor)
# conjuntos y diccionarios se declaran con {}, listas [], tuplas()

dias = {
    "lun": "Lunes",
    "mar": "Martes",
    "mie": "Miércoles",
    "jue": "Jueves",
    "vie": "Viernes",
    "sab": "Sábado",
    "dom": "Domingo"
}
# entre corchetes accedemos a un elemeto con el identificador o llave
print(dias)
print(dias["mie"])

# con GET, si no existe la llave o identificador, imprime un mensaje que quieras poner
print(dias.get("l", "No es un identificador"))

# con POP, elimína el elemento de la llave o identificador que pongas
print(dias.pop("lun"))
print(dias)

# con POPITEM, elimína el último elemento y lo da, para usarlo como quieras
print( )
print(dias.popitem())
print(dias)

# con UPDATE, modifica un elemento dada la llave y si no existe, lo agrega al diccionario
print( )
dias.update(mar = "jueves")
print(dias)
dias.update(otro = "Otro día")
print(dias)