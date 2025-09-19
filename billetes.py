from cliente import Cliente
class Billete():

    # def __init__(self, Cliente):
    #     Cliente.__init__(self, nombre, apellido)

    

    
    def __init__(self, tickets, espacio_libre, billetes_vendido):
        Cliente.__init__(self, nombre, apellido)
        self.setTickets(tickets)
        self.setEspacio_libre(espacio_libre)
        self.setBilletes_vendido(billetes_vendido)
        
        def getTickets(self):
            return self.tickets
        def getEspacio_libre(self):
            return self.espacio_libre
        def getBilletes_vendido(self):
            return self.billetes_vendido


        def setTickets(self, tickets):
            self.__tickets = tickets
        def setEspacio_libre(self, espacio_libre):
            self.__espacio_libre = espacio_libre
        def setBilletes_vendido(self, billetes_vendido):
            self.__billetes_vendido = billetes_vendido