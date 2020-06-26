# 46 APRENDER A ABRIR Y CERRAR ARCHIVOS DE TEXTO

# Para abrir el archivo se hace de la siguiente forma
"""
# Para abrirlo sólo en lectura se pone una "r"
open("Alumnos.txt","r")
# Para abrirlo sólo en escritura se pone una "w"
open("Alumnos.txt","w")
# Para abrirlo sólo en escritura se pone una "a"
open("Alumnos.txt","a")
# Para abrirlo en escritura y lectura se pone una "r+"
open("Alumnos.txt","r+")
"""
# Para abrirlo sólo en lectura se pone una "r"
archivo_alumnos = open("estu.txt", "r")
# Para saber si es un archivo de lectura
print(archivo_alumnos)
# Para cerrar el archivo se hace de la siguiente forma, así debe ser la buena practica
archivo_alumnos.close()
# ^ Despues de cerrado el archivo ya no se puede hacer uso de él.