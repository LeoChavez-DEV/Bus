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
    
    def venderBillete(self, cliente):
        if self.capacidadLibre() <= 0:
            print ("No hay plazas disponibles")
        
        billete = Billete(cliente, self)
        self.billetes.append(billete)
        return billete
    
    def devolverBillete(self, cliente):
        for b in self._billetes:
            if b.cliente == cliente:
                self._billetes.remove(b)
                return True
        return False
    
    def estado(self):
        return (
        f"Bus {self._nombre} (ID {self._id_bus})\n"
        f"Total: {self._capacidad}\n"
        f"Libre: {self.capacidad_libre()}\n"
        f"Vendido: {len(self._billetes)}"
    )
        
    def __str__(self):
        return f"ID: {self._id_bus}, Capacidad: {self._capacidad}"
    
    # 
