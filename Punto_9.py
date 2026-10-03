"""
Diseñe una clase Empresa que maneje empleados, sus salarios, bonificaciones y descuentos.
Incluya métodos para generar reportes en archivos separados por departamentos.
"""

class Empleado:
    def __init__(self, nombre, departamento, salario, bonificacion=0, descuento=0):
        self.nombre = nombre
        self.departamento = departamento
        self.salario = salario
        self.bonificacion = bonificacion
        self.descuento = descuento

    def salario_neto(self):
        return self.salario + self.bonificacion - self.descuento


class Empresa:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def generar_reporte_por_departamento(self):
        departamentos = {}
        for emp in self.empleados:
            if emp.departamento not in departamentos:
                departamentos[emp.departamento] = []
            departamentos[emp.departamento].append(emp)

        for dept, emps in departamentos.items():
            nombre_archivo = f"reporte_{dept.replace(' ', '_')}.txt"
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                archivo.write(f"REPORTE DEL DEPARTAMENTO: {dept}\n")
                archivo.write("=" * 40 + "\n")
                for emp in emps:
                    archivo.write(f"Nombre: {emp.nombre}\n")
                    archivo.write(f"Salario base: {emp.salario}\n")
                    archivo.write(f"Bonificación: {emp.bonificacion}\n")
                    archivo.write(f"Descuento: {emp.descuento}\n")
                    archivo.write(f"Salario neto: {emp.salario_neto()}\n")
                    archivo.write("-" * 40 + "\n")


if __name__ == "__main__":
    empresa = Empresa()
    empresa.agregar_empleado(Empleado("Carlos Ruiz", "IT", 3000000, 300000, 100000))
    empresa.agregar_empleado(Empleado("Ana Gómez", "IT", 2800000, 200000, 80000))
    empresa.agregar_empleado(Empleado("Pedro Torres", "RRHH", 2500000, 150000, 50000))
    empresa.generar_reporte_por_departamento()
