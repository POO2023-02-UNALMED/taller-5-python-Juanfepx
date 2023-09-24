class Animal:
    totalAnimals = 0

    def __init__(self, nombre, edad, habitat, genero):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = None
        Animal.totalAnimals += 1

    def movimiento(self):
        return "desplazarse"

    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.ave import Ave
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.pez import Pez
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.reptil import Reptil
        return ("Mamiferos : " + str(Mamifero.cantidadMamiferos()) + "\n" +
                "Aves : " + str(Ave.cantidadaAves()) + "\n" +
                "Reptiles : " + str(Reptil.cantidadReptiles()) + "\n" +
                "Peces : " + str(Pez.cantidadPeces()) + "\n" +
                "Anfibios : " + str(Anfibio.cantidadAnfibios()))

    def toString(self):
        if self.zona is not None:
            return "Mi nombre es " + str(self.nombre) + ", tengo una edad de " + str(self.edad) + ", habito en " + str(
                self.habitat) + " y mi genero es " + str(self.genero) + ", la zona en la que me ubico es " + str(
                self.zona) + ", en el" + str(self.zona.getZoo())
        else:
            return "Mi nombre es " + str(self.nombre) + ", tengo una edad de " + str(self.edad) + ", habito en " + str(
                self.habitat) + " y mi genero es " + str(self.genero)

    def getNombre(self):
        return self.nombre

    def getHabitat(self):
        return self.habitat

    def getEdad(self):
        return self.edad

    def getGenero(self):
        return self.genero
