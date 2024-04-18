import os
from personaje import Heroe, Enemigo
from arma import *

# Creamos al Heroe y le desequipamos y equipamos otra arma.

heroe = Heroe(name="Heroe", hp=100)
heroe.soltar()
heroe.equipo(Espada_de_Hierro)

# Creamos al villano.
villano = Enemigo(name="Villano", hp=100, arma=Puño_Americano)

while True:
    os.system("cls")

    heroe.lucha(villano)
    villano.lucha(heroe)

    heroe.barra_vida.pintar()
    villano.barra_vida.pintar()
    input()


