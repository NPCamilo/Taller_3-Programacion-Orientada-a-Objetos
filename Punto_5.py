\"""
Cree una clase Encuesta que almacene respuestas de usuarios (edad, género, ciudad, opinión).
Guarde cada respuesta en un archivo distinto por ciudad. Muestre estadísticas por género.
\"""

class Encuesta:
    def __init__(self, edad, genero, ciudad, opinion):
        self.edad = edad
        self.genero = genero
        self.ciudad = ciudad
        self.opinion = opinion

    def guardar_por_ciudad(self):
        nombre_archivo = f"{self.ciudad.replace(' ', '_')}.txt"
        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{self.edad}|{self.genero}|{self.ciudad}|{self.opinion}\n")

    @staticmethod
    def estadisticas_por_genero(nombre_archivo):
        masculino = 0
        femenino = 0
        otro = 0
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        edad, genero, ciudad, opinion = linea.split("|")
                        genero_lower = genero.lower()
                        if genero_lower == "masculino":
                            masculino += 1
                        elif genero_lower == "femenino":
                            femenino += 1
                        else:
                            otro += 1
        except FileNotFoundError:
            print("El archivo no existe.")
        return {"masculino": masculino, "femenino": femenino, "otro": otro}


if __name__ == "__main__":
    e1 = Encuesta(25, "Masculino", "Bogotá", "Excelente servicio")
    e2 = Encuesta(30, "Femenino", "Bogotá", "Muy bueno")
    e3 = Encuesta(22, "Femenino", "Medellín", "Mejorar tiempos")
    e4 = Encuesta(40, "Masculino", "Bogotá", "Regular")

    e1.guardar_por_ciudad()
    e2.guardar_por_ciudad()
    e3.guardar_por_ciudad()
    e4.guardar_por_ciudad()

    print("Estadísticas Bogotá:", Encuesta.estadisticas_por_genero("Bogotá.txt"))
