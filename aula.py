class Aula:
    total_aulas = 0  # Contador de instancias

    def __init__(self, numero: str, capacidad: int, recursos: list[str]):
        self.numero = numero
        self.capacidad = capacidad
        self.recursos = recursos
        Aula.total_aulas += 1  # Aumenta el contador cada vez que se crea un aula

    def __repr__(self):
        return (
            f'{type(self).__name__}' # Devuelve el nombre de la clase
            # Devolvemos los atributos de instancia
            f'(Número: "{self.numero}"), '
            f'(Capcidad: "{self.capacidad}"), '
            f'(Recursos: "{self.recursos}"), '
            # Devolvemos el atributo de clase
            f'Total aulas: {type(self).total_aulas}'
        )

    @classmethod
    def desde_tupla(cls, tupla: tuple):
        # Creamos un alumno desde una tupla dada
        return cls(*tupla)
        # El asterisco es para "descomprimir la tupla en todos sus elementos"

    @staticmethod
    def es_adecuada_para_clase(edad):
        if edad > 18 and edad < 25:
            return True
        else:
            return False