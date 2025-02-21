class Curso:
    total_cursos = 0  # Contador de instancias

    def __init__(self, nombre, codigo, descripcion):
        self.nombre = nombre
        self.codigo = codigo
        self.descripcion = descripcion
        Curso.total_cursos += 1  # Aumenta el contador cada vez que se crea un curso

    def mostrar_detalles(self):
        print(f'Nombre:{self.nombre}')
        print(f'Codigo: {self.codigo}')
        print(f'Descricion: {self.descripcion}')

    def actualizar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def __str__(self):
        return f"{self.nombre}, {self.codigo}, \
        {self.descripcion})"

    def __repr__(self):
        return(
            f" {type(self).__name__}"
            f"nombre={self.nombre}"
            f"codigo={self.codigo}"
            f"descripcion={self.descripcion}"
            f"total_cursos={Curso.total_cursos}"

        )

    @classmethod
    def desde_tupla(cls,tupla):
        return cls(*tupla)
    @staticmethod
    def es_curso_abierto():
        print('Hola que tal')