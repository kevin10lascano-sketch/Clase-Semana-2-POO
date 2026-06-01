"""
Semana 2 - Programación Orientada a Objetos
Tema: Abstracción

La abstracción permite representar solo las características
y comportamientos importantes de un objeto, ignorando detalles
que no son necesarios para resolver el problema.
"""


class Auto:
    """
    Esta clase representa un automóvil de manera simplificada.

    No se modelan todos los detalles reales del vehículo,
    como motor, cables, tornillos o sistema eléctrico.
    Solo se consideran los datos necesarios para este ejemplo.
    """

    def __init__(self, marca, modelo, velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def acelerar(self):
        """
        Aumenta la velocidad del automóvil.
        """
        self.velocidad += 10

    def mostrar_estado(self):
        """
        Muestra el estado actual del automóvil.
        """
        print(f"Auto: {self.marca} {self.modelo}")
        print(f"Velocidad: {self.velocidad} km/h")


# El modelo conserva solo la información necesaria.
auto = Auto("Toyota", "Yaris")

auto.acelerar()
auto.mostrar_estado()