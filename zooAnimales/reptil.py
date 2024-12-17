from .animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0
    _colorEscamas = True
    _largoCola = 4

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)
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

    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, pa: int) -> None:
        self._largoCola = pa

    def cantidadReptiles(self) -> int:
        return len(self._listado)

    @classmethod
    def crearIguana(cls, nombre, edad, genero) -> Animal:
        cls._colorEscamas = 'verde'
        cls._largoCola = 3
        cls.setHabitat(cls, 'humedal')
        Reptil.iguanas += 1
        return Reptil(nombre, edad, cls.getHabitat(cls), genero, cls._colorEscamas, cls._largoCola)

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero) -> Animal:
        cls._colorEscamas = 'blanco'
        cls._largoCola = 1
        cls.setHabitat(cls, 'jungla')
        Reptil.serpientes += 1
        return Reptil(nombre, edad, cls.getHabitat(cls), genero, cls._colorEscamas, cls._largoCola)

    def movimiento():
        return 'reptar'