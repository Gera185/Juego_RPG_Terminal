import os

BARRA="+=======================================================+"


def espacio()->None:
    print()


def texto_Menu()->None:
    print(BARRA)
    print("|\t[A] Ataque\t[E] Equipo\t\t\t|")
    print("|\t[M] Mágia\t[C] Correr\t\t\t|")
    print(BARRA)

def limpiar()->None:
    os.system("cls")
