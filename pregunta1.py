def obtener_fraccion():
    while True:
        try:
            entrada = input("Introduce una fracción en el formato X/Y: ")
            x, y = map(int, entrada.split('/'))
            
            # Validación de Y != 0 y X <= Y
            if y == 0:
                print("El denominador (Y) no puede ser cero. Inténtalo de nuevo.")
                continue
            if x > y:
                print("El numerador (X) no puede ser mayor que el denominador (Y). Inténtalo de nuevo.")
                continue
            
            porcentaje = (x / y) * 100
            
            if porcentaje < 1:
                print("E")
            elif porcentaje > 99:
                print("F")
            else:
                print(f"{round(porcentaje)}%")
            
            break
            
        except ValueError:
            print("Error en el formato. Asegúrate de ingresar dos números enteros separados por '/'.")
        except ZeroDivisionError:
            print("El denominador (Y) no puede ser cero. Inténtalo de nuevo.")
        except Exception as e:
            print(f"Se ha producido un error inesperado: {e}")

# Llamar a la función
obtener_fraccion()
