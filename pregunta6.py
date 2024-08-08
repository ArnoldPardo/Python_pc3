class Producto:
    def __init__(self, nombre, año, precio):
        self.nombre = nombre
        self.año = año
        self.precio = precio

    def __str__(self):
        return f"Nombre: {self.nombre}, Año: {self.año}, Precio: ${self.precio:.2f}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if isinstance(producto, Producto):
            self.productos.append(producto)
        else:
            print("Error: El objeto agregado no es una instancia de Producto.")

    def mostrar_productos(self):
        if not self.productos:
            print("El catálogo está vacío.")
        else:
            for producto in self.productos:
                print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if productos_filtrados:
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No se encontraron productos del año {año}.")

    def filtrar_por_precio(self, precio_min, precio_max):
        productos_filtrados = [producto for producto in self.productos if precio_min <= producto.precio <= precio_max]
        if productos_filtrados:
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No se encontraron productos en el rango de ${precio_min} a ${precio_max}.")

# Crear el catálogo
catalogo = Catalogo()

# Crear productos
producto1 = Producto("Filtro de aceite", 2022, 29.99)
producto2 = Producto("Batería de coche", 2021, 89.99)
producto3 = Producto("Pastillas de freno", 2023, 49.99)

# Agregar productos al catálogo
catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

# Mostrar todos los productos
print("Todos los productos en el catálogo:")
catalogo.mostrar_productos()

# Filtrar productos por año
print("\nProductos del año 2023:")
catalogo.filtrar_por_año(2023)

# Filtrar productos por precio
print("\nProductos en el rango de $30 a $50:")
catalogo.filtrar_por_precio(30, 50)
