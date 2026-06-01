"""
Semana 2 - Programación Orientada a Objetos
Tema: Polimorfismo

El polimorfismo permite que distintos objetos respondan
de manera diferente a una misma acción.
"""


class Animal:
    """
    Clase base.

    Define un método general llamado hacer_sonido.
    """

    def hacer_sonido(self):
        pass


class Perro(Animal):
    """
    Clase hija que redefine el método hacer_sonido.
    """

    def hacer_sonido(self):
        return "Guau"


class Gato(Animal):
    """
    Clase hija que redefine el método hacer_sonido.
    """

    def hacer_sonido(self):
        return "Miau"


# Lista de objetos de diferentes clases
animales = [Perro(), Gato()]

# La misma acción produce resultados diferentes
for animal in animales:
    print(animal.hacer_sonido())