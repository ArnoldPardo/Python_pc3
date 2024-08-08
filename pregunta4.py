class RECTANGULO:
    def __init__(self, largo, ancho):
        # Inicializa los atributos largo y ancho
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        # Calcula el área del rectángulo
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        # Inicializa el cuadrado como un rectángulo con lados iguales
        super().__init__(lado, lado)

# Crear un objeto de tipo RECTANGULO
rectangulo = RECTANGULO(4, 6)  # Largo 4 unidades, ancho 6 unidades

# Crear un objeto de tipo CUADRADO
cuadrado = CUADRADO(5)  # Lado 5 unidades

# Calcular y mostrar el área de los objetos
area_rectangulo = rectangulo.calcular_area()
area_cuadrado = cuadrado.calcular_area()

print(f"El área del rectángulo con largo {rectangulo.largo} y ancho {rectangulo.ancho} es: {area_rectangulo}")
print(f"El área del cuadrado con lado {cuadrado.largo} es: {area_cuadrado}")
