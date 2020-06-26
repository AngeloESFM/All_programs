# 47 LECTURA DE ARCHIVOS DE TEXTO

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
# Para saber si es un archivo que puedes leer se escribe .readable()
print(archivo_alumnos.readable())
# Para que se muestre el contenido del archivo se escribe .read()
#print(archivo_alumnos.read())
# Para imprimir la primer linea y asi sucesivamente se escribe .readline()
#print(archivo_alumnos.readline())
#print(archivo_alumnos.readline())
# Para acceder al archivo como si fuera una lista se usa .readlines() en plural
#print(archivo_alumnos.readlines())
# sólo puedes recorrer o leer el archivo una vez y desaparecen los datos no en el original
print(archivo_alumnos.readlines()[1])
# Para cerrar el archivo se hace de la siguiente forma, así debe ser la buena practica
archivo_alumnos.close()
# ^ Despues de cerrado el archivo ya no se puede hacer uso de él.