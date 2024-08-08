

import operaciones

def main():
    # Ejemplo de uso de las funciones del módulo operaciones

    # Pruebas de suma
    print("Suma:")
    print(f"5 + 3 = {operaciones.suma(5, 3)}")
    print(f"5 + 'a' = {operaciones.suma(5, 'a')}")  # Debería mostrar un mensaje de error

    # Pruebas de resta
    print("\nResta:")
    print(f"10 - 4 = {operaciones.resta(10, 4)}")
    print(f"10 - 'b' = {operaciones.resta(10, 'b')}")  # Debería mostrar un mensaje de error

    # Pruebas de producto
    print("\nProducto:")
    print(f"7 * 2 = {operaciones.producto(7, 2)}")
    print(f"7 * 'c' = {operaciones.producto(7, 'c')}")  # Debería mostrar un mensaje de error

    # Pruebas de división
    print("\nDivisión:")
    print(f"8 / 2 = {operaciones.division(8, 2)}")
    print(f"8 / 0 = {operaciones.division(8, 0)}")  # Debería mostrar un mensaje de error
    print(f"8 / 'd' = {operaciones.division(8, 'd')}")  # Debería mostrar un mensaje de error

if __name__ == "__main__":
    main()
