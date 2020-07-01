# 24, 25, 26 PROGRAMACIÓN ORIENTADA A OBJETOS
"""
Se verá la teoria de lo que es POO
*Ventaja 
    es reutilizable, herencia
    todo puede ser visto como objeto
*Terminología
    Clase
        caracteristicas comúnes de un grupo de objetos
    Instancia u Objeto
        Ejemplar perteneciente a una clase
    Modularización 
        Permite reutilizar trozos de código de un programa a otro
        si hay un fallo, se puede quitar ese fallo y lo demás funciona normal
        encapsular, cada clase no interviene en otra, pero si se conectan con métodos de accesos

*el objeto tiene
propiedades- que caracteristicas tiene el objeto
comportamiento o método - qué puede hacer el objeto?
estado - cómo se encuentra el objeto


"""
# Creamos una clase
#CLASS nombre_de_la_clase(parametros):

class Coche():

    # Creamos las propiedades comúnes de la clase
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

# Definimos un método de la clase en este ejemplo la acción de arrancar
    def arrancar(self):
        # con esta instrucción cambiamos el estado del coche
        self.enmarcha = True

# Definimos otro método que nos diga si el coche está en marcha o no
    def estado(self):
        if self.enmarcha:
            return "El coche está en marcha"
        else:
            return "El coche está parado"

# Se crea el primer objeto de la clase Coche()
c1 = Coche() # A esto se le llama tambien instanciar una clase

# Para acceder a propiedades o método de la clase se usa el punto
# nombre_del_objeto.propiedad/metodo
print("El largo del coche es: ", c1.largoChasis)
print("El coche tiene, ", c1.ruedas, " ruedas")

# Para llamar los métodos se hace nombre_del_objeto.nombre_del_metodo()
c1.arrancar()

print(c1.estado())