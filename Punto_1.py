\"""
Cree una clase llamada Libro con atributos como título, autor, año, editorial y género. 
Incluya métodos para mostrar la información del libro, guardar los datos en un archivo y buscar libros por autor.
\"""

class Libro:
    def __init__(self, titulo, autor, anio, editorial, genero):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.editorial = editorial
        self.genero = genero

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio}")
        print(f"Editorial: {self.editorial}")
        print(f"Género: {self.genero}")

    def guardar_en_archivo(self, nombre_archivo="libros.txt"):
        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{self.titulo}|{self.autor}|{self.anio}|{self.editorial}|{self.genero}\n")

    @staticmethod
    def buscar_por_autor(nombre_archivo, autor_buscar):
        resultados = []
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        titulo, autor, anio, editorial, genero = linea.split("|")
                        if autor.lower() == autor_buscar.lower():
                            resultados.append((titulo, autor, anio, editorial, genero))
        except FileNotFoundError:
            print("El archivo no existe.")
        return resultados


if __name__ == "__main__":
    libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 1943, "Reynal & Hitchcock", "Fábula")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Editorial Sudamericana", "Realismo mágico")

    libro1.mostrar_informacion()
    print("-" * 30)
    libro2.mostrar_informacion()

    libro1.guardar_en_archivo("libros.txt")
    libro2.guardar_en_archivo("libros.txt")

    print("\nBuscando libros de Gabriel García Márquez:")
    res = Libro.buscar_por_autor("libros.txt", "Gabriel García Márquez")
    for r in res:
        print(r)
