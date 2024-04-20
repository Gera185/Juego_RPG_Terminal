from arma import *
from hp_bar import HP_Bar, MP_Bar
from magia import *

class Personaje:

    def __init__(self, name: str, hp: int, mp:int):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.mp = mp
        self.mp_max = mp

        self.arma= Puño_Americano #Arma predeterminada.

    def luchaArma(self, target) -> None:
        target.hp -= self.arma.atq
        target.hp = max(target.hp, 0)
        target.barra_vida.actualizar()
        print(f"{self.name} hizo {self.arma.atq} de daño a {target.name} con {self.arma.name}.")


class Heroe(Personaje):
    def __init__(self, name: str, hp: int, mp: int) -> None:
        super().__init__(name=name, hp=hp, mp=mp)
        self.arma_defecto = self.arma
        self.barra_vida = HP_Bar(self, color="green")
        self.barra_mp = MP_Bar(self)

        self.hechizo1 = bola_fuego
    
    def equipo(self, arma) -> None:
        self.arma = arma
        print(f"{self.name} se equipó un/a {self.arma.name}!")

    def soltar(self) -> None:
        self.arma = self.arma_defecto
        print(f"{self.name} solto el/la {self.arma.name}.")

    def mostrarHechizos(self)->None:
        print(f"|\t[1] {self.hechizo1.nombre}\t\t\t\t|")

    def luchaMagia(self, target, hechizo) -> None:
        target.hp -= hechizo.dmg
        target.hp = max(target.hp, 0)
        self.mp -= hechizo.coste
        self.mp = max(self.mp, 0)
        target.barra_vida.actualizar()
        self.barra_mp.actualizar()
        print(f"{self.name} hizo {hechizo.dmg} de daño a {target.name} con {hechizo.nombre}.")

# Creamos al Heroe y le desequipamos y equipamos otra arma.
heroe = Heroe(name="Heroe", hp=100, mp=50)
heroe.soltar()
heroe.equipo(Espada_de_Hierro)



class Enemigo(Personaje):
    def __init__(self, name: str, hp: int, arma) -> None:
        super().__init__(name=name, hp=hp, mp=0)

        self.arma = arma
        self.barra_vida = HP_Bar(self, color="red")

# Creamos al villano.
villano = Enemigo(name="Villano", hp=100, arma=Puño_Americano)