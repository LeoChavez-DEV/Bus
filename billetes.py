from cliente import Cliente
from bus import Bus

class Billete:
    def __init__(self, cliente: Cliente, bus: Bus):
        self.setCliente(cliente)
        self.setBus(bus)

    def vender(self):
        return self.bus.vender_billete(self.cliente)
    
    def devolver(self):
        return self.bus.devolver_billete(self.cliente)