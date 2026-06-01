"""
Semana 2 - Programación Orientada a Objetos
Tema: Clase y objeto

Una clase es una plantilla o modelo que define las características
y comportamientos que tendrán los objetos.

Un objeto es una instancia concreta creada a partir de una clase.
"""


class Automovil:
    """
    La clase Automovil representa un modelo general de automóvil.
    Define atributos como marca, modelo y velocidad.
    """

    def __init__(self, marca, modelo, velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def acelerar(self):
        """
        Incrementa la velocidad del automóvil.
        """
        self.velocidad += 10

    def mostrar_informacion(self):
        """
        Muestra la información del automóvil.
        """
        print(f"Automóvil: {self.marca} {self.modelo}")
        print(f"Velocidad actual: {self.velocidad} km/h")


# Creación de un objeto a partir de la clase Automovil
mi_auto = Automovil("Toyota", "Corolla")

# Uso de un método del objeto
mi_auto.acelerar()

# Mostrar información del objeto
mi_auto.mostrar_informacion()