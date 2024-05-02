from personaje import *
class Pociones():
    def __init__(self, nombre: str, coste: int):
        self.nombre = nombre
        self.coste = coste

class Pociones_HP(Pociones):
    def __init__(self, nombre: str, coste: int, curacion: int):
        super().__init__(nombre=nombre, coste=coste)
        self.curacion=curacion

    def usar(self, target)->None:
        target.hp += self.curacion
        target.hp = max(100, target.hp_max)
        target.barra_vida.actualizar()
        print(f"{target.name} usó {self.nombre} y se curó {self.curacion} HP.")

pocion = Pociones_HP("Poción", 10, 20)

class Pociones_MP(Pociones):
    def __init__(self, nombre: str, coste: int, curacion: int):
        super().__init__(nombre, coste)
        self.curacion = curacion

    def usar(self, target)->None:
        target.mp += self.curacion
        target.mp = max(50, target.mp_max)
        target.barra_mp.actualizar()
        print(f"{target.name} usó {self.nombre} y se curó {self.curacion} MP.")

elixir = Pociones_MP("Elixir", 10, 20)