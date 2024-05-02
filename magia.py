class Magia:
    def __init__ (self, nombre: str, tipo: str, dmg: int, coste: int) -> None:
        self.nombre = nombre
        self.tipo = tipo
        self.dmg = dmg
        self.coste = coste


bola_fuego=Magia("Bola de Fuego", "Fuego", 40, 25)
carambano=Magia("Carambano    ", "Hielo", 35, 20)