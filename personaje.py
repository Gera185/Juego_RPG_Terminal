from arma import Puño_Americano
from hp_bar import BarraVida

class Personaje:

    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp
        self.hp_max = hp

        self.arma= Puño_Americano #Arma predeterminada.

    def lucha(self, target) -> None:
        target.hp -= self.arma.atq
        target.hp = max(target.hp, 0)
        target.barra_vida.actualizar()
        print(f"{self.name} hizo {self.arma.atq} de daño a {target.name} con {self.arma.name}.")


class Heroe(Personaje):
    def __init__(self, name: str, hp: int) -> None:
        super().__init__(name=name, hp=hp)

        self.arma_defecto = self.arma
        self.barra_vida = BarraVida(self, color="green")

    
    def equipo(self, arma) -> None:
        self.arma = arma
        print(f"{self.name} equipped a(n) {self.arma.name}!")

    def soltar(self) -> None:
        self.arma = self.arma_defecto
        print(f"{self.name} solto el/la {self.arma.name}.")
        

class Enemigo(Personaje):
    def __init__(self, name: str, hp: int, arma) -> None:
        super().__init__(name=name, hp=hp)

        self.arma = arma
        self.barra_vida = BarraVida(self, color="red")
