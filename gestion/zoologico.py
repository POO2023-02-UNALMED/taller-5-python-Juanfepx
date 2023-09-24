class Zoologico:

    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []
    def getNombre(self):
        return self.nombre

    def cantidadTotalAnimales(self):
        contador = 0
        for zona in self.zonas:
            contador += zona.cantidadAnimales()
        return contador

    def getZona(self):
        return self.zonas

    def agregarZonas(self, zona):
        self.zonas.append(zona)
