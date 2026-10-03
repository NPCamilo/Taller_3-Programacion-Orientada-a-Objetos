\"""
Cree una clase InventarioProducto que gestione un listado de productos (nombre, precio, cantidad).
Agregue métodos para añadir productos, calcular el valor total del inventario y guardar todo en un archivo.
\"""

class InventarioProducto:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        self.productos.append(producto)

    def calcular_valor_total(self):
        valor_total = sum(p["precio"] * p["cantidad"] for p in self.productos)
        return valor_total

    def guardar_en_archivo(self, nombre_archivo="inventario.txt"):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for producto in self.productos:
                archivo.write(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}\n")
            archivo.write(f"\\nValor total del inventario: {self.calcular_valor_total()}\n")


if __name__ == "__main__":
    inventario = InventarioProducto()
    inventario.agregar_producto("Laptop", 2500000, 2)
    inventario.agregar_producto("Mouse", 150000, 5)
    inventario.agregar_producto("Teclado", 300000, 3)

    print(f"Valor total: {inventario.calcular_valor_total()}")
    inventario.guardar_en_archivo()
