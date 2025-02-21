class Profesor:
    total_profesores = 0  # Contador de instancias

    def __init__(self, nombre, especialidad, cursos_asignados):
        self.nombre = nombre
        self.especialidad = especialidad
        self.cursos_asignados = cursos_asignados
        Profesor.total_profesores += 1  # Aumenta el contador cada vez que se crea un profesor

    def asignar_curso(self, curso: str):
        self.cursos_asignados.append(curso)

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print (f"Especialidad: {self.especialidad}")
        print(f"Cursos asignados: {self.cursos_asignados}")

    def __str__(self):
        return f"Profesor {self.nombre}, Especialidad: {self.especialidad}, Cursos asignados: {self.cursos_asignados}"

    def __repr__(self):
        return f"Profesor({self.nombre}, {self.especialidad}, {self.cursos_asignados})"

    @classmethod
    def desde_tupla(cls, tupla):
        return cls(tupla)

    @staticmethod
    def esta_disponible_para_nuevo_curso():
        return True