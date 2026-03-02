import random

ANCHO = 20
ALTO = 10


def crear_serpiente():
    return [(5, 5), (4, 5), (3, 5)]


def crear_comida(serpiente):
    while True:
        comida = (random.randint(0, ANCHO - 1),
                  random.randint(0, ALTO - 1))
        if comida not in serpiente:
            return comida


def mover_serpiente(serpiente, direccion, crecer=False):
    x, y = serpiente[0]

    if direccion == "w":
        y -= 1
    elif direccion == "s":
        y += 1
    elif direccion == "a":
        x -= 1
    elif direccion == "d":
        x += 1

    nueva_cabeza = (x, y)
    serpiente.insert(0, nueva_cabeza)

    if not crecer:
        serpiente.pop()

    return serpiente


def colision_pared(cabeza):
    x, y = cabeza
    return x < 0 or x >= ANCHO or y < 0 or y >= ALTO


def colision_cuerpo(serpiente):
    return serpiente[0] in serpiente[1:]


def dibujar_tablero(serpiente, comida):
    for y in range(ALTO):
        for x in range(ANCHO):
            if (x, y) == serpiente[0]:
                print("O", end="")
            elif (x, y) in serpiente:
                print("o", end="")
            elif (x, y) == comida:
                print("X", end="")
            else:
                print(".", end="")
        print()