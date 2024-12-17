from .animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0
    _pelaje = True
    _patas = 4

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)
        Animal.setTotalAnimales(Animal.getTotalAnimales() + 1)

    @classmethod
    def getListado(cls):
        return cls._listado
    
    def setListado(self, L: list) -> None:
        self._listado = L

    def isPelaje(self):
        return self._pelaje
    
    def setPelaje(self, pe: bool) -> None:
        self._pelaje = pe

    def getPatas(self):
        return self._patas
    
    def setPatas(self, pa: int) -> None:
        self._patas = pa

    def cantidadMamiferos(self) -> int:
        return len(Mamifero._listado)
    
    @classmethod
    def crearCaballo(cls, nombre, edad, genero) -> Animal:
        cls._pelaje = True
        cls._patas = 4
        cls.setHabitat(cls, 'pradera')
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, cls.getHabitat(cls), genero, cls._pelaje, cls._patas)

    @classmethod
    def crearLeon(cls, nombre, edad, genero) -> Animal:
        cls._pelaje = True
        cls._patas = 4
        cls.setHabitat(cls, 'selva')
        Mamifero.leones += 1
        return Mamifero(nombre, edad, cls.getHabitat(cls), genero, cls._pelaje, cls._patas)
    