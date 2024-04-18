import os

os.system("")


class BarraVida:
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


    def __init__(self,
                 entidad,
                 longitud: int = 20,
                 tiene_color: bool = True,
                 color: str = "") -> None:
        self.entidad = entidad
        self.longitud = longitud
        self.vida_actual = entidad.hp
        self.vida_max = entidad.hp_max
        self.tiene_color = tiene_color
        self.color = self.colors.get(color) or self.colors["default"]

    def actualizar(self) -> None:
        self.vida_actual = self.entidad.hp

    def pintar(self) -> None:
        barra_restante = round(self.vida_actual / self.vida_max * self.longitud)
        barra_perdida = self.longitud - barra_restante
        print(f"HP del {self.entidad.name}: {self.entidad.hp}/{self.entidad.hp_max}")
        print(f"{self.barrera}"
              f"{self.color if self.tiene_color else ''}"
              f"{barra_restante * self.simbolo_entero}"
              f"{barra_perdida * self.simbolo_perdido}"
              f"{self.colors['default'] if self.tiene_color else ''}"
              f"{self.barrera}")
