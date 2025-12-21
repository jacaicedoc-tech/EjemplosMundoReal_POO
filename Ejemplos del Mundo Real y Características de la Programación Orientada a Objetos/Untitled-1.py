# --------------------------------------------
# PROGRAMA: Sistema simple de Tienda
# Paradigma: Programación Orientada a Objetos
# --------------------------------------------

# Clase Producto (ABSTRACCIÓN + ENCAPSULAMIENTO)
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    # Método para mostrar información del producto
    def mostrar_info(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Stock disponible: {self.stock}")

    # Método para vender una cantidad del producto
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Venta realizada: {cantidad} unidades de {self.nombre}")
        else:
            print("No hay suficiente stock disponible")


# Clase Tienda (INTERACCIÓN ENTRE OBJETOS)
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    # Método para agregar productos a la tienda
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Método para mostrar todos los productos
    def mostrar_productos(self):
        print(f"\nProductos disponibles en {self.nombre}:")
        for producto in self.productos:
            producto.mostrar_info()
            print("-" * 30)


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    # Crear productos
    producto1 = Producto("Laptop", 800, 5)
    producto2 = Producto("Mouse", 20, 15)

    # Crear tienda
    tienda = Tienda("Tienda La Ganga")

    # Agregar productos a la tienda
    tienda.agregar_producto(producto1)
    tienda.agregar_producto(producto2)

    # Mostrar productos
    tienda.mostrar_productos()

    # Realizar una venta
    producto1.vender(2)

    # Mostrar productos actualizados
    tienda.mostrar_productos()
