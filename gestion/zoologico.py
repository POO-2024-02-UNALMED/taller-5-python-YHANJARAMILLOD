class Zoologico():

    def __init__(self, nombre: str, ubicacion: str):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def agregarZonas(self, zona):
        self._zonas.append(zona)
        zona._zoo = self

    def cantidadTotalAnimales(self):
        cont = 0
        for zona in self._zonas:
            cont += zona.cantidadAnimales()

        return cont
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getZona(self):
        return self._zonas
    
    def setZona(self, z) -> None:
        self._zona = z