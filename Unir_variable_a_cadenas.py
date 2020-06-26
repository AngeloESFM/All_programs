# UNIR VARIABLES A CADENAS
# Sirve para concatenar variables y cadenas, transformar los números en letras

alumnos = 3600
academia = "Academia Angelo"
cadena = "Los " + str(alumnos) + " alumnos de la " + academia + " son muy listos"
print (cadena)

# El más práctico es poner f al principio de la cadena para que detecte los formatos de las variables entre corchetes
cadena = f"Los {alumnos} alumnos de la {academia} son muy listos"
print (cadena)

# .FORMAT = tambien convierte automaticamente tod o en cadena, tomando las variables que sean sustituyendolas por {}
# .FORMAT(variable1, variable2, ... )
cadena = "Los {} alumnos de la {} son muy listos".format(alumnos,academia)
print (cadena)

# Tambien puedes renombrar los corchetes, para que no importe el orden de los parámetros
cadena = "Los {a} alumnos de la {b} son muy listos".format(b=academia, a=alumnos)
print (cadena)
 ###P
