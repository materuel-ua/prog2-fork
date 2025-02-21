class Estudiante:
    total_estudiantes = 0  # Contador de instancias

    def __init__(self, nombre, edad, cursos_inscritos):
        self.nombre = nombre
        self.edad = edad
        self.cursos_inscritos = cursos_inscritos
        Estudiante.total_estudiantes += 1  # Aumenta el contador cada vez que se crea un estudiante
        
    def inscribir_curso(self,curso):
        self.cursos_inscritos.append(curso)

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')
        print(f'Cursos: {self.cursos_inscritos}')

    def __str__(self):
        print(f'El alumno {self.nombre} tiene {self.edad} años y estudia {self.cursos_inscritos}')

    def __repr__(self):
        print(f'Nombre: ({self.nombre}), Edad:({self.edad}), Cursos:({self.cursos_inscritos})')

    @classmethod
    def desde_tupla(cls,tupla):
        return cls(tupla[0], tupla[1], tupla[2])
    @staticmethod
    def mayor_edad(edad):
        