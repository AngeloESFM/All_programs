# 48 ESCRIBIR EN ARCHIVOS DE TEXTO

# Para crear y escribir en un archivo se pone una "w" de write
archivo_alumnos = open("estudiantes2.txt", "w")
# Para saber si es un archivo escribible
print(archivo_alumnos.writable())
# Para escribir en el archivo se hace de la siguiente forma
# Aunque cada modificación crea un archivo nuevo
print(archivo_alumnos.write("Es un texto nuevo que se crea cada vez\nY puedo dar saltos de linea"))
# Para agregar texto al que ya está en el archivo se usa la "a" de append
# Se agrega al final del texto original y hay que usar saltos de linea para evitar romper el programa
archivo_alumnos = open("estudiantes2.txt", "a")
print(archivo_alumnos.write("\nCaroline Masutti - ReactJS"))
# Cuando se usa r+ se puede leer y escribir pero sobre escribe en la primer parte del archivo
archivo_alumnos = open("estudiantes2.txt", "r+")
print(archivo_alumnos.write("Caroline Masutti2 - ReactJS"))
# Para cerrar el archivo se hace de la siguiente forma, así debe ser la buena practica
archivo_alumnos.close()
# ^ Despues de cerrado el archivo ya no se puede hacer uso de él.