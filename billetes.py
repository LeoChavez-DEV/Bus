from cliente import Cliente

class Billete(Cliente):
    def __init__(self, venta, devolucion, cliente):
        self.setVenta(venta)
        self.setDevolucion(devolucion)
        super().__init__(cliente)

    def setVenta(self, venta):
        self.__venta = venta

    def getVenta(self, venta):
        self.__venta = venta
    
    def setDevolucion(self, devolucion):
        self.__devolucion = devolucion
    
    def getDevolucion(self, devolucion):
        self.__devolucion = devolucion

    def __str__(self):
        f"{super().__init__()} ha comprado {self.getVenta()} y ha devuelto {self.getDevolucion}"