class Cliente:
    def __init__(self, nombre, apellido):
        self.setNombre(nombre)
        self.setApellido(apellido)
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getNombre(self):
        return self.__nombre
    
    def setApellido(self, apellido):
        self.__apellido = apellido
    
    def getApellido(self):
        return self.__apellido
    
    def __str__(self):
        return f"Cliente: {self.getNombre()} {self.getApellido()}"