from .animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0
    _colorPiel = True
    _venenoso = 4

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)
        Animal.setTotalAnimales(Animal.getTotalAnimales() + 1)

    @classmethod
    def getListado(cls):
        return cls._listado
    
    def setListado(self, L: list) -> None:
        self._listado = L

    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, pe: bool) -> None:
        self._colorPiel = pe

    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, pa: int) -> None:
        self._venenoso = pa

    def cantidadAnfibios(self) -> int:
        return len(self._listado)

    @classmethod
    def crearRana(cls, nombre, edad, genero) -> Animal:
        cls._colorPiel = 'rojo'
        cls._venenoso = True
        cls.setHabitat(cls, 'selva')
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, cls.getHabitat(cls), genero, cls._colorPiel, cls._venenoso)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero) -> Animal:
        cls._colorPiel = 'negro y amarillo'
        cls._venenoso = False
        cls.setHabitat(cls, 'selva')
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, cls.getHabitat(cls), genero, cls._colorPiel, cls._venenoso)

    def movimiento():
        return 'saltar'
    
