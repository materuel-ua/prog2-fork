class Estudiante:
    total_estudiantes = 0  # Contador de instancias

    def __init__(self, nombre, edad, cursos_inscritos):
        self.nombre = nombre
        self.edad = edad
        self.cursos_inscritos = cursos_inscritos
        Estudiante.total_estudiantes += 1  # Aumenta el contador cada vez que se crea un estudiante
    def inscribir_curso(self,curso):
        self.cursos_inscritos.append(curso)
    def mostrar_información(self):
        print('Información')
    def __str__(self):
        return(f'Nombre: {self.nombre} Edad: {self.edad} Cursos:{self.cursos_inscritos}')
    def __repr__(self):
        return(f"{type(self).__name__}"
              f'(Nombre="{self.nombre}",'
              f'Edad="{self.edad}",'
              f'Cursos="{self.cursos_inscritos}",')
    @classmethod
    def desde_tuplas(cls,tupla):
        return cls(*tupla)
    @staticmethod
    def es_mayor_de_edad(nombre):
        if nombre.edad>17:
            print('Es mayor de edad')
        else:
            print('No es mayor de edad')