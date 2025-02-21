class Horario:
    total_horarios = 0  # Contador de instancias

    def __init__(self, curso, dia, hora_inicio, hora_fin):
        self.curso = curso
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        Horario.total_horarios += 1  # Aumenta el contador cada vez que se crea un horario
    def mostrar_horario(self):
        return f'{self.curso} - {self.dia}: {self.hora_inicio} - {self.hora_fin}'
    def modificar_horario(self,nuevo_horario: dict):
        self.hora_inicio = nuevo_horario.get("horario_inicio",self.hora_inicio)
        self.hora_fin = nuevo_horario.get("horario_fin",self.hora_fin)
    def __str__(self):
        return self.mostrar_horario()
