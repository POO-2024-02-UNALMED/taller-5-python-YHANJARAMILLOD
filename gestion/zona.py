from zooAnimales.animal import Animal

class Zona():

    def __init__(self, nombre: str, zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    def agregarAnimales(self, animal: Animal):
        animal.setZona(self)
        self._animales.append(animal)

    def cantidadAnimales(self):

        return len(self._animales)
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getZoo(self):
        return self._zoo
    
    def setZoo(self, zoo):
        self._zoo = zoo