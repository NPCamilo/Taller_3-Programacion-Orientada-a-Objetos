"""
Diseñe una clase AgendaContactos con atributos como nombre, teléfono, correo y dirección.
Agregue métodos para buscar contactos, eliminar contactos y actualizar información desde y hacia un archivo.
"""

import os

class AgendaContactos:
    def __init__(self, nombre, telefono, correo, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    @staticmethod
    def guardar_contactos(contactos, nombre_archivo="agenda.txt"):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for contacto in contactos:
                archivo.write(f"{contacto.nombre}|{contacto.telefono}|{contacto.correo}|{contacto.direccion}\n")

    @staticmethod
    def leer_contactos(nombre_archivo="agenda.txt"):
        contactos = []
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nombre, telefono, correo, direccion = linea.split("|")
                        contactos.append(AgendaContactos(nombre, telefono, correo, direccion))
        except FileNotFoundError:
            print("El archivo no existe.")
        return contactos

    @staticmethod
    def buscar_contactos(contactos, criterio):
        resultados = []
        criterio_lower = criterio.lower()
        for contacto in contactos:
            if (criterio_lower in contacto.nombre.lower() or
                criterio_lower in contacto.telefono or
                criterio_lower in contacto.correo.lower()):
                resultados.append(contacto)
        return resultados

    @staticmethod
    def eliminar_contacto(contactos, nombre):
        for contacto in contactos:
            if contacto.nombre.lower() == nombre.lower():
                contactos.remove(contacto)
                return True
        return False

    @staticmethod
    def actualizar_contacto(contactos, nombre, nuevo_telefono=None, nuevo_correo=None, nueva_direccion=None):
        for contacto in contactos:
            if contacto.nombre.lower() == nombre.lower():
                if nuevo_telefono is not None:
                    contacto.telefono = nuevo_telefono
                if nuevo_correo is not None:
                    contacto.correo = nuevo_correo
                if nueva_direccion is not None:
                    contacto.direccion = nueva_direccion
                return True
        return False


if __name__ == "__main__":
    c1 = AgendaContactos("Juan Pérez", "1234567", "juan@mail.com", "Calle 123")
    c2 = AgendaContactos("María López", "7654321", "maria@mail.com", "Carrera 45")
    contactos = [c1, c2]
    AgendaContactos.guardar_contactos(contactos)
    cargados = AgendaContactos.leer_contactos()
    print("Contactos cargados:", len(cargados))
