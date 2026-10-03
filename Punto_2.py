\"""
Diseñe una clase Estudiante con atributos como nombre, código, carrera, edad y promedio. 
Implemente métodos para calcular si el estudiante aprueba (promedio >= 3.0), y guardar los datos en un archivo.
\"""

class Estudiante:
    def __init__(self, nombre, codigo, carrera, edad, promedio):
        self.nombre = nombre
        self.codigo = codigo
        self.carrera = carrera
        self.edad = edad
        self.promedio = promedio

    def aprueba(self):
        if self.promedio >= 3.0:
            return True
        else:
            return False

    def guardar_en_archivo(self, nombre_archivo="estudiantes.txt"):
        estado = "Aprobado" if self.aprueba() else "Reprobado"
        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{self.nombre}|{self.codigo}|{self.carrera}|{self.edad}|{self.promedio}|{estado}\n")


if __name__ == "__main__":
    estudiante1 = Estudiante("Ana Torres", "12345", "Ingeniería de Sistemas", 20, 4.2)
    estudiante2 = Estudiante("Luis Pérez", "67890", "Ingeniería de Sistemas", 22, 2.5)

    print(f"{estudiante1.nombre}: Aprobado = {estudiante1.aprueba()}")
    print(f"{estudiante2.nombre}: Aprobado = {estudiante2.aprueba()}")

    estudiante1.guardar_en_archivo()
    estudiante2.guardar_en_archivo()
