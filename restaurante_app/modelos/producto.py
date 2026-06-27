# Clase que representa un producto

class Producto:

    def __init__(self, nombre: str, precio: float, categoria: str, disponible: bool):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.nombre} - ${self.precio:.2f} - {self.categoria} - {estado}"