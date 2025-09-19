class bus:
    def Bus():
        def __init__(self, idBus, bus, plazasLibres, plazasComletas):
            self.setIdBus(idBus)
            self.setBus(bus)
            self.setPlazasLibres(plazasLibres)
            self.setPlazasComletas(plazasComletas)

        # Getters      
        def getIdBus(self):
            return self.__idBus

        def getBus(self):
            return self.__bus

        def getPlazasLibres(self):
            return self.__plazasLibres

        def getPlazasComletas(self):
            return self.__plazasComletas

        # Setters
        def setIdBus(self, idBus):
            self.__idBus = idBus
        
        def setBus(self, bus):
            self.__bus = bus
        
        def setPlazasCompletas(self, plazasComletas):
            self.__plazasCompletas = plazasComletas
        
        def setPlazasLibres(self, plazasLibres):
            self.__plazasLibres = plazasLibres

        def __str__(self):
            return f"ID: {self.getIdBus()}, Buses: {self.getBus()}, plazaCompletas: {self.getPlazasCompletas()}, plazasLibres: {self.getPlazasLibres()}"
        
        

