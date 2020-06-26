# 54 CLASES Y OBJETOS

# Definimos una clase de la siguiente forma
# Si la clase tiene más de un nombre se usa CamelCase como a continuación
#class EstudiantesActivosAhora:

# Esta clase ya puede ser mandada a llamar en otro archivo como si fuera un módulo
class Estudiante:
    def __init__(self, nombre, edad, curso_inicial):         # <<< Aquí se ponen los atributos
        self.nombre = nombre
        self.edad = edad
        self.curso_inicial = curso_inicial
        self.esta_inscrito = True                          # puede ir un "si" o lo que se quiera
        self.cursos = [curso_inicial, "SQL"]

# el nombre que se le asigna al dato para acceder a él, es el que está después de .SELF
# Le asignamos los datos a un objeto para ser parte de la clase, no puede faltar ninguno
estudiante1 = Estudiante("Angelo", 24, "Python")

# De esta forma se accede a cada parte o dato, de la clase hecha
print(estudiante1.nombre)
print(estudiante1.edad)
print(estudiante1.cursos)
print(estudiante1.esta_inscrito)