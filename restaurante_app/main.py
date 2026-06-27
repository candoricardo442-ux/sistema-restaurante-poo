# Sistema básico de restaurante usando POO

class Producto:
    def __init__(self, nombre, precio, categoria, disponible):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.disponible = disponible

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "Agotado"
        return f"{self.nombre} - ${self.precio} - {self.categoria} - {estado}"


class Cliente:
    def __init__(self, nombre, edad, telefono, cliente_frecuente):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.cliente_frecuente = cliente_frecuente

    def mostrar_informacion(self):
        tipo = "Cliente frecuente" if self.cliente_frecuente else "Cliente nuevo"
        return f"{self.nombre} - {self.edad} años - {self.telefono} - {tipo}"


class Restaurante:
    def __init__(self):
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_datos(self):
        print("\n--- PRODUCTOS ---")
        for producto in self.productos:
            print(producto.mostrar_informacion())

        print("\n--- CLIENTES ---")
        for cliente in self.clientes:
            print(cliente.mostrar_informacion())


# Programa principal

restaurante = Restaurante()

producto1 = Producto("Pizza", 12.50, "Comida", True)
producto2 = Producto("Gaseosa", 2.00, "Bebida", True)

cliente1 = Cliente("Ricardo", 21, "225069511", True)
cliente2 = Cliente("Carlos", 30, "0985212452", False)


restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)

restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)


restaurante.mostrar_datos()