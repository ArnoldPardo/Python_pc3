def obtener_calificaciones():
    while True:
        try:
            entrada = input("Introduce una lista de calificaciones separadas por comas: ")
            # Divide la cadena en partes usando la coma como delimitador
            partes = entrada.split(',')
            # Convierte cada parte en un entero
            calificaciones = [int(calificacion.strip()) for calificacion in partes]
            # Muestra la lista de calificaciones
            print("Calificaciones:", calificaciones)
            break
        except ValueError:
            print("Error: Asegúrate de introducir solo números enteros separados por comas.")
        except Exception as e:
            print(f"Se ha producido un error inesperado: {e}")

# Llamar a la función
obtener_calificaciones()
