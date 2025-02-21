class Aula:
    total_aulas = 0  # Contador de instancias

    def __init__(self, numero, capacidad, recursos):
        self.numero = numero
        self.capacidad = capacidad
        self.recursos = recursos
        self.reservada= False
        Aula.total_aulas += 1  # Aumenta el contador cada vez que se crea un aula

    def mostrar_detalles(self) -> str:
        return (f'Este colegio tiene {type(self).total_aulas} clases. Esta clase en concreto tiene {self.capacidad} estudiantes \
                su numero es {self.numero} y tiene estos recursos: {self.recursos}')
    def reservar_aula(self,):
        self.reservada= True
        print('La clase esta reservada.')

    @ classmethod
    def desde_tupla(cls, tupla) -> object:
        return cls(tupla[0],tupla[1],tupla[2])
    def es_adecuada_para_clase(nombre):
        print(f'{nombre} sera una gran adicion a la clase.')

    def __str__(self):
        return f'{type(self).__name__}, {type(self).total_aulas}, {self.numero}, {self.capacidad}, {self.recursos}'
    def __repr__(self):
        return f'{type(self).__name__}, (total_aulas = {type(self).total_aulas}, numero= {self.numero}\
    capacidad = {self.capacidad}, recursos = {self.recursos}'