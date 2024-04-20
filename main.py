from menu import *
from config import *

texto_Menu()
while True:

    opcion=(str(input()).lower())
    if(opcion=="a" or opcion=="e" or opcion=="c") :
        menuCombateArma(opcion)
    elif(opcion=="m"):
        menuMagia()
        numHechizo=(int(input()))
        if(numHechizo==1):
            menuCombateMagia(heroe.hechizo1)

    

