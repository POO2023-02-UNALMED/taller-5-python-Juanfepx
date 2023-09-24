from Ave import Ave
from Anfibio import Anfibio
from Pez import Pez
from Mamifero import Mamifero
from Reptil import Reptil


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
        return "Mamiferos: " + Mamifero.cantidadMamiferos() + "\n" + "Aves: " + Ave.cantidadaAves() + "\n" + "Reptiles: " + Reptil.cantidadReptiles() + "\n" + "Peces: " + Pez.cantidadPeces() + "\n" + "Anfibios: " + Anfibio.cantidadAnfibios()

    def __str__(self):
        if self.zona is not None:
            return "Mi nombre es " + self.nombre + ", tengo una edad de " + self.edad + ", habito en " + self.habitat + " y mi genero es " + self.genero + ", la zona en la que me ubico es " + self.zona + ", en el" + self.zona.getZoo()
        else:
            return "Mi nombre es " + self.nombre + ", tengo una edad de " + self.edad + ", habito en " + self.habitat + " y mi genero es " + self.genero

    def getNombre(self):
        return self.nombre

    def getHabitat(self):
        return self.habitat

    def getEdad(self):
        return self.edad

    def getGenero(self):
        return self.genero
