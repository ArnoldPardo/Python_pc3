# menu_calculos.py

from pregunta3 import CIRCULO
from pregunta4 import RECTANGULO, CUADRADO

def validar_entrada(prompt):
    while True:
        try:
            valor = float(input(prompt))
            if valor <= 0:
                print("Error: El valor debe ser un número positivo.")
            else:
                return valor
        except ValueError:
            print("Error: Ingrese un número válido.")

def menu():
    while True:
        print("\nMenú de Cálculos Geométricos")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        eleccion = input("Seleccione una opción (1-4): ")

        if eleccion == '1':
            radio = validar_entrada("Ingrese el radio del círculo: ")
            circulo = CIRCULO(radio)
            print(f"El área del {circulo} es: {circulo.calcular_area():.2f}")

        elif eleccion == '2':
            largo = validar_entrada("Ingrese el largo del rectángulo: ")
            ancho = validar_entrada("Ingrese el ancho del rectángulo: ")
            rectangulo = RECTANGULO(largo, ancho)
            print(f"El área del {rectangulo} es: {rectangulo.calcular_area():.2f}")

        elif eleccion == '3':
            lado = validar_entrada("Ingrese el lado del cuadrado: ")
            cuadrado = CUADRADO(lado)
            print(f"El área del {cuadrado} es: {cuadrado.calcular_area():.2f}")

        elif eleccion == '4':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    menu()

