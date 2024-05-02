from personaje import *
from config import *

def menuEquipo() -> None:
    print(BARRA)
    heroe.mostrarEquipo()
    print(BARRA)

def menuEquipoUsado(numObjeto) -> None:
    limpiar()
    heroe.mochila[numObjeto-1].usar(heroe)
    heroe.mochila.pop(numObjeto-1)
    villano.luchaArma(heroe)

    heroe.barra_vida.pintar()
    heroe.barra_mp.pintar()
    espacio()
    villano.barra_vida.pintar()
    
    texto_Menu()

def menuCombateArma(opcion: str) -> None:
    limpiar()

    heroe.luchaArma(villano)
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

def menuCombateMagia(hechizo) -> None:
    limpiar()

    heroe.luchaMagia(villano, hechizo)
    villano.luchaArma(heroe)

    heroe.barra_vida.pintar()
    heroe.barra_mp.pintar()
    espacio()
    villano.barra_vida.pintar()
    
    texto_Menu()