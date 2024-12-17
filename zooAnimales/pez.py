
from .animal import Animal
class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0
    _colorEscamas = ''
    _cantidadAletas = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorEscamas = pelaje
        self._cantidadAletas = patas
        Pez._listado.append(self)
        Animal.setTotalAnimales(Animal.getTotalAnimales() + 1)

    @classmethod
    def getListado(cls):
        return cls._listado
    
    def setListado(self, L: list) -> None:
        self._listado = L

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, pe: bool) -> None:
        self._colorEscamas = pe

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setAletas(self, pa: int) -> None:
        self._cantidadAletas = pa

    def cantidadPeces(self) -> int:
        return len(self._listado)

    @classmethod
    def crearSalmon(cls, nombre, edad, genero) -> Animal:
        cls._colorEscamas = 'rojo'
        cls._cantidadAletas = 6
        cls.setHabitat(cls, 'oceano')
        Pez.salmones += 1
        return Pez(nombre, edad, cls.getHabitat(cls), genero, cls._colorEscamas, cls._cantidadAletas)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero) -> Animal:
        cls._colorEscamas = 'gris'
        cls._cantidadAletas = 6
        cls.setHabitat(cls, 'oceano')
        Pez.bacalaos += 1
        return Pez(nombre, edad, cls.getHabitat(cls), genero, cls._colorEscamas, cls._cantidadAletas)

    def movimiento():
        return 'nadar'
 