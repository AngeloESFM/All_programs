# 49 ELIMINAR ARCHIVOS DE TEXTO

# Para abrir el archivo se hace de la siguiente forma

archivo_alumnos = open("estudiantes2.txt", "r")
print(archivo_alumnos)
archivo_alumnos.close()

# Para borrar un archivo se hace de la siguiente forma
# Primero importar una librería
import os
# Llamar la función de esa libreria con el archivo y lo borra
os.remove("estudiantes2.txt")
