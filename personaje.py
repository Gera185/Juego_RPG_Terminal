from arma import Puño_Americano
from hp_bar import HP_Bar, MP_Bar

class Personaje:

    def __init__(self, name: str, hp: int, mp:int):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.mp = mp
        self.mp_max = mp

        self.arma= Puño_Americano #Arma predeterminada.

    def lucha(self, target) -> None:
        target.hp -= self.arma.atq
        target.hp = max(target.hp, 0)
        target.barra_vida.actualizar()
        print(f"{self.name} hizo {self.arma.atq} de daño a {target.name} con {self.arma.name}.")


class Heroe(Personaje):
    def __init__(self, name: str, hp: int, mp: int) -> None:
        super().__init__(name=name, hp=hp, mp=mp)
        print("Hola")
        self.arma_defecto = self.arma
        self.barra_vida = HP_Bar(self, color="green")
        self.barra_mp = MP_Bar(self)

    
    def equipo(self, arma) -> None:
        self.arma = arma
        print(f"{self.name} equipped a(n) {self.arma.name}!")

    def soltar(self) -> None:
        self.arma = self.arma_defecto
        print(f"{self.name} solto el/la {self.arma.name}.")
        

class Enemigo(Personaje):
    def __init__(self, name: str, hp: int, arma) -> None:
        super().__init__(name=name, hp=hp, mp=0)

        self.arma = arma
        self.barra_vida = HP_Bar(self, color="red")
