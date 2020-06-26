# 58, 59 JUEGO DE POKEMON
from utilidades_extra import tirar_dado

# Creamos la clase Pokemon
class Pokemon:
    def __init__(self, nombre, ataque):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = 100

    def personaje(self, numero_de_p):
        self.Pikachu = p1
        self.Bulbazur = p2
        self.Squirtle = p3


    def gano(self):
        print(f"{(self.nombre).upper()} GANÓ ESTA BATALLA!!!")

# Creamos nuestros pokemon
P1 = Pokemon("Pikachu", 59)
P2 = Pokemon("Bulbazur", 55)
p3 = Pokemon("Squirtle", 57)
p4 = Pokemon("Charmander", 60)
p5 = Pokemon("Meowth", 50)
p6 = Pokemon("Jigglypuff", 99)

# Inicializamos los valores y el turno

while True:
    P1.vida = 100
    P2.vida = 100

    turno = tirar_dado(2)
    print(f"{P1.nombre} se enfrenta a {P2.nombre}, veremos quien es más fuerte")
    print("HA INICIADO LA BATALLA!!!\n")
    # Inicia la batalla
    while P1.vida > 0 and P2.vida > 0:
        if turno == 1:
            P2.vida = P2.vida - P1.ataque
            turno = 2
            print(f"{P1.nombre} ataca, ahora {P2.nombre} tiene de vida {P2.vida}")
            print("\n----PRÓXIMA RONDA----")
        else:
            P1.vida -= P2.ataque
            turno = 1
            print(f"{P2.nombre} ataca, ahora {P1.nombre} tiene de vida {P1.vida}")
            print("\n----PRÓXIMA RONDA----")

        # consultamos que pokemon perdió
    if P1.vida <= 0:
        P2.gano()
    else:
        P1.gano()

    print("\nQuieres otra batalla? ")
    print("Presiona 1 para seguir con ellas, o presiona 2 para terminarlas")
    opc = input("> ")
    if opc == "1":
        print("¡¡¡CONTINUAN LAS BATALLAS!!!")
    if opc == "2":
        print("OK, Nos vemos pronto para la siguiente batalla.")
        break