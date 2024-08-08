import math

class CIRCULO:
    def __init__(self, radio):
        # Inicializa el atributo radio
        self.radio = radio

    def calcular_area(self):
        # Calcula el área del círculo usando la fórmula A = π * r^2
        return math.pi * self.radio ** 2

# Crear dos objetos de tipo CIRCULO
circulo1 = CIRCULO(12)  # Radio 12 unidades
circulo2 = CIRCULO(10) # Radio 10 unidades

# Calcular y mostrar el área de los círculos
area_circulo1 = circulo1.calcular_area()
area_circulo2 = circulo2.calcular_area()

print(f"El área del círculo con radio {circulo1.radio} es: {area_circulo1:.2f}")
print(f"El área del círculo con radio {circulo2.radio} es: {area_circulo2:.2f}")
