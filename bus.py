from cliente import Cliente
from billetes import Billete

class Bus:
    def __init__(self, idBus, capacidad):
        self.__idBus = idBus
        self.__capacidad = capacidad
        self._billetes = []

    def getIdBus(self):
        return self.__idBus

    def getCapacidad(self):
        return self.__capacidad

    def capacidadLibre(self):
        return self.__capacidad - len(self._billetes)

    def venderBillete(self, cliente: Cliente):

        for b in self._billetes:
            if b.cliente.getNombre() == cliente.getNombre() and b.cliente.getApellido() == cliente.getApellido():
                print("El cliente ya tiene un billete en este bus.")
                return False

        if self.capacidadLibre() <= 0:
            print("No hay plazas disponibles")
            return False

        billete = Billete(cliente, self)
        self._billetes.append(billete)
        return True

    def devolverBillete(self, cliente: Cliente):
        for b in self._billetes:
            if b.cliente.getNombre() == cliente.getNombre() and b.cliente.getApellido() == cliente.getApellido():
                self._billetes.remove(b)
                return True
        print("No se encontró billete para devolver.")
        return False

    def estado(self):
        return (
            f"Bus {self.__idBus}\n"
            f"Total: {self.__capacidad}\n"
            f"Libre: {self.capacidadLibre()}\n"
            f"Vendido: {len(self._billetes)}"
        )