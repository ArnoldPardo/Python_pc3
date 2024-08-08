# biblioteca/main.py

from gestion import GestionBiblioteca
from libro import Libro

def validar_entrada(prompt):
    while True:
        valor = input(prompt).strip()
        if valor:
            return valor
        else:
            print("Error: La entrada no puede estar vacía.")

def menu():
    biblioteca = GestionBiblioteca()
    
    while True:
        print("\nMenú de Gestión de Biblioteca")
        print("1. Agregar un libro")
        print("2. Listar todos los libros")
        print("3. Buscar libro por título")
        print("4. Buscar libro por autor")
        print("5. Salir")
        
        eleccion = input("Seleccione una opción (1-5): ")

        if eleccion == '1':
            titulo = validar_entrada("Ingrese el título del libro: ")
            autor = validar_entrada("Ingrese el autor del libro: ")
            isbn = validar_entrada("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            biblioteca.agregar_libro(libro)
            print("Libro agregado con éxito.")
        
        elif eleccion == '2':
            print("Listado de libros:")
            biblioteca.listar_libros()
        
        elif eleccion == '3':
            titulo = validar_entrada("Ingrese el título del libro a buscar: ")
            biblioteca.buscar_por_titulo(titulo)
        
        elif eleccion == '4':
            autor = validar_entrada("Ingrese el autor del libro a buscar: ")
            biblioteca.buscar_por_autor(autor)
        
        elif eleccion == '5':
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    menu()
