"""
Implemente una clase NotaMusical con atributos como nombre, frecuencia y duración.
Guarde en un archivo las notas mayores a cierta frecuencia. Añada un método que simule la ejecución de la nota (texto).
"""

class NotaMusical:
    def __init__(self, nombre, frecuencia, duracion):
        self.nombre = nombre
        self.frecuencia = frecuencia
        self.duracion = duracion

    @staticmethod
    def guardar_notas_mayores(notas, frecuencia_minima, nombre_archivo="notas_altas.txt"):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for nota in notas:
                if nota.frecuencia > frecuencia_minima:
                    archivo.write(f"{nota.nombre}|{nota.frecuencia}|{nota.duracion}\n")

    def simular_ejecucion(self):
        print(f"Ejecutando nota {self.nombre} ({self.frecuencia} Hz) por {self.duracion} segundos")


if __name__ == "__main__":
    n1 = NotaMusical("Do", 261.63, 1.0)
    n2 = NotaMusical("La", 440.0, 0.5)
    n3 = NotaMusical("Do agudo", 523.25, 1.0)

    notas = [n1, n2, n3]
    NotaMusical.guardar_notas_mayores(notas, 300, "notas_altas.txt")
    n2.simular_ejecucion()
