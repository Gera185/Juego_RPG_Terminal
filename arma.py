class Arma:
    def __init__(self, name: str, tipo: str, atq: int, valor: int) -> None:
        self.name = name
        self.tipo = tipo
        self.atq = atq
        self.valor = valor
    

Espada_de_Hierro = Arma(name="Espada de hierro",
                        tipo="Afilado",
                        atq=30,
                        valor=10)

Arco_Corto = Arma(name="Arco corto",
                        tipo="Larga distancia",
                        atq=30,
                        valor=10)

Puño_Americano = Arma(name="Puño americano",
                    tipo="Contundente",
                    atq=25,
                    valor=10)