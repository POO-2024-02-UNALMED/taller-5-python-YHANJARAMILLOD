class Animal():
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, n: str) -> None:
        self._ = n

    def getEdad(self):
        return self._edad
    
    def setEdad(self, e: int) -> None:
        self._edad = e

    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, h: str) -> None:
        self._habitat = h

    def getGenero(self):
        return self._genero
    
    def setGenero(self, g: str) -> None:
        self._genero = g

    def getZona(self):
        return self._zona
    
    def setZona(self, z: str) -> None:
        self._zona = z

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    
    @classmethod
    def setTotalAnimales(cls, t: int) -> None:
        cls._totalAnimales = t

    @classmethod
    def totalPorTipo(cls):
        from .mamifero import Mamifero
        from .ave import Ave
        from .reptil import Reptil
        from .pez import Pez
        from .anfibio import Anfibio

        ml = Mamifero.getListado()
        al = Ave.getListado()
        rl = Reptil.getListado()
        pl = Pez.getListado()
        anl = Anfibio.getListado()

        return f'Mamiferos : {len(ml)}\nAves : {len(al)}\nReptiles : {len(rl)}\nPeces : {len(pl)}\nAnfibios : {len(anl)}'
    
    def movimiento():
        return 'desplazarse'
    
    def __str__(self):

        return f'Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}'