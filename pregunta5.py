class Alumno:
    def __init__(self, nombre, numero_registro):
        # Inicializa los atributos nombre y numero_registro
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        # Muestra toda la información del estudiante
        edad_info = f"Edad: {self.edad}" if self.edad is not None else "Edad no asignada"
        notas_info = ", ".join(map(str, self.notas)) if self.notas else "No hay notas asignadas"
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        print(edad_info)
        print(f"Notas: {notas_info}")

    def set_age(self, edad):
        # Asigna la edad al estudiante
        self.edad = edad

    def set_nota(self, notas):
        # Asigna las notas al estudiante (notas debe ser una lista de números)
        if isinstance(notas, list) and all(isinstance(nota, (int, float)) for nota in notas):
            self.notas = notas
        else:
            print("Error: Las notas deben ser una lista de números.")

# Crear un objeto de tipo Alumno
alumno1 = Alumno("Juan Pérez", "12345")

# Asignar edad y notas al estudiante
alumno1.set_age(20)
alumno1.set_nota([8.5, 7, 9.5])

# Mostrar la información del estudiante
alumno1.display()
