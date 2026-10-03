\"""
Diseñe una clase Vehículo que guarde marca, modelo, año, tipo y placa. 
Incluya un método para guardar en archivo solo los vehículos del año actual y otro para leerlos.
\"""

import datetime

class Vehiculo:
    def __init__(self, marca, modelo, anio, tipo, placa):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.tipo = tipo
        self.placa = placa

    def guardar_vehiculos_anio_actual(self, vehiculos, nombre_archivo="vehiculos_actuales.txt"):
        anio_actual = datetime.datetime.now().year
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for vehiculo in vehiculos:
                if vehiculo.anio == anio_actual:
                    archivo.write(f"{vehiculo.marca}|{vehiculo.modelo}|{vehiculo.anio}|{vehiculo.tipo}|{vehiculo.placa}\n")

    @staticmethod
    def leer_vehiculos(nombre_archivo="vehiculos_actuales.txt"):
        vehiculos = []
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        marca, modelo, anio, tipo, placa = linea.split("|")
                        vehiculos.append((marca, modelo, int(anio), tipo, placa))
        except FileNotFoundError:
            print("El archivo no existe.")
        return vehiculos


if __name__ == "__main__":
    v1 = Vehiculo("Toyota", "Corolla", 2026, "Automóvil", "ABC123")
    v2 = Vehiculo("Honda", "CBR", 2025, "Motocicleta", "XYZ789")
    v3 = Vehiculo("Chevrolet", "Onix", 2026, "Automóvil", "DEF456")

    vehiculos = [v1, v2, v3]
    Vehiculo.guardar_vehiculos_anio_actual(v1, "vehiculos_actuales.txt") if False else None
    # Guardar correctamente
    v1.guardar_vehiculos_anio_actual(vehiculos)

    print("Vehículos del año actual guardados.")
    print("Lectura:", Vehiculo.leer_vehiculos())
