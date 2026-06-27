# Clase que representa un cliente

class Cliente:

    def __init__(self, nombre: str, edad: int, telefono: str, cliente_frecuente: bool):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.cliente_frecuente = cliente_frecuente

    def __str__(self):
        tipo = "Frecuente" if self.cliente_frecuente else "Nuevo"
        return f"{self.nombre} | {self.edad} años | {self.telefono} | {tipo}"