import os

os.system("")


class Barra:
    simbolo_entero: str = "█"
    simbolo_perdido: str = "_"
    barrera: str = "|"
    colors: dict = {"red": "\033[91m",
                    "purple": "\33[95m",
                    "blue": "\33[34m",
                    "blue2": "\33[36m",
                    "blue3": "\33[96m",
                    "green": "\033[92m",
                    "green2": "\033[32m",
                    "brown": "\33[33m",
                    "yellow": "\33[93m",
                    "grey": "\33[37m",
                    "default": "\033[0m"
                    }


    def __init__(self, entidad, nombre, longitud: int = 20, tiene_color: bool = True, color: str = "") -> None:
        self.nombre = nombre
        self.entidad = entidad
        self.longitud = longitud
        self.tiene_color = tiene_color
        self.color = self.colors.get(color) or self.colors["default"]

    def pintar(self) -> None:
        barra_restante = round(self.cantidad_actual / self.cantidad_max * self.longitud)
        barra_perdida = self.longitud - barra_restante
        print(f"{self.nombre} del {self.entidad.name}: {self.cantidad_actual}/{self.cantidad_max}")
        print(f"{self.barrera}"
            f"{self.color if self.tiene_color else ''}"
            f"{barra_restante * self.simbolo_entero}"
            f"{barra_perdida * self.simbolo_perdido}"
            f"{self.colors['default'] if self.tiene_color else ''}"
            f"{self.barrera}")


class HP_Bar(Barra):
    def __init__(self, entidad, nombre: str="HP", longitud: int = 20, tiene_color: bool = True, color: str = ""):
        super().__init__(entidad=entidad, nombre=nombre, longitud=longitud, tiene_color=tiene_color, color=color)
        
        self.cantidad_actual = entidad.hp
        self.cantidad_max = entidad.hp_max

    def actualizar(self) -> None:
        self.cantidad_actual = self.entidad.hp

class MP_Bar(Barra):
    def __init__(self, entidad, nombre: str="HP", longitud: int = 20, tiene_color: bool = True, color: str = "blue"):
        super().__init__(entidad=entidad, nombre=nombre, longitud=longitud, tiene_color=tiene_color, color=color)
        
        self.cantidad_actual = entidad.mp
        self.cantidad_max = entidad.mp_max