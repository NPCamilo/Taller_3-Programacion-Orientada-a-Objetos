"""
Desarrolle una clase SistemaNotas para manejar múltiples estudiantes y sus calificaciones.
Implemente métodos para calcular promedios por materia y guardar los mejores estudiantes en un archivo.
"""

class Estudiante:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.notas = {}  # materia: lista de notas

    def agregar_nota(self, materia, nota):
        if materia not in self.notas:
            self.notas[materia] = []
        self.notas[materia].append(nota)

    def promedio_materia(self, materia):
        if materia not in self.notas or len(self.notas[materia]) == 0:
            return 0
        return sum(self.notas[materia]) / len(self.notas[materia])

    def promedio_general(self):
        todas_notas = []
        for notas_list in self.notas.values():
            todas_notas.extend(notas_list)
        if not todas_notas:
            return 0
        return sum(todas_notas) / len(todas_notas)


class SistemaNotas:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def calcular_promedios_por_materia(self, materia):
        resultados = []
        for est in self.estudiantes:
            prom = est.promedio_materia(materia)
            resultados.append((est.nombre, prom))
        return resultados

    def guardar_mejores_estudiantes(self, nombre_archivo="mejores_estudiantes.txt", limite=3):
        mejores = sorted(self.estudiantes, key=lambda e: e.promedio_general(), reverse=True)[:limite]
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("MEJORES ESTUDIANTES (PROMEDIO GENERAL)\n")
            archivo.write("=" * 45 + "\n")
            for est in mejores:
                archivo.write(f"Nombre: {est.nombre} | Código: {est.codigo} | Promedio: {est.promedio_general():.2f}\n")


if __name__ == "__main__":
    sistema = SistemaNotas()
    e1 = Estudiante("Laura Martínez", "001")
    e1.agregar_nota("Matemáticas", 4.5)
    e1.agregar_nota("Matemáticas", 4.8)
    e1.agregar_nota("Física", 4.0)

    e2 = Estudiante("Andrés López", "002")
    e2.agregar_nota("Matemáticas", 3.5)
    e2.agregar_nota("Física", 3.8)

    e3 = Estudiante("Sofía García", "003")
    e3.agregar_nota("Matemáticas", 5.0)
    e3.agregar_nota("Física", 4.9)

    sistema.agregar_estudiante(e1)
    sistema.agregar_estudiante(e2)
    sistema.agregar_estudiante(e3)

    print("Promedios Matemáticas:", sistema.calcular_promedios_por_materia("Matemáticas"))
    sistema.guardar_mejores_estudiantes()
