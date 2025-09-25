from cliente import Cliente

class Billete:
    def __init__(self, cliente, bus):
        self.cliente = cliente
        self.bus = bus

    def vender(self):
        return self.bus.venderBillete(self.cliente)

    def devolver(self):
        return self.bus.devolverBillete(self.cliente)
