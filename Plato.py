class Plato:

    def __init__ (self, name, classification, option, price):
        self.name = name
        self.classification = classification
        self. option = option
        self. price = price

    def mostrar_plato (self):
        return '{}, es {}, de {},{} USD'. format(self.name, self.classification, self.option, self.price)