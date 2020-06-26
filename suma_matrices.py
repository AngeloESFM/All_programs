# SUMA DE MATRÍCES
# Definimos la matríz

A = [[21, 18, 35, 40],
     [19, 11, 21, 14],
     [12, 15, 20, 30]]

B = [[11, 7, 21, 32],
     [9, 15, 24, 10],
     [23, 8, 12, 22]]


def sumar_matrices(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):

        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(0)

        for i in range(len(m3)):
            for j in range(len(m3[0])):
                m3[i][j] = m1[i][j] + m2[i][j]


# TAMBIEN SE PUEDE DE LA SIGUIENTE FORMA EN VEZ DE AGREGAR UN 0

def sumar_matrices(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j] + m2[i][j])

        return m3
    else:
        return None


c = sumar_matrices(a, b)

if c == None:
    print("No se puede sumar")

else:
    for fila in c:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")