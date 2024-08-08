# operaciones.py

def suma(a, b):
    try:
        # Verifica que ambos argumentos sean números (int o float)
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Error: Tipo de dato no válido.")
        return a + b
    except TypeError as e:
        print(e)

def resta(a, b):
    try:
        # Verifica que ambos argumentos sean números (int o float)
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Error: Tipo de dato no válido.")
        return a - b
    except TypeError as e:
        print(e)

def producto(a, b):
    try:
        # Verifica que ambos argumentos sean números (int o float)
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Error: Tipo de dato no válido.")
        return a * b
    except TypeError as e:
        print(e)

def division(a, b):
    try:
        # Verifica que ambos argumentos sean números (int o float)
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Error: Tipo de dato no válido.")
        # Verifica que el divisor no sea cero
        if b == 0:
            raise ZeroDivisionError("Error: No es posible dividir entre cero.")
        return a / b
    except TypeError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
