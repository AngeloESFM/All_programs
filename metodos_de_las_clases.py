# 55 MÉTODOS DE LAS CLASES

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
#
# Podemos definir más funciones y hacer uso de ellas
    def desactivar (self):
        self.esta_inscrito = False

    def anadir(self, agregar):

        self.cursos = self.cursos + [agregar]


estudiante1 = Estudiante("Angelo", 24, "Python")
print(estudiante1.esta_inscrito)
print(estudiante1.cursos)
# Hacemos uso de la función desactivar y al imprimir cambia de True a False
estudiante1.desactivar()
print(estudiante1.esta_inscrito)
estudiante1.anadir(agregar = input("añade un nuevo curso"))
print(estudiante1.cursos)

# TAREA CREAR DOS MÉTODOS
# 1 QUE PERMITA AÑADIR CURSOS AL ESTUDIANTE
# 2 OTRO QUE PERMITA ELIMINAR CURSOS DEL ESTUDIANTE
