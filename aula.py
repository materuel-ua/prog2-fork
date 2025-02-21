class Aula:
    total_aulas = 0  # Contador de instancias

    def __init__(self, numero, capacidad, recursos):
        self.numero = numero
        self.capacidad = capacidad
        self.recursos = recursos
        Aula.total_aulas += 1  # Aumenta el contador cada vez que se crea un aula

    def mostrar_datos(self):
        print(f'el aula {self.aula} tiene una capacida de {self.capacidad} y tiene {self.recursos}')
    
    def reservar_aula(self,curso):
        print(f'El aula {self.aula} está reservada para el curso {curso}')

    def __str__(self):
        return f'{self.aula} - capacidad:{self.capacidad}, tiene {self.recursos}'
    
    def __repr__(self):
        return f' aula: {self.aula} capacidad: {self.capacidad}'
