"""
Semana 2 - Programación Orientada a Objetos
Tema: Herencia

La herencia permite crear nuevas clases a partir de una clase existente.
Esto ayuda a reutilizar código y organizar mejor las clases.
"""


class Animal:
    """
    Clase padre o clase base.

    Contiene atributos y métodos comunes para todos los animales.
    """

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def moverse(self):
        """
        Método común para todos los animales.
        """
        return f"{self.nombre} se está moviendo."


class Perro(Animal):
    """
    Clase hija que hereda de Animal.

    Un perro es un animal, por eso puede reutilizar
    los atributos y métodos de la clase Animal.
    """

    def ladrar(self):
        return "Guau"


class Gato(Animal):
    """
    Clase hija que hereda de Animal.

    Un gato también es un animal y puede reutilizar
    los atributos y métodos de la clase Animal.
    """

    def maullar(self):
        return "Miau"


# Creación de objetos de las clases hijas
perro = Perro("Firulais", 3)
gato = Gato("Michi", 2)

# Ambos objetos pueden usar el método heredado de Animal
print(perro.moverse())
print(gato.moverse())

# Cada clase hija también puede tener sus propios métodos
print(perro.ladrar())
print(gato.maullar())