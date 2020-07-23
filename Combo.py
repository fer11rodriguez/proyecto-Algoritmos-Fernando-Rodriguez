class Combo:

    def __init__ (self, name, cantidad, products, price):
        self.name = name
        self.cantidad = cantidad
        self.products = products
        self. price = price

    def mostrar_combo (self):
        return '{}, {} USD'. format(self.name,  self.price)