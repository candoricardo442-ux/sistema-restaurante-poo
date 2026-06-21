from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():

    # Crear restaurante
    restaurante = Restaurante("Marisquería El Delfín")

    # Crear productos
    producto1 = Producto("Ceviche de Camarón", "Mariscos", 8.50)
    producto2 = Producto("Arroz Marinero", "Mariscos", 10.00)
    producto3 = Producto("Encocado de Pescado", "Mariscos", 9.50)

    # Crear clientes
    cliente1 = Cliente("Ricardo Cando", "0991234567")
    cliente2 = Cliente("María López", "0987654321")

    # Registrar productos
    restaurante.registrar_producto(producto1)
    restaurante.registrar_producto(producto2)
    restaurante.registrar_producto(producto3)

    # Registrar clientes
    restaurante.registrar_cliente(cliente1)
    restaurante.registrar_cliente(cliente2)

    # Mostrar información
    print("===== SISTEMA DE GESTIÓN DE RESTAURANTE =====")
    print("Nombre del restaurante:", restaurante.nombre)

    restaurante.mostrar_productos()
    restaurante.mostrar_clientes()


if __name__ == "__main__":
    main()