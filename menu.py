from personaje import *
from config import *

def menuCombateArma(opcion: str) -> None:

    limpiar()

    heroe.luchaArma(villano)
    villano.luchaArma(heroe)

    heroe.barra_vida.pintar()
    heroe.barra_mp.pintar()
    espacio()
    villano.barra_vida.pintar()
    
    texto_Menu()


def menuCombateMagia(hechizo) -> None:
    limpiar()

    heroe.luchaMagia(villano, hechizo)
    villano.luchaArma(heroe)

    heroe.barra_vida.pintar()
    heroe.barra_mp.pintar()
    espacio()
    villano.barra_vida.pintar()
    
    texto_Menu()




def menuMagia() -> None:
    print(BARRA)
    heroe.mostrarHechizos()
    print(BARRA)