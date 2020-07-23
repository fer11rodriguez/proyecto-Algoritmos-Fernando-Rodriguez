class Pasajero:
    def __init__ (self, name, dni, age, disability, count):
        self.name = name
        self.dni = dni
        self.age = age
        self.disability = disability
        self.count = count

    def passenger_characteristics (self):
        return 'El nombre del pasajero es: {} | DNI: {} | Edad: {} | Discapacidad: {} | Saldo: {}'''.format (self.name, self.dni, self.age, self.disability, self.count)

    def ver_cuenta(self):
        print (f'Hasta el momento debes {self.count}')

    def tour_puerto (self, price):
        self.count += price

    def comida_local (self, price):
        self.count += price

    def trotar (self, price):
        self.count += price

    def lugares_historicos (self, price):
        self.count += price
