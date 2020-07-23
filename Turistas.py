class Turista:

    def __init__ (self, name, dni, age, check):
        self.name =  name
        self.dni = dni
        self.age = age
        self.check = check

    def ver_cuenta(self):
        print (f'Hasta el momento debes {self.check}')

    def tour_puerto (self, price):
        self.check += price

    def comida_local (self, price):
        self.check += price

    def trotar (self, price):
        self.check += price

    def lugares_historicos (self, price):
        self.check += price