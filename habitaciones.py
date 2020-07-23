class Habitacion:
    def __init__ (self, tipo, letter, capacity, number, name, info):
        self.tipo = tipo
        self.letter = letter
        self.capacity = capacity
        self.number = number
        self.name = name
        self.info = info
    def room_characteristics(self):
        return' Habitacion {}, {}{}, puede hospedar a {} personas, su huesped actual es: {}'.format (self.type, self.letter, self.number, self.name, self.info)

from random import randrange
from random import choice
import random
halls = ['A', 'B','C', 'D', 'E']
letra = random.randint (0, 4)
answer = choice(['si', 'no'])
print (answer)
