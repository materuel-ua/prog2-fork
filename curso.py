class Curso:
    total_cursos = 0  # Contador de instancias

    def __init__(self, nombre, codigo, descripcion):
        self.nombre = nombre
        self.codigo = codigo
        self.descripcion = descripcion
        Curso.total_cursos += 1  # Aumenta el contador cada vez que se crea un curso

    def mostrar_detalles(self,nombre,codigo,descripcion):
        print(self.nombre)
        print(self.codigo)
        print(self.descripcion)

    def actualizar_descripción(self,nueva_descripcion):
        nueva_descripcion=self.descripcion

    def __str__(self):