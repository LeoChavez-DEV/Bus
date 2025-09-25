from cliente import Cliente
from billetes import Billete

class Bus:
    
    def __init__(self, idBus, capacidad):
        self.setIdBus(idBus)
        self.setCapacidad(capacidad)
        self._billetes = []

    # Getters      
    def getIdBus(self):
        return self.__idBus

    def getCapacidad(self):
        return self.__capacidad

    # Setters
    def setIdBus(self, idBus):
        self.__idBus = idBus
    
    def setCapacidad(self, capacidad):
        self.__capacidad = capacidad
        
    def capacidadLibre(self):
        return self.__capacidad - len(self._billetes)
    

    def __str__(self):
        return f"ID: {self.getIdBus()}, Capacidad: {self.getCapacidad()}"
