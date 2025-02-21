class Horario:
    total_horarios = 0  # Contador de instancias

    def __init__(self, curso, dia, hora_inicio, hora_fin):
        self.curso = curso
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        Horario.total_horarios += 1  # Aumenta el contador cada vez que se crea un horario
    def mostrar_horarios(self):
        pass
    def modificar_horarios(self,nuevo_horario:dict):
        pass
    def __str__(self):
        pass
    def __repr__(self):
        pass
    def desde_tupla(self,cls,tupla):
        pass
    def es_horario_valido(self):
        pass