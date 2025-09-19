class Bus:
    
    def __init__(self, idBus, bus, capacidad):
        self.setIdBus(idBus)
        self.setBus(bus)
        self.setCapacidad(capacidad)

    # Getters      
    def getIdBus(self):
        return self.__idBus

    def getBus(self):
        return self.__bus

    def getCapacidad(self):
        return self.__capacidad

    # Setters
    def setIdBus(self, idBus):
        self.__idBus = idBus
    
    def setBus(self, bus):
        self.__bus = bus
    
    def setCapacidad(self, capacidad):
        self.__capacidad = capacidad

    def __str__(self):
        return f"ID: {self.getIdBus()}, Buses: {self.getBus()}, capacidad: {self.getCapacidad()}"
