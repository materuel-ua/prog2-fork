class Curso:
    total_cursos = 0  # Contador de instancias

    def __init__(self, nombre, codigo, descripcion):
        self.nombre = nombre
        self.codigo = codigo
        self.descripcion = descripcion
        Curso.total_cursos += 1  # Aumenta el contador cada vez que se crea un curso

    def mostrar_detalles(self):
        pass
    def actualizar_descripcion(self):
        pass
    def __repr__(self):
        pass
    def desde_tuplas(cls,tupla):
        pass
    def es_curso_abierto(self):
        pass
    def __str__(self):
        pass
