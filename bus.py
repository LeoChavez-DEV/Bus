class bus:
    def Bus():
        def __init__(self, bus, plazas):
            self.setBus(bus)
            self.setPlazas(plazas)

        def getBus(self, bus):
            return self.bus
        
        def getPlazas(self, plazas):
            return self.plazas
        
        def setBus(self, bus):
            return self.__bus
        
        def setPlazas(self, plazas):
            return self.__plazas
        
        def __str__(self):
            return f"Buses: {self.getBus()}, plazas: {self.getPlazas()}"
        
        

