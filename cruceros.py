class Cruceros:
    def __init__ (self, name, route, departure, cost, rooms, capacity, sells):
        self.name = name
        self. route = route
        self. departure = departure
        self.cost = cost
        self.rooms = rooms
        self.capacity = capacity
        self.sells = sells

    def show(self):
        return'''
        El crucero se llama: {}
        Su ruta es: 
        Fecha y Hora de salida :{}
        Tiene un costo de: {} segun las habitaciones que son {}
        cuya capacidad es: {} respectivamente
        Ademas cuenta con venta de: {}.'''.format(self.name, self.route, self.departure, self.cost, self.rooms, self.capacity, self.sells)
