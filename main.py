from menu import *
from config import *

texto_Menu()
while True:

    opcion=(str(input("> ")).lower())
    if(opcion=="a" or opcion=="c") :
        menuCombateArma(opcion)
    elif(opcion=="m"):
        menuMagia()
        numHechizo=int(input("> "))
        menuCombateMagia(heroe.hechizos[numHechizo-1])
    elif(opcion=="e"):
        menuEquipo()
        numObjeto=int(input("> "))
        menuEquipoUsado(numObjeto)
    

