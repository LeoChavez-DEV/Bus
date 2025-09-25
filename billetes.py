from cliente import Cliente

class Billete:
    def __init__(self, cliente: Cliente, bus):
        self.cliente = cliente
        self.bus = bus

    def vender(self):
        return self.bus.venderBillete(self.cliente)

    def devolver(self):
        return self.bus.devolverBillete(self.cliente)
