from zooAnimales.animal import Animal


class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        self.listado.append(self)

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls.listado)

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)

    def movimiento(self):
        return "desplazarse"

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)

    def isPelaje(self):
        return self.pelaje

    def getPatas(self):
        return self.patas
